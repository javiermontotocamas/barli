<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <NavBar />

  <div id="content">
    <RouterView />
  </div>

  <Footer />
</template>

<style scoped>
#content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
