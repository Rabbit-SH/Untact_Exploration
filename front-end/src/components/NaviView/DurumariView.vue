<template>
  <div class="black-bg" v-if="show">
    <div class="white-bg"> 
        <button @click="closeP" class="close">X</button>
        <div class="mission">
          <!-- <button @click="closeP" class="close">X</button> -->
          <!-- <img :src="require('@/assets/background_duru.png')"> -->
          
          
          <!-- <div class="durumari-overlay"> -->
            <div class="durumari">
              <div class="durumari-row">
                <div class="d">
                  <img :src="getDurumariImage(1)" :style="{width:'50%', height:'50%'}">
                </div>
                <div class="d">
                  <img :src="getDurumariImage(2)" :style="{width:'50%', height:'50%'}">
                </div>
              </div>
              <div class="durumari-row">
                <div class="d">
                  <img :src="getDurumariImage(3)" :style="{width:'50%', height:'50%'}">
                </div>
                <div class="d">
                  <img :src="getDurumariImage(4)" :style="{width:'50%', height:'50%'}">
                </div>
              </div>
              <div class="durumari-row">
                <div class="d">
                  <img :src="getDurumariImage(5)" :style="{width:'50%', height:'50%'}">
                </div>
                <div class="d">
                  <img :src="getDurumariImage(6)" :style="{width:'50%', height:'50%'}">
                </div>
              </div>
              <!-- <div class="durumari-row">
                <div class="d">
                  <img :src="getDurumariImage(5)" :style="{width:'40%', height:'45%'}">
                </div>
              </div> -->
            </div>
          <!-- </div> -->
      </div>    
    </div>
  </div>
</template>

<script>
import {EventBus} from '@/assets/EventBus.js'

export default {
    props: {
        show: {
            type: Boolean,
            required: true,
        },
    },

    methods: {
      closeP(){
          this.$emit('close');
      },
      getDurumariImage(index){
        switch (index) {
          case 1:
          return this.r1 ? require('@/assets/reward_a.png') : require('@/assets/reward_b.png');
          case 2:
          return this.r2 ? require('@/assets/reward_a.png') : require('@/assets/reward_b.png');
          case 3:
          return this.r3 ? require('@/assets/reward_a.png') : require('@/assets/reward_b.png');
          case 4:
          return this.r4 ? require('@/assets/reward_a.png') : require('@/assets/reward_b.png');
          case 5:
          return this.r5 ? require('@/assets/reward_a.png') : require('@/assets/reward_b.png');
          case 6:
          return this.r6 ? require('@/assets/reward_a.png') : require('@/assets/reward_b.png');
        }
      },
    },
    created(){
      EventBus.$on('send-results-to-durumari', (res) => {
        this.r1 = res.r1;
        this.r2 = res.r2;
        this.r3 = res.r3;
        this.r4 = res.r4;
        this.r5 = res.r5;
        this.r6 = res.r6;
      })
    },
    data(){
      return{
        r1: null,
        r2: null,
        r3: null,
        r4: null,
        r5: null,
        r6: null,
      }
    }
}
</script>

<style scoped>
    body{
      margin: 0;
    }
    div{
      box-sizing: border-box;
    }
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
      width: 100%; height: 100%;
      position: relative;
      border-radius: 8px;
      padding: 30px;
      overflow-y: auto;
      background-image: url('~@/assets/background.png');
      background-size: cover;
      background-position: center; /* 이미지를 중앙에 정렬합니다 */
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
    .d{
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .durumari-overlay {
      position: relative;
    }
    .durumari {
      position: absolute;
      /* top: -700px; */
      /* top: 50%; */
      left: -10px;
      /* transform: translate(-50%, -50%); */
      bottom: 11%;
      z-index: 1;
    }
    .mission img{
      margin: 20px;
      border-radius: 15px;
      display: relative;
    }
    .durumari-row{
      display: flex;
    }
</style>