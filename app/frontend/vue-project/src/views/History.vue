<script setup>
    import { ref, reactive ,watchEffect,onMounted} from 'vue';
    import axios from 'axios';

    const historyList = ref();
    const date =ref('');
    const getHistory = async () => {
        try{
            const response = await axios.post('http://192.85.4.173:8008/get-history', { date: date.value });
            console.log(response.data);
            historyList.value = response.data;
        }
        catch (error) {
        console.error('Error fetching image:', error);
        }
        date.value = '';
    }
</script>
    
<template>
    <div>
        <a href="/">Back Monitor</a>
    </div>
    <div>
        
        <h1>History</h1>
        
    </div>
    <form @submit.prevent="addTodo">
        <input v-model="date" placeholder="2001-03-20">
        <button @click="getHistory()">Load</button>
        {{ date }}
    </form>
    <div>
        <ul>
            <il v-for="history in historyList" :key="history.date"  class="history-item">
                <div>
                    <label>{{history.date}}</label>
                    <div>
                        <label>{{history.location}}</label>
                    </div>
                    
                    <div>
                        <img :src="`data:image/png;base64,${history.image}`"  alt="Image" class="history-image" />
                    </div>
                </div>
            </il>
        </ul>
    </div>
</template>


<style scoped>
    .history-item {
        margin-bottom: 20px;
    }
    
    .history-image {
        max-width: 400px; 
        max-height: 200px; 
    }
</style>
