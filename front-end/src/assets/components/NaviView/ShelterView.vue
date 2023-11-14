<template>
  <div class="black-bg" v-if="show">
    <div class="white-bg">
        <button class="close" @click="closeP">X</button>
        <div class="shelterIMG">
            <img :src="require('@/assets/tutorialView/tutorial4.png')">
        </div>
    </div>
  </div>
</template>

<script>
export default {
    props:{
        show: {
            type:Boolean,
        }
    },
    methods:{
        closeP(){
            this.$emit('close');
        },
    }

}
</script>

<style>
    body{
        margin: 0;
    }
    div{
        box-sizing: border-box;
    }
    .black-bg{
        width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.5);
        position: fixed; padding: 20px;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .white-bg{
        width: 100%; height: 100%;
        position: relative;
        background:white;
        border-radius: 8px;
        padding: 30px;
        overflow-y: auto;
    }
    .shelterIMG img{
        width: 100%; height: 100%;
        background-image: url('~@/assets/tutorialView/tutorial4.png');
        background-size: none;
        background-position: center; /*이미지를 중앙에 정렬합니다*/
    }
    .close{
            display: flex;
            width: 5%;
            padding: 10px 10px;
            margin-top: 5px;
            background-color: #ccc;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-left: auto; /* 왼쪽 마진을 오토로 설정해서 오른쪽으로 밀어냄 */
            justify-content: center;
        
      }
</style>