<template>
  <div class="black-bg" v-if="show">
    <div class="white-bg"> 
        <h4> 팝업창5 만들거임</h4>
        <p> 마커5 누르면 뜨는 팝업창 ! </p>
        <button @click="closeP">닫기</button>
    </div>
  </div>
</template>

<script>
export default {
    props: {
        show: {
            type: Boolean,
            required: true,
        }
    },

    methods: {
        closeP(){
            this.$emit('close');
        }
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
        width: 80%; height: 80%; 
        background:white;
        border-radius: 8px;
        padding: 50px;
    }
</style>