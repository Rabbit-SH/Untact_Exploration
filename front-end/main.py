import glob
from fastapi import BackgroundTasks, FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import PIL.Image
import os
# import functools

import uvicorn
class Item(BaseModel):
    pass
# import tempfile

app = FastAPI()
#CORS 오류 해결
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080","http://192.168.35.20:8080","https://hyeoong.github.io"],  # 프론트엔드 서버 주소
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)
hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
# class TransferData(BaseModel):
#     result: str
def remove_file(path: str):
    try:
        os.remove(path)
    except Exception as e:
        print(f"Error while deleting file {path}: {e}")
def load_image_from_file(file_path, image_size=(512, 512), preserve_aspect_ratio=True):
    image = PIL.Image.open(file_path)
    image = np.array(image)
    # convert_image_dtype : 타입 변환과 동시에 픽셀값을 0~1 정규화
    image = tf.image.convert_image_dtype(image, tf.float32)
    # 배치크기 1로 설정하여 추가
    image = image[tf.newaxis, ...]
    # image = crop_center(image)   나는 자르지 않고 압축입력함
    image = tf.image.resize(image, image_size, preserve_aspect_ratio=preserve_aspect_ratio)
    return image

def transform_image(content_image, style_image):
    # 스타일 전이 적용
    outputs = hub_module(content_image, style_image)
    stylized_image = outputs[0]
    return stylized_image

@app.post("/upload")
async def create_upload_file(background_tasks: BackgroundTasks,file: UploadFile = File(...)):
    
    #업로드한 사진 저장
    content_image_path = f"./static/datasets/photo/{file.filename}"
    with open(content_image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    content_image = load_image_from_file(content_image_path,(512,512))
    
    # # 스타일 이미지 가져오기(한장)
    # style_file_path = './static/datasets/style/sample2.jpg'
    # style_image = load_image_from_file(style_file_path,(384,384))
    # stylized_image = transform_image(content_image, style_image)
    
    # # 변환된 사진 저장할 경로
    # output_path = f'./result/{file.filename}_stylized_image.jpg'
    
    # # 이미지 저장
    # stylized_image_to_save = tf.image.convert_image_dtype(stylized_image, dtype=tf.uint8)
    # stylized_image_to_save = PIL.Image.fromarray(stylized_image_to_save.numpy()[0])
    # stylized_image_to_save.save(output_path)
    
    # 스타일 이미지 가져오기 (여러장)
    
    style_images_path = glob.glob('./static/datasets/style/*.jpg') # 스타일 이미지 경로
    
    stylized_images = []
    for style_image_path in style_images_path:
        style_image = load_image_from_file(style_image_path)
        outputs = hub_module(tf.constant(content_image),tf.constant(style_image))
        stylized_image = outputs[0]
        stylized_images.append(stylized_image)
        
    combined_stylized_image = tf.reduce_mean(tf.stack(stylized_images),axis=0)
    
    output_path = f'./static/datasets/result/{file.filename}_combined_image.jpg'
    stylized_image_to_save = tf.image.convert_image_dtype(combined_stylized_image,dtype=tf.uint8)
    stylized_image_to_save = PIL.Image.fromarray(stylized_image_to_save.numpy()[0])
    
    stylized_image_to_save.save(output_path)   
    response = FileResponse(output_path,media_type='image/jpeg')
    
    #파일 전송 후 삭제
    background_tasks.add_task(remove_file, content_image_path)
    background_tasks.add_task(remove_file, output_path)
    
    return response

# Uvicorn 서버 실행
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)