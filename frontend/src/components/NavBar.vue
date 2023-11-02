<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <img src="https://placehold.co/64x64" />
    <nav>
        <router-link :to="{ name: 'home'}">Home</router-link> |
        <router-link :to="{ name: 'about'}">About</router-link> |
        <router-link :to="{ name: 'signin'}">SignIn</router-link> |
        <router-link :to="{ name: 'register'}">Register</router-link>
    </nav>
  </header>
</template>

<style scoped>
header {
  background-color: beige;
  display: flex;
  flex-direction: row;
  align-items: center;
}

nav {
    display: flex;
    flex-direction: row;
    flex: 1;
    justify-content: space-evenly;
}
#content {
  flex: 1;
}

footer {
  background-color: beige;
}
</style>
