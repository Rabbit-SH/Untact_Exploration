from PIL import Image
from fastapi.staticfiles import StaticFiles
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import requests
import tempfile
from io import BytesIO
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth
import cv2
import subprocess
import os
import uvicorn
from fastapi import BackgroundTasks, FastAPI, File, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil

#모델 파일 import (수묵화, 애니메이션, 만화)




app = FastAPI()
#CORS 오류 해결
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프론트엔드 서버 주소
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

def remove_file(path: str):
    try:
        os.remove(path)
    except Exception as e:
        print(f"Error while deleting file {path}: {e}")
        
def segment_image(image, k=3):
    
    # 이미지를 NumPy 배열로 변환
    data = np.array(image)

    # 이미지 데이터를 2D로 변환 (각 픽셀은 RGB 색상을 가짐)
    w, h, d = data.shape
    data = data.reshape((w * h, d))

    # KMeans 클러스터링
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
    labels = kmeans.predict(data)

    # 클러스터링 결과에 따라 색상 재할당
    segmented_data = kmeans.cluster_centers_.astype('uint8')[labels]

    # 2D 데이터를 원래 이미지 크기로 다시 변환
    segmented_image = segmented_data.reshape((w, h, d))

    return Image.fromarray(segmented_image)

def adjust_brightness_dynamic(image, dark_factor=1.5, bright_factor=1):
    
    # Ensure the image is a float type for calculations
    if image.dtype != np.float32:
        image = image.astype(np.float32)

    # Find the mean value of the image for threshold
    mean_value = np.mean(image)

    # Apply different factors based on brightness
    adjusted_image = np.where(image <= mean_value, image / dark_factor, image * bright_factor)

    # Clip the values to ensure they remain within the range and convert back to original data type
    adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)

    return adjusted_image

def load_and_preprocess(image_path):
    
  # 이미지 읽어오기
  image = cv2.imread(image_path)
  # 이미지 크기 확인
  height, width = image.shape[:2]
  # 이미지 크기를 절반으로 조정
  resized_image = cv2.resize(image, (width // 2, height // 2))
  # color segmentation
  segmented_img = segment_image(resized_image, 5)

  #numpy 오류 해결
  if isinstance(segmented_img, Image.Image):
    segmented_img = np.array(segmented_img)

  # 그레이스케일로 변경
  gray_image = cv2.cvtColor(segmented_img, cv2.COLOR_BGR2GRAY)

  # 클라해 수행
  # Adaptive Histogram Equalization 적용
  clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
  clahe_image = clahe.apply(gray_image)
  
  # 픽셀 조절
  dynamic_img = adjust_brightness_dynamic(clahe_image)

  return dynamic_img
app.mount("/waterfrog/",StaticFiles(directory="C:/Users/herji/OneDrive/문서/GitHub/Untact_Exploration/front-end/dist",html=True),name="waterfrog")
@app.get("/",response_class=HTMLResponse)
async def root_root():
    return """
        
        """
@app.post("/transform/sumuk")
async def load_image(background_tasks: BackgroundTasks,file: UploadFile=File(...)):
    #업로드된 사진 경로 설정해서 저장.
    input_image_path = f'./{file.filename}'
    with open(input_image_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    preprocessed_image = load_and_preprocess(input_image_path)
    
    #전처리된 이미지 저장.
    cv2.imwrite("./input/preprocessed_image.jpg", preprocessed_image)
    
    #이미지 변환.
    command = 'python render-keep-ratio.py --model model_save --inp "./input/preprocessed_image.jpg" --oup output --size 1024'

    # 명령어 실행 및 stdout와 stderr 캡처
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 실행 결과와 오류 메시지 출력
    print("STDOUT:\n", result.stdout.decode())
    print("STDERR:\n", result.stderr.decode('utf-8', errors='replace'))

    # 이미지를 열어서 저장
    result_image = Image.open('output/stylized.jpg')
    result_image.save('output/style_transfer_image.jpg')
    
    response = FileResponse('output/style_transfer_image.jpg',media_type='image/jpeg')
    
    #파일 전송 후 삭제
    background_tasks.add_task(remove_file, input_image_path)
    background_tasks.add_task(remove_file, "./input/preprocessed_image.jpg")
    background_tasks.add_task(remove_file, 'output/style_transfer_image.jpg')

    return response
# @app.post("/transform/animation") # 애니메이션 로직



# @app.post("/transform/cartoon") # 만화 로직




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)