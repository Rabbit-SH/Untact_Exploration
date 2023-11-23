<template>
  <div class="background" justify="center" align="center">
    <h1 class="pt-10">AI 화가</h1>
    <div class="uploadIMG text-center mt-16"></div>

    <div class="button_container">
        <v-btn></v-btn>
    </div> 






    <v-dialog v-model="dialog" max-width="500">
      <v-card class="text-center dialog_Card">
        <!-- <v-card-title class="text-h5 grey lighten-2 text-center">
          Privacy Policy
        </v-card-title> -->
        <v-card-text class="pa-5 pt-10">
            <div class="text_container">
                <strong>한국화</strong>는 한국의 전통 그림이에요!<br>
                붓과 먹을 사용해서<br>부드러운 선으로 그린답니다~<br><br>
                여기에 찍은 사진을 올려주면 <br>AI 화가가 사진을 한국화로 그려줄거에요!!
            </div>
          <br>
          <br>
          <br>
          <div class="example_container d-flex justify-center align-center">
            <img :src="require('@/assets/AIView/origin.jpg')">
            <v-icon>mdi mdi-arrow-right-thick</v-icon>
            <img :src="require('@/assets/AIView/koreaPaint.png')">
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="orange"
            text
            @click="dialog = false"
          >
            확인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
    data(){
        return{
            dialog: true,
        }
    }
}
</script>

<style scoped>
.background{
    background-image: url('~@/assets/background.png');
    width: 100%;
    height: 100%;
    background-size: cover;
}
.uploadIMG{
    width: 70%;
    height: 45%;
    background-color: aliceblue;
}
.dialog_Card{
    background-image: url('~');
}
.dialog_Card img{
    width: 45%;
    height: auto;
    border-radius: 15px;
}
.example_container{
    display: flex;
}
.text_container{
    background-image:url('~@/assets/AIView/bg.png');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;

}
</style>