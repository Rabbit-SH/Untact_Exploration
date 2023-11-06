<template>
    <div>
        <div class= "navi">
            <img :src="require('@/assets/logo1.png')" alt="Logo" class="logo">
        </div>
        <div class= "bar"> <!-- 각 버튼 눌러서 새창 뜨게 구현해야함 -->
            <input type="button" value="튜토리얼 다시보기" class="story">
            <input type="button" value="사진첩" class="gallery">
            <input type="button" value="두루마리" class="credit">
            <input type="button" value="탐방코스 선택" class="course" @click="toggleCourseOptions">
            <div class="course-selection" v-show="showCourseOptions">
                <div>
                    <input type="radio" id="course1" value="Course1" v-model="selectedCourse">
                    <label for="course1">코스 1</label>
                </div>
                <div>
                    <input type="radio" id="course2" value="Course2" v-model="selectedCourse">
                    <label for="course2">코스 2</label>
                </div>
                <div>
                    <input type="radio" id="course3" value="Course3" v-model="selectedCourse">
                    <label for="course3">코스 3</label>
                </div>
                <div>
                    <input type="button" id="select" value="선택" @click="finalizeCourseSelection">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            showCourseOptions: false, // 탐방코스 선택 창 표시 여부
            selectedCourse: '', // 선택된 탐방코스
        }
    },
    methods: {
        // toggle(코스 선택) 관련 메서드
        toggleCourseOptions(){
            this.showCourseOptions = !this.showCourseOptions;
        },
        finalizeCourseSelection() {
            if (this.selectedCourse) {
            // 선택된 코스로 로직 처리...
            alert(`선택된 탐방로: ${this.selectedCourse}`);
            }
            this.showCourseOptions = false; // 선택 창 닫기
        },
    }
}
</script>

<style>
    .navi {
        display: flex;
        justify-content: center; /* 수평 가운데 정렬*/
        align-content: center; /* 수직 가운데 정렬 */
        top: 10px;
        left: 30px;
        right: 40px;
        background-color: rgba(255,255,255,0.7); 
        z-index: 1000;
        position: absolute;
        border-radius: 20px;
        height: 50px;
    }
    .logo{
        height: auto;
        width: 190px;
    }
    .bar {
        display: flex;
        justify-content: space-around; /* 버튼들 사이에 동일한 간격을 줍니다 */
        align-items: center;
        position: absolute;
        top: 65px; /* navi 높이에 따라 조정하세요 */
        left: 30px;
        right: 30px;
        z-index: 900; /* navi 바로 아래에 위치하도록 z-index 설정 */
        padding: 5px 10px;
    }
    .bar input[type="button"] {
        flex: 1; /* 버튼들이 균등한 너비를 가지도록 */
        margin: 0 15px; /* 좌우 마진으로 버튼들 사이에 간격을 줍니다 */
        padding: 10px 10px; /* 버튼의 패딩으로 크기를 조정 */
        background-color: #f5f5f5; /* 버튼의 배경색 */
        border: 1px solid #ddd; /* 버튼의 테두리 */
        opacity: 0.8;
        border-radius: 15px; /* 버튼의 둥근 모서리 */
        cursor: pointer; /* 마우스 오버 시 포인터 모양 변경 */
    }
    .course-selection {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 70px;
        left: 30px;
        right: 30px;
        padding: 10px;
        background: #fff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        border-radius: 15px;
        overflow: hidden;
        max-height: 500px;
        transition: max-height 0.3s ease-in-out;
    }

    .course-selection > div {
        margin-bottom: 10px;
    }
</style>