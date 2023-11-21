<template>
    <div class="black-bg" v-if="show">
        <div class="white-bg">  
            <v-carousel v-model="currentSlideIndex" hide-delimiters class="tutorial-img"
            :continuous="false"
            :cycle="false">
                <v-carousel-item
                    v-for="slide in slides"
                    class="tutorial-img-ca"
                    :key="slide.id"
                    :style="{ backgroundImage: 'url(' + require('@/assets/tutorialView/' + slide.image) + ')' }"
                    cover>
                    <button class="closetutorial" @click="closetutorial" v-if="currentSlideIndex < slides.length - 1">skip</button> 
                    <button class="start" @click="closetutorial" v-if="currentSlideIndex === slides.length - 1">
                        <img :src="require('@/assets/start_button_img.png')">
                    </button>
                </v-carousel-item>
            </v-carousel>
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
                {id:1, image : 'info.png', backgroundColor: '#F5F9EF'},
                {id:2, image : 'character.png', backgroundColor: '#F5F9EF'},
                {id:3, image : 'tutorial1.png', backgroundColor: '#E4F0D5'},
                {id:4, image : 'tutorial2.png', backgroundColor: '#E4F0D5'},
                {id:5, image : 'tutorial3.png', backgroundColor: '#E4F0D5'},
                // {id:6, image : require('@/assets/tutorialView/tutorial4.png'), backgroundColor: 'white'},
                {id:7, image : 'last_tu.png', backgroundColor: 'white'},
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
    .white-bg{
        width: 80%;
        position: fixed; 
        overflow-y: auto;
        background-size: contain;
        background-position: center; /* 이미지를 중앙에 정렬합니다 */
        z-index: 1600;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius:5px;
    }

    .tutorial-img-ca {
        background-size: 100% 100%; /* 이미지를 컨테이너 크기에 맞춰 늘림 */
        background-position: center;
        width: 100%;
        height: 100%;
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
        left: 50%; /* 왼쪽에서 50% 위치에 배치 */
        transform: translateX(-50%); /* 버튼의 너비의 절반만큼 왼쪽으로 이동 */
        top: 25%; /* 필요한 경우 상단 위치 조정 */
        max-width: 200px; /* 최대 너비 설정, 필요에 따라 조정 */
        width: auto;
        height: auto;
    }


</style>