<template>
    <div>
        <v-app-bar
            app
            color="teal"
            dark
            >
            <div class = "d-flex justify-center flex-grow-1">
                <span class="mr-2">물두꺼비를 따라가보자!</span>
            </div>
        </v-app-bar>
        
        <!-- <v-bottom-navigation
            :value = "value"
            color = "teal"
            grow
            class="navi-button"
            justify="space-around"
            background-color="rgba(255,255,255,0.2)"
        >
            <v-btn style="border-radius:50%;"
            @click="showTutorialPopup" class="story">
                <!-- <span>튜토리얼</span> -->
                <v-icon>mdi-book-open-page-variant-outline</v-icon>
            </v-btn>
            <v-btn style="border-radius:50%;"
            @click="getGallery" class="gallery">
                <!-- <span>사진첩</span> -->
                <v-icon>mdi-image-multiple</v-icon>
            </v-btn>
            <v-btn style="border-radius:50%;"
            @click="getDurumari" class="credit">
                <!-- <span>미션 현황</span> -->
                <v-icon>mdi-text-box-check-outline</v-icon>
            </v-btn>
            <v-btn x-large style="border-radius:50%;" 
            @click="shwoUImg" class="uploadImg">
                <!-- <span>수묵화 변환</span> -->
                <v-icon>mdi-panorama-variant-outline</v-icon>
            </v-btn>

        </v-bottom-navigation> -->
        <button @click="openGoogleForm" class="google-form-button">Google 폼 열기</button>

    </div>
</template>

<script>
// import Durumari from './NaviView/DurumariView.vue';
// import GalleryView from './NaviView/GalleryView.vue';
// import TutorialView from './NaviView/TutorialView.vue';
// import UploadImageView from './/NaviView/UploadImageView2.vue';

export default {
    props:{
        result1:{type:Boolean},
        result2:{type:Boolean},
        result3:{type:Boolean},
        result4:{type:Boolean},
        result5:{type:Boolean},
        result6:{type:Boolean},
    },
    data(){
        return{
            value: '',
            r1: this.result1,
            r2: this.result2,
            r3: this.result3,
            r4: this.result4,
            r5: this.result5,
            r6: this.result6,

            isCredit: false,
            gallery_open: false,
            showtutorial: false,
            uploadIMG: false,
        }
    },
    components:{
    // Durumari,
    // GalleryView,
    // TutorialView,
    // UploadImageView,
},
    methods: {
        // getDurumari(){
        //     this.isCredit = true;
        //     this.gallery_open = false;
        //     this.showtutorial = false;
        //     this.uploadIMG = false;
        // },
        // closeDurumari(){
        //     this.isCredit = false;
        //     this.gallery_open = false;
        //     this.showtutorial = false;
        //     this.uploadIMG = false;
        // },
        // getGallery(){
        //     this.gallery_open = true;
        //     this.showtutorial = false;
        //     this.uploadIMG = false;
        //     this.isCredit = false;
        // },
        // closeGallery(){
        //     this.gallery_open = false;
        //     this.isCredit = false;
        //     this.showtutorial = false;
        //     this.uploadIMG = false;
        // },
        // closeTutorial(){
        //     this.isCredit = false;
        //     this.gallery_open = false;
        //     this.showtutorial = false;
        //     this.uploadIMG = false;
        // },
        // showTutorialPopup(){
        //     this.showtutorial = true;
        //     this.uploadIMG = false;
        //     this.isCredit = false;
        //     this.gallery_open = false;

        // },
        // shwoUImg(){
        //     this.uploadIMG = true;
        //     this.showtutorial = false;
        //     this.isCredit = false;
        //     this.gallery_open = false;
        // },
        // closeUImg(){
        //     this.isCredit = false;
        //     this.gallery_open = false;
        //     this.showtutorial = false;
        //     this.uploadIMG = false;
        // },
        // closeModal(){
        //     this.showModal = false;
        // },
        openGoogleForm(){
            const url = "https://docs.google.com/forms/d/e/1FAIpQLSdBCQgSi7xSaxSddm6OTSFwxXKcOjrNvLxfllJq-o0S7_09OQ/viewform?usp=sf_link";
            const options = "width = 700, height=600, left=200, top=200";
            window.open(url, "_blank", options);
        },

    }
}
</script>

<style>
    .google-form-button{
    z-index: 1001;
    position: absolute;
    bottom: 20px;
    right: 10px;
  }
<<<<<<< Updated upstream
  /* .navi-bar{
    position: flex;
    justify-content: space-between;
    align-items: center;
  } */
=======
  .navi-button{
    z-index: 450;
  }
>>>>>>> Stashed changes
</style>