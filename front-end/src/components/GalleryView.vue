<<<<<<< HEAD
<template>
    <div class="black-bg" v-if="show">
      <div class="white-bg"> 
        <button class="close" @click="closeP">X</button> 
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
        };
    },
    methods: {
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
=======
<template>
    <div class="black-bg" v-if="show">
      <div class="white-bg"> 
        <button class="close" @click="closeP">X</button> 
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
        };
    },
    methods: {
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
<style>
.white-bg{
    width: 335px;
    height: 627px;
}
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
>>>>>>> 0870ba4ab726cc0f09512eea489028f75d804166
</style>