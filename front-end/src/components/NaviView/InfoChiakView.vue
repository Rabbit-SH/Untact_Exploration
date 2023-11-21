<template>
    <div class="black-bg" v-if="show">
        <div class="white-bg">  
            <v-carousel v-model="currentSlideIndex" hide-delimiters class="tutorial-img">
                <v-carousel-item
                    v-for="slide in slides"
                    class="tutorial-img-ca"
                    :key="slide.id"
                    :src="slide.image" cover>
                    <button class="closetutorial text-center" @click="closetutorial">X</button> 
                    
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
                {id:1, image : require('@/assets/infoChiakView/010.png'), backgroundColor: 'white'},
                {id:2, image : require('@/assets/infoChiakView/011.png'), backgroundColor: 'white'},
                {id:3, image : require('@/assets/infoChiakView/012.png'), backgroundColor: 'white'},
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
        /* position: absolute;
        top: 10px;
        right: 10px;
        width: 10px;
        height: 10px;
        display: flex;
        width: auto;
        margin-top: 5px;
        background-color: #ccc;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin-left: auto; */
        width: 20px;
        height: 20px;

        background-color: #ccc;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;

        justify-content: center;
        align-items: center;
        position:absolute;
        top:10px;
        right:10px;
    }

</style>