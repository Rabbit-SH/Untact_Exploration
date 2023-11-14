<template>
    <div class="black-bg" v-if="show">
      <div class="white-bg"> 
        
        <button class="close" @click="closeP">X</button>
        <input type="file" @change="previewImage" accept="image/*" class="fileButtom">
        <div v-if="imagedata">
            <img :src="imagedata" alt = 'Image Preview' class="image_preview"/>
            <!-- style="max-width: 200px; max-height: 200px;" -->
        </div>
        <div class = 'gallery-container'>
            <div v-for="(photo, index) in photos" :key="index" class="image-container">
                <img :src="photo" :alt="'knps_photo' + index" @click = 'downloadPhoto(photo,index)'>
            </div>
        </div>
      </div>
    </div>
</template>

<script>
import EventBus from '@/EventBus.js';

export default {
    name: 'AppGallery',
    mounted() {
        EventBus.$on('add-photo',this.addPhoto)
    },
    props: {
        show: {
                type: Boolean,
                required: true,
            },
    },
    data(){
        return {
            photos: [],
            selectFile: null,
            imagedata: null
        };
    },
    methods: {
        previewImage(event) {
            this.selectFile = event.target.files[0];
            const reader = new FileReader();
            reader.onload =  (e)=> {
                this.imagedata = e.target.result;
            };
            reader.readAsDataURL(this.selectFile);
        },
        addPhoto(photoUrl) {
            this.photos.push(photoUrl)
        },
        closeP(){
            this.$emit('close');
        },
        downloadPhoto(photo,index) {
            const a = document.createElement('a');
            a.href = photo;
            a.download = `knps_${index}`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        },
    },
    beforeDestroy() {
    EventBus.$off('add-photo', this.photoUrl);
    this.photos.forEach(URL.revokeObjectURL);
    },
};
</script>
<style scoped>
    .gallery-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px; /* Adjust the gap as needed */
    }

    .image-container {
        width: 150px; /* Set fixed width */
        height: 150px; /* Set fixed height */
        overflow: hidden;
        position: relative;
    }

    .image-container img {
        width: 100%;
        height: 100%;
        object-fit: cover; /* This will cover the area without stretching the image */
        cursor: pointer; /* Indicates that the image is clickable */
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
        /* padding: 30px; */
        /* overflow-y: auto; */
        background-image: url('~@/assets/KImage.png');
        background-size: cover;
        background-position: center; /* 이미지를 중앙에 정렬합니다 */
    }
    .image_preview{
        /* max-height: 45%; */
        max-width: 45%;
        position: absolute;
        top: 24%;
        left: 28%;
    }
    .fileButtom{
        position: absolute;
        top: 52%;
        left: 20%;
    }
</style>