<script setup>

import { RouterView } from "vue-router"

import Nav from "./components/Nav.vue"
import TodoList from "./views/TodoList.vue";
import CallAPI from "./views/CallAPI.vue";
import GetImage from "./views/GetImage.vue"
import History from "./views/History.vue"
import Monitor from "./views/Monitor.vue"
</script>

<template>
  <div>
    <!-- <History></History> -->
    <!-- <Monitor></Monitor> -->
    <!-- <GetImage></GetImage> -->
    <!-- <CallAPI></CallAPI> -->
    <!-- <TodoList></TodoList> -->
    <!-- <Nav /> -->
    <RouterView/>
  </div>
</template>

<style scoped></style>
