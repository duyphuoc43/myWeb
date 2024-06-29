<template>
    <div>
      <ul>
        <li v-for="post in posts" :key="post.id">{{ post.title }}</li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  const posts = ref([]);
  
  onMounted(async () => {
    try {
      const response = await axios.get(`http://127.0.0.1/:8001`);
      console.log(response)
      posts.value = response.data;
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  });
  </script>