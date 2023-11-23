<template>
    <div class="background" justify="center" align="center">
        <h1 class="pt-10">AI 화가</h1>
        <div class="uploadIMG mt-16" justify="center" align="center">
            <img v-if="imageUrl" :src="imageUrl" alt="preview Image" class="preview_img mt-7">
        </div>
  
        <div v-if="!imageUrl" class="button_container my-16">
            <input type = "file" @change="uploadImg" class='input' ref="fileInput" style="display: none;" />
            <v-btn class="chooseIMG py-6 text-h5 white--text" color="#EF8200" @click="triggeruploadImg"> 사진 선택 </v-btn>
        </div> 
        <div v-if="imageUrl" class="button_container2 my-16 d-flex">
            <input type = "file" @change="uploadImg" class='input' ref="fileInput" style="display: none;" />
            <v-btn class="againChooseImg py-6 text-h5 white--text" color="#EF8200" @click="triggeruploadImg">재촬영</v-btn>
            <v-btn class="translateImg py-6 text-h5 white--text" color="#EF8200" @click="transformImg">한국화 그리기</v-btn>
        </div>
        <div class="galley_container d-flex my-10 mr-16">
            <v-icon color="white" class="mr-5" size="25" @click="downloadImage">mdi mdi-download</v-icon>
            <v-icon color="white" size="25" @click="openGallery">mdi mdi-image-album</v-icon>
        </div>

        <GalleryView :show="gallery" @close="closeGallery" />
  

        <v-dialog v-model="dialog" max-width="500">
            <v-card class="text-center dialog_Card">
            <v-card-text class="pa-5 pt-10">
                <div class="text_container">
                    <strong>한국화</strong>는 한국의 전통 그림이에요!<br>
                    붓과 먹을 사용해서<br>부드러운 선으로 그린답니다~<br><br>
                    여기에 찍은 사진을 올려주면 <br>AI 화가가 사진을 한국화로 그려줄거에요!!
                </div>
                <br>
                <br>
                <br>
                <div class="example_container d-flex justify-center align-center">
                <img :src="require('@/assets/AIView/origin.jpg')">
                <v-icon>mdi mdi-arrow-right-thick</v-icon>
                <img :src="require('@/assets/AIView/koreaPaint.png')">
                </div>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                color="orange"
                text
                @click="dialog = false"
                >
                확인
                </v-btn>
            </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
  
<script>
import GalleryView from './GalleryView.vue';
import axios from 'axios';

export default {
    name: 'AIView2',
    components:{GalleryView,},
    data(){
        return{
            dialog: true, //true로 바꿔야 함

            imageUrl: null,
            preimage: null,
            istranslated: false,
            response: null,

            gallery: false,

        }
    },
    methods:{
        downloadImage() {
            if (this.imageUrl){
                const link = document.createElement('a');
                link.href = this.imageUrl;
                link.download = 'stylized_image.jpg';  // 다운로드될 파일명 설정
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                this.istranslated = false
            } else {
                alert('사진을 업로드 후 이용해주세요.')
            }
            
        },
        async uploadImg(event) {
            // 이미지 업로드 로직
            //만약 사진을 고르지 않았다면?
            this.imageUrl = null;
            this.preimage = event.target.files[0];
            if (!this.preimage) {
                console.log("파일을 선택해주세요.");
                return;
            }
            const fileReader = new FileReader();
            fileReader.readAsDataURL(this.preimage)
            fileReader.onload = () => {
                    this.imageUrl = fileReader.result;
                    // EventBus.$emit('add-photo', this.photoDataUrl);
            }
            this.istranslated = false
  
        },
        triggeruploadImg(){
            this.$refs.fileInput.click();
        },
        beforeUnload(event) {
            // 이벤트 취소 메시지 설정
            event.preventDefault();
            event.returnValue = ''; // 대부분의 브라우저에서는 이 메시지가 표시되지 않습니다.
        },
        async transformImg() {
            // 이미지 변환 페이지로 이동하는 함수
            if (!this.preimage) {
                alert("사진을 선택해주세요!")
                return;
            }

            // 서버로 전송 하는 로직.
            const formData = new FormData();
            formData.append("file", this.preimage);

            this.loading = true;
            this.error = false;
            this.errorMessage = '';

            try {
                this.response = await axios.post('https://5e11-1-244-138-205.ngrok.io:8000/upload', formData,{responseType: 'blob'});
                
                this.imageUrl = URL.createObjectURL(this.response.data);
                // console.log("변환된 이미지 URL:", this.imageUrl);
                this.loading = false;
            } catch (error) {
                console.error("Error during image processing:", error);
                this.error = true;
                this.errorMessage = 'Error processing image. Please try again.';
                this.loading = false;
            }
            this.istranslated = true;

            },
        openGallery(){
            this.gallery = true;
        },
        closeGallery(){
            this.gallery = false;
        }
    }
}
</script>
  
<style scoped>
.background{
    background-image: url('~@/assets/background.png');
    width: 100%;
    height: 100%;
    background-size: cover;
}
.uploadIMG{
    width: 70%;
    height: 45%;
    background-color: aliceblue;
    justify-content: center;
    align-content: center;
    display: flex;
}
.dialog_Card{
    background-image: url('~');
}
.dialog_Card img{
    width: 45%;
    height: auto;
    border-radius: 15px;
}
.example_container{
    display: flex;
}
.text_container{
    background-image:url('~@/assets/AIView/bg.png');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;

}
.button_container{
    width: 70%;
}
.button_container2{
    width: 70%;
    justify-content: space-between;
}
.chooseIMG{
    width: 100%;
    height: 100%;
}
.againChooseImg{
    width: 30%;
    height: 100%;
}
.translateImg{
    width: 65%;
    height: 100%;
}
.preview_img{
    max-height: 90%;
    max-width: 90%;
    border-radius: 10px;
}
.galley_container{
    position:absolute;
    bottom: 0%;
    right: 0%;
}
</style>