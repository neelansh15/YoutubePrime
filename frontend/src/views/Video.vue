<template>

 <div class='container'>
     <h1>My Videos</h1>
      <div v-for = "video in APIData" :key="video.caption"> 
      <h3 class="text-center mt-2 mb-2">{{video.caption}}</h3>
      <video class="embed-responsive embed-responsive-16by9" controls="controls">
        <source :src="video.video.url" type="video/mp4"/>
      </video>
    </div>
 </div>
</template>
 

<script>
// import {getAPI} from "../axios-api"
import axios from "axios"
export default{
name:'video',
data(){
    return {
        APIData: []
    }
},

created () {
    axios.get('http://127.0.0.1:8000/video')
    .then(response=>{
        console.log('video API has recieved data')
        this.APIData=response.data
    })
    .catch(err=>{
        console.log(err)
    });
}
}


</script>

<style>

</style>
