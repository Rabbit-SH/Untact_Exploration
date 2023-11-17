<template>
    <div class="black-bg" v-if="show">
        <!-- <div class="tutorial" :style="{ background: slide.backgroundColor }"> -->
        <div v-for="(slide, index) in slides" v-show="currentSlideIndex === index" :key="slide.id" class="slideDIV">
            <div class="tutorial" :style="{ background: slide.backgroundColor }">

                <div class="img-container">
                    <img :src="slide.image" alt="Tutorial Image" :style="{ width: '100%', height: '100%' }"/>
                </div>

                <button class="prev" @click="prevSlide" >
                    <img :src="require('@/assets/left.png')">
                </button>
                <button class="next" @click="nextSlide" v-if="currentSlideIndex < slides.length - 1">
                    <img :src="require('@/assets/right.png')">
                </button>
                <button class="closetutorial" @click="closetutorial" v-if="currentSlideIndex < slides.length - 1">skip</button>
                <button class="start" @click="closetutorial" v-if="currentSlideIndex === slides.length - 1">
                    <img :src="require('@/assets/start_button_img.png')">
                </button>

            </div>
        </div>
    </div>
</template>

<script>
export default {
    props:{
        show: {
                type: Boolean,
                required: true,
            },

    },
    data(){
        return{
            currentSlideIndex: 0,

            slides: [
                {id:1, image : require('@/assets/info.png'), backgroundColor: '#F5F9EF'},
                {id:2, image : require('@/assets/character.png'), backgroundColor: '#F5F9EF'},
                {id:3, image : require('@/assets/tutorial1.png'), backgroundColor: '#E4F0D5'},
                {id:4, image : require('@/assets/tutorial2.png'), backgroundColor: '#E4F0D5'},
                {id:5, image : require('@/assets/tutorial3.png'), backgroundColor: '#E4F0D5'},
                {id:6, image : require('@/assets/tutorial4.png'), backgroundColor: 'white'},
                {id:7, image : require('@/assets/last_tu.png'), backgroundColor: 'white'},
            ],

            checkedExercise: false,
            checkedEquipment: false,
        }
    },
    methods: {
        nextSlide() {
            if (this.currentSlideIndex < this.slides.length - 1) {
                this.currentSlideIndex++;
            }
        },
        prevSlide() {
            if(this.currentSlideIndex > 0){
                this.currentSlideIndex--;
            }
        },
        closetutorial(){
            this.currentSlideIndex = 0;
            this.$emit('closeTutorial');
        },
        showTutorialPopup(){
            this.currentSlideIndex = 0;
            this.$emit('openTutorial');
        },

    },
}
</script>

<style>
    .black-bg{
        width: 100%; height: 100%;
        background: rgba(255, 255, 255, 0.1);
        position: fixed; padding: 20px;
        z-index: 10000;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .tutorial{
        position: relative;
        width: 100%;
        height: 100%;
        z-index: 1000;
        text-align: center;
        border-radius: 8px;
        justify-content: center;
        padding: 10px;
        display: flex;
        align-items: center;
        overflow: auto;
        flex-direction: column;
    }
    .prev{
        position: absolute;
        left: 10px;
        bottom: 50%;
        background-color: #ccc;
        color: white;
        border-radius: 4px;
        border: none;
        padding: 5px 10px;
    }
    .next{
        position: absolute;
        right: 10px;
        bottom: 50%;
        background-color: #ccc;
        color: white;
        border-radius: 4px;
        border: none;
        padding: 5px 10px;
    }
    .closetutorial{
        position: absolute;
        top: 15px;
        right: 25px;
        display: flex;
        width: auto;
        padding: 5px 10px;
        margin-top: 5px;
        background-color: #ccc;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-left: auto; /* 왼쪽 마진을 오토로 설정해서 오른쪽으로 밀어냄 */
    }
    .start{
        position: absolute;
        background-color: white;
        color: white;
        border: none;
        /* border-radius: 4px; */
        /* padding: 10px 20px; */
        /* bottom: 20%; */
        top: 25%;
        width: 100%;
        height:auto;
        /* pointer-events: none; */
    }
     /* 이미지 크기 조정을 위한 CSS */
     .image-container {
        width: 100%; /* div 폭에 맞게 조정 */
        max-height: 60vh; /* 최대 높이 설정 (60% 화면 높이) */
        overflow: hidden; /* 넘치는 부분 숨김 */
        display: block;
        align-items: center;
        justify-content: center;
        /* z-index: 2000; */
        object-fit: contain;

    }

    .image-container img {
        width: auto;
        height: 100%;
        max-width: 100%; /* 이미지 폭 최대 크기 설정 */
        max-height: 100%; /* 이미지 높이 최대 크기 설정 */
        object-fit: fill;

    }
    .slideDIV{
        justify-content: center;
        text-align: center;
        align-items: center;
    }

</style>