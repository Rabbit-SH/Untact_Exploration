<template>
    <div class="black-bg" v-if="show">
        <!-- <div class="white-bg">   -->
            <v-carousel v-model="currentSlideIndex" hide-delimiters class="tutorial-img"
            :continuous="false"
            :cycle="false"
            >
                <v-carousel-item
                v-for="slide in slides"
                class="tutorial-img-ca"
                :key="slide.id"
                :src="slide.image">
                   <button class="closetutorial" @click="closetutorial" v-if="currentSlideIndex < slides.length - 1">skip</button> 
                    <div class="goToMainPage" @click="closetutorial" v-if="currentSlideIndex === slides.length - 1"></div>
                </v-carousel-item>
            </v-carousel>
        </div>
    <!-- </div> -->
</template>


<script scoped>
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
                {id:1, image : require('@/assets/tutorialView/캐릭터 소개 예시.png')},
                {id:2, image : require('@/assets/tutorialView/튜토리얼1.png')},
                {id:3, image : require('@/assets/tutorialView/튜토리얼2.jpg')},
                {id:4, image : require('@/assets/tutorialView/튜토리얼3.png')},
                {id:5, image : require('@/assets/tutorialView/게임시작 페이지 예시.png')}
            ],

            checkedExercise: false,
            checkedEquipment: false,
        }
    },
    methods: {
        closetutorial(){
            this.currentSlideIndex = 0;
            this.$emit('closeTutorial');
        },

    },
}
</script>

<style scoped>
    .black-bg{
        width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.5);
        position: fixed; 
        top: 0;
        left: 0;
        padding: 20px;
        z-index: 1500;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .white-bg {
        width: 80%;
        position: fixed;
        z-index: 1600;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow-y: auto; /* 스크롤을 활성화합니다. */
        border-radius: 5px;
    }

    .tutorial-img-ca {
        width: 100%; /* 이미지가 부모 요소에 꽉 차도록 설정합니다. */
        max-height: 100%; /* 세로 방향으로도 크기가 조절되도록 설정합니다. */
        overflow: auto;
    }
    .tutorial-img{
        width: 80%;
        border-radius: 5px; /* 원하는 border-radius 값으로 설정합니다. */
        overflow-y: auto;
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
    .goToMainPage {
        position: absolute;
        bottom: 15%;
        left: 10%;
        width: 80%;
        height: 10%;
    }
</style>