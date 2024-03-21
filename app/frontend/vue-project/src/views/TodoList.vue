<script setup>
    import { ref, reactive ,watchEffect,onMounted} from 'vue';
    import axios from 'axios';
    const text = ref('');
    const id = ref(0);
    const object_list = ref([]);
    const imageData = ref('');

    const add_obj = () =>{
        const new_object = reactive({
            id: ++id.value,
            name: text.value
        });
        object_list.value.push(new_object);
        text.value = '';
    }
    // const get_image = async () => {
    //     try {
    //         const response = await axios.get('http://192.85.4.173:8008/get-history/2024-03-21');
    //         console.log(response.data.image);
    //         imageData.value = response.data.image;
    //     } catch (error) {
    //         console.error('Error fetching image:', error);
    //     }
    // };
 
</script>

<template>
    <div>
        <h1>
            <text>ToDoLits</text>
        </h1>
    </div>
    <form @submit.prevent="addTodo">
        <input v-model="text" placeholder="input">
        <button @click="add_obj()" >
            <text>Add</text>
        </button>
    </form>
    <div >
        <ul>
            <li v-for="object in object_list" :key="object.id">
                <div class="obj">
                    <input  type="checkbox" v-model="object.done">
                    <span :class="{ done: object.done }"> {{ object.name }}</span>
                </div>
                
            </li>
        </ul>
        <!-- <img :src="`data:image/png;base64,${imageData}`"  alt="Image" /> -->
    </div>
</template>


<style scoped>
    .done {
        text-decoration: line-through;
    }
    .obj {
        display: flex;
        align-items: center;
      }
    .obj input[type="checkbox"] {
        margin-right: 10px;
    }
</style>
