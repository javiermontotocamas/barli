<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    Barli
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </header>

  <div id="content">
    <RouterView />
  </div>

  <footer>Pie de pagina</footer>
</template>

<style scoped>
header {
  background-color: beige;
}

#content {
  flex: 1;
}

footer {
  background-color: beige;
}
</style>
