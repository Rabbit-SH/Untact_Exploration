<template>
  <div class="black-bg" v-if="show">
      <!-- <div class="tutorial" :style="{ background: slide.backgroundColor }"> -->
      <div v-for="(slide, index) in slides" v-show="currentSlideIndex === index" :key="slide.id" class="slideDIV">
          <div class="tutorial" :style="{ background: slide.backgroundColor, 'background-size': 'cover' }">

              <div class="img-container">
                  <img :src="slide.image" alt="Tutorial Image" :style="{ width: '100%', height: '100%' }"/>
              </div>

              <button class="prev" @click="prevSlide" >
                  <img :src="require('@/assets/left.png')">
              </button>
              <button class="next" @click="nextSlide" v-if="currentSlideIndex < slides.length - 1">
                  <img :src="require('@/assets/right.png')">
              </button>
              <button class="close" @click="closeGiftView" v-if="currentSlideIndex === slides.length - 1">
                  <img :src="require('@/assets/giftView/giftButton.png')">
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
              {id:1, image : require('@/assets/giftView/gift1.png'), backgroundColor: '#white'},
              {id:2, image : require('@/assets/giftView/gift2.png'), backgroundColor: '#white'},
              {id:3, image : require('@/assets/giftView/gift3.png'), backgroundColor: '#white'},
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
      closeGiftView(){
          this.currentSlideIndex = 0;
          this.$emit('closeGift');
      },
  },
}
</script>

<style scoped>
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
  .close{
      position: absolute;
      background-color: white;
      color: white;
      border: none;
      /* border-radius: 4px; */
      /* padding: 10px 20px; */
      /* bottom: 20%; */
      bottom: 10%;
      width: 100%;
      height:auto;
      /* pointer-events: none; */
  }

  .slideDIV{
      justify-content: center;
      text-align: center;
      align-items: center;
  }
  .close img{
    width: 220px;
    height: 70px;
  }

</style>