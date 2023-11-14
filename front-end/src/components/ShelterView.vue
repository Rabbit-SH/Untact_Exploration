<template>
  <div class="black-bg" v-if="show">
    <div class="white-bg">
        <button class="close" @click="closeP">X</button>

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
        /* padding-bottom: 70px; */
    }
    button:hover{
        background-color: #0056b3;
    
    }
    .close-button{
        position: absolute;
        top: 20px; /* 위로 10px 이동 */
        right: 20px; /* 오른쪽으로 10px 이동 */
    }
</style>