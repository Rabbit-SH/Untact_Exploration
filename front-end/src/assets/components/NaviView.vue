<template>
    <div>
        <div class= "navi">
            <img :src="require('@/assets/Navi/logo2.png')" alt="Logo" class="logo">
        </div>
        <div class= "bar">
            <div @click="showTutorialPopup" class="story">
                <img :src="require('@/assets/Navi/tutorial.png')">
            </div>
            <div @click="getGallery" class="gallery">
                <img :src="require('@/assets/Navi/credit.png')">
            </div>
            <div @click="getDurumari" class="credit">
                <img :src="require('@/assets/Navi/gallery.png')">
            </div>
            <div @click="goShelter" class="shelter">
                <img :src="require('@/assets/Navi/shelter.png')">
            </div>
            <div @click="shwoUImg" class="uploadImg">
                <img :src="require('@/assets/Navi/uploadImg.png')">
            </div>
        </div>

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
            showCourseOptions: false, // 탐방코스 선택 창 표시 여부
            selectedCourse: '', // 선택된 탐방코스

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
    .navi {
        display: flex;
        justify-content: center; /* 수평 가운데 정렬*/
        align-content: center; /* 수직 가운데 정렬 */
        top: 10px;
        left: 10px;
        right: 10px;
        background: #ECF3E4;
        z-index: 1000;
        position: absolute;
        border-radius: 11px;
        height: 55px;
    }
    .logo{
        height: 100%;
        width: auto;
    }
    .bar {
        display: flex;
        justify-content: space-around; /* 버튼들 사이에 동일한 간격을 줍니다 */
        align-items: center;
        position: absolute;
        top: 65px; /* navi 높이에 따라 조정하세요 */
        left: 10px;
        right: 10px;
        z-index: 900; /* navi 바로 아래에 위치하도록 z-index 설정 */
        padding-top: 5px;
    }
    .bar div{
        /* width: auto; */
        max-width: 55px;
        margin: 0 auto;
    }
    .bar div img{
        max-width: 100%;
        height: 40px; 
        width: 78px;
        object-fit: contain;
        transition: transform 0.3s ease;
        opacity: 0.7;
        /* height: 60px;
        width: 180px; */
        /* height: 120px; */
    }
    .bar button:hover img{
        transform: scale(1.1);
    }
    /* 반응형 */
    @media (max-width: 768px) {
        .bar div {
            max-width: 30%; /* Smaller max-width for smaller screens */
            margin: 0 3px;
            width: 22%;
        }
    }

    @media (max-width: 480px) {
        .bar div {
            max-width: 30%; /* Even smaller max-width for mobile screens */
            margin: 0 3px;
            width: 22%;
        }
    }
    .course-selection {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 70px;
        left: 30px;
        right: 30px;
        padding: 10px;
        background: #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        border-radius: 15px;
        overflow: hidden;
        max-height: 500px;
        transition: max-height 0.3s ease-in-out;
    }

    .course-selection > div {
        margin-bottom: 10px;
    }
    .google-form-button{
    z-index: 1001;
    position: absolute;
    bottom: 20px;
    right: 10px;
  }
</style>