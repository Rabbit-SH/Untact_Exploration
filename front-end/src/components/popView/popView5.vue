<template>
    <div class="black-bg" v-if="show">
      <div class="white-bg"> 
        <button class="close" @click="closeP">X</button> 
        <div class="br" />
        <input type="text" v-model="userAnswer" class="textarea">
        <br>
        <br>
        <div class="button-container">
          <button class="submit" @click="checkAnswer">제출하기</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
      data(){
        return{
            showPopup:false,
            userAnswer:'',
        };
      },
      props: {
          show: {
              type: Boolean,
              required: true,
          },
          result5: {
            type: Boolean
          }
      },
  
      methods: {
        closeP(){
              this.$emit('close');
          },
          //팝업 여는 메소드
        showHint(){
            this.showPopup=true;
          },
          //팝업 닫는 메소드
        closePopup(){
            this.showPopup=false;
          },
          checkAnswer(){
            if(this.userAnswer === '탄소중립'){
                alert('정답입니다!');

                if(this.result5 == false) {
                    this.$emit('answerCorrect')
                }

                // 팝업 닫기
                this.closeP();
            } else{
                alert('오답입니다. 다시 시도해보세요');
            }
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
      width: 90%; height: 90%;
      /* position: relative; */
      border-radius: 8px;
      position: fixed; 
      padding: 20px;
      overflow-y: auto;
      background-image: url('~@/assets/background_pop5.png');
      background-size: contain;
      background-position: center; /* 이미지를 중앙에 정렬합니다 */
  }

  .button-container{
    /* display: flex; */
    position: absolute; /* 고정 위치 */
    /* bottom: 50%; 하단에 위치 */
    left: 0; /* 왼쪽에 위치 */
    bottom: 3%;
    width: 100%; /* 너비를 전체로 설정 */
    background-color: #fff; /* 배경 색상 */
    padding: 10px 20px; /* 패딩을 상하에만 적용 */
    display: flex; /* 버튼들을 가로로 정렬 */
    justify-content: center; /* 가운데 정렬 */
    z-index: 10; /* 다른 요소들 위에 나타나도록 z-index 설정 */
  }
  .submit{
    flex: none;
    width: 80%;
    padding: 10px 10px;
    margin-top: 5px;
    background-color: #0056b3;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    justify-content: start;
    }
  .hint{
    flex: none;
    width: 20%;
    padding: 10px 10px;
    margin-top: 5px;
    background-color: #0056b3;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-left: 10px;
  }
   
  button:hover{
    background-color: #0056b3;
  }
  .close{
  /* position: absolute;
  top: 20px; /* 위로 10px 이동
  right: 20px; 오른쪽으로 10px 이동 */
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
  .br{
    display: inline-block;
    height: 60%;
  }
  .textarea{
    margin: auto;
    width: 90%;
    height: 5%;
    /* margin-top: 60%; */
    /* bottom: 20%; */
    padding: 10px;
    /* justify-content: center; */
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .hint-popup{
    width: 65%; height: 65%;
    position:fixed;
    top: 50%;
    left: 50%;
    border-radius: 4px;
    transform: translate(-50%, -50%); /* 자신의 크기만큼 이동하여 완전히 중앙에 오도록 조정 */
    background: wheat;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2000;
  }
  .close-popup {
    position: absolute;
    top: 10px;
    right: 10px;
    display: flex;
    width: auto;
    padding: 10px 20px;
    margin-top: 5px;
    background-color: #ccc;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-left: auto; /* 왼쪽 마진을 오토로 설정해서 오른쪽으로 밀어냄 */
  }
  </style>