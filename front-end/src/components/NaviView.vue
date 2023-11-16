<template>
    <div>
        <v-app-bar
            app
            color="green"
            dark
            >
            <div class = "d-flex justify-center flex-grow-1">
                <span class="mr-2">물두꺼비를 따라가보자!</span>
            </div>
            </v-app-bar>
        <v-bottom-navigation
            :value = "value"
            color = "teal"
            grow
        >
        <v-btn @click="showTutorialPopup" class="story">
            <span>튜토리얼 다시보기</span>
            <v-icon>mdi-book-open-page-variant-outline</v-icon>
        </v-btn>
        <v-btn @click="getGallery" class="gallery">
            <span>사진첩</span>
            <v-icon>mdi-image-multiple</v-icon>
        </v-btn>
        <v-btn @click="getDurumari" class="credit">
            <span>미션 현황</span>
            <v-icon>mdi-text-box-check-outline</v-icon>
        </v-btn>
        <v-btn @click="shwoUImg" class="uploadImg">
            <span>수묵화 변환</span>
            <v-icon>mdi-panorama-variant-outline</v-icon>
        </v-btn>

        </v-bottom-navigation>
        
        <TutorialView :show="showtutorial" 
            @closeTutorial="closeTutorial"
            @openTutorial="showTutorialPopup" />
        <Durumari :show="isCredit" @close="closeDurumari"/>
        <GalleryView :show="gallery_open" @close="closeGallery" />
        <ShelterView :show="showShelter" @close="closeShelter" />
        <UploadImageView :show="uploadIMG" :class="{'show':uploadIMG}" @close="closeUImg" />

        <button @click="openGoogleForm" class="google-form-button">Google 폼 열기</button>

    </div>
</template>

<script>
import Durumari from './NaviView/DurumariView.vue';
import GalleryView from './NaviView/GalleryView.vue';
import TutorialView from './NaviView/TutorialView.vue';
import ShelterView from './NaviView/ShelterView.vue';
import UploadImageView from './/NaviView/UploadImageView2.vue';

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
            showtutorial: true,
            showShelter: false,
            uploadIMG: false,
        }
    },
    components:{
    Durumari,
    GalleryView,
    TutorialView,
    ShelterView,
    UploadImageView,
},
    methods: {
        // toggle(코스 선택) 관련 메서드
        toggleCourseOptions(){
            this.showCourseOptions = !this.showCourseOptions;
        },
        finalizeCourseSelection() {
            if (this.selectedCourse) {
            // 선택된 코스로 로직 처리...
            alert(`선택된 탐방로: ${this.selectedCourse}`);
            }
            this.showCourseOptions = false; // 선택 창 닫기
        },
        getDurumari(){
            this.isCredit = true;
        },
        closeDurumari(){
            this.isCredit = false;
        },
        getGallery(){
            this.gallery_open = true;
        },
        closeGallery(){
            this.gallery_open = false;
        },
        closeTutorial(){
            this.showtutorial = false;
        },
        showTutorialPopup(){
            this.showtutorial = true;

        },
        goShelter(){
            this.showShelter = true;
        },
        closeShelter(){
            this.showShelter = false;
        },

        shwoUImg(){
        this.uploadIMG = true;
        },
        closeUImg(){
            this.uploadIMG = false;
        },
        closeModal(){
            this.showModal = false;
        },
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
</style>