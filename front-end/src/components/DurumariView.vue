<<<<<<< HEAD
<template>
  <div class="black-bg" v-if="show">
    <!-- <div class="white-bg">  -->
        <!-- <button @click="closeP" class="close">X</button> -->
        <div class="mission">
          <button @click="closeP" class="close">X</button>
          <img :src="require('@/assets/background_duru.png')">
          
          <!-- <button @click="closeP" class="close">X</button> -->
          
          <!-- <div class="durumari-overlay"> -->
            <!-- <button @click="closeP" class="close">X</button> -->
            <div class="durumari">
              <div class="durumari-row">
                <div class="d">
                  <img :src="getDurumariImage(1)" :style="{width:'70%', height:'70%'}">
                </div>
                <div class="d">
                  <img :src="getDurumariImage(2)" :style="{width:'70%', height:'70%'}">
                </div>
              </div>
              <div class="durumari-row">
                <div class="d">
                  <img :src="getDurumariImage(3)" :style="{width:'70%', height:'70%'}">
                </div>
                <div class="d">
                  <img :src="getDurumariImage(4)" :style="{width:'70%', height:'70%'}">
                </div>
              </div>
              <div class="durumari-row">
                <div class="d" :style="{width:'50%', height:'30%'}">
                  <img :src="getDurumariImage(5)" :style="{width:'70%', height:'70%'}">
                </div>
              </div>
            </div>
          <!-- </div> -->
      </div>    
    <!-- </div> -->
  </div>
</template>

<script>
import EventBus from '@/EventBus.js'

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
      })
    },
    data(){
      return{
        r1: null,
        r2: null,
        r3: null,
        r4: null,
        r5: null,
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
    /* .white-bg{
      width: 80%; height: 80%; 
      background:white;
      border-radius: 8px;
      padding: 50px;
    } */
    .close-button{
      position: absolute;
      top: 20px; /* 위로 10px 이동 */
      right: 20px; /* 오른쪽으로 10px 이동 */
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
      /* left: 50%; */
      /* transform: translate(-50%, -50%); */
      bottom: 20%;
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
=======
<template>
  <div class="black-bg" v-if="show">
    <div class="white-bg"> 
        <button @click="closeP" class="close">X</button>
        <div class="mission">
          <button @click="closeP" class="close">X</button>
          <img :src="require('@/assets/background_duru.png')">
          
          <button @click="closeP" class="close">X</button>
          
          <div class="durumari-overlay">
            <button @click="closeP" class="close">X</button>
            <div class="durumari">
              <div class="durumari-row">
                <div class="d">
                  <img :src="getDurumariImage(1)" :style="{width:'70%', height:'70%'}">
                </div>
                <div class="d">
                  <img :src="getDurumariImage(2)" :style="{width:'70%', height:'70%'}">
                </div>
              </div>
              <div class="durumari-row">
                <div class="d">
                  <img :src="getDurumariImage(3)" :style="{width:'70%', height:'70%'}">
                </div>
                <div class="d">
                  <img :src="getDurumariImage(4)" :style="{width:'70%', height:'70%'}">
                </div>
              </div>
              <div class="durumari-row">
                <div class="d" :style="{width:'50%', height:'30%'}">
                  <img :src="getDurumariImage(5)" :style="{width:'70%', height:'70%'}">
                </div>
              </div>
            </div>
          </div>
      </div>    
    </div>
  </div>
</template>

<script>
import EventBus from '@/EventBus.js'

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
      })
    },
    data(){
      return{
        r1: null,
        r2: null,
        r3: null,
        r4: null,
        r5: null,
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
    .close-button{
      position: absolute;
      top: 20px; /* 위로 10px 이동 */
      right: 20px; /* 오른쪽으로 10px 이동 */
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
      /* left: 50%; */
      /* transform: translate(-50%, -50%); */
      bottom: 20%;
      z-index: 1;
    }
    .mission img{
      margin: 20px;
      border-radius: 15px;
      display: relative;
    }
    /* .durumari-row{
      display: flex;
    } */
>>>>>>> 0870ba4ab726cc0f09512eea489028f75d804166
</style>