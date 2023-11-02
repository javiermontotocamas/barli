<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">Barly</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <ul class="navbar-nav me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <router-link :to="{ name: 'home' }" class="nav-link"
                                router-link-active="active">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link :to="{ name: 'about' }" class="nav-link"
                                router-link-active="active">About</router-link>
                        </li>
                    </ul>
                    <div class="d-flex gap-2">
                        <router-link :to="{ name: 'signin' }" class="nav-link"
                                router-link-active="active">
                            <button class="btn btn-success">SignIn</button>
                        </router-link>
                        <router-link :to="{ name: 'register' }" tag="button">
                            <button class="btn btn-info">Register</button>
                        </router-link>
                    </div>
                </div>
            </div>
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
}</style>
