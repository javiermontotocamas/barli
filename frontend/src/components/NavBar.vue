<script>
import { RouterLink } from 'vue-router'
import { logout } from '../api/apiClient'

export default {
    emits: ['show-signin-modal', 'show-register-modal', 'user-logout'],
    props: {
        username: String,
        role: {
            validator(value) {
                return ['user', 'bar'].includes(value)
            }
        }
    },
    methods: {
        showSignInModal() {
            this.$emit('show-signin-modal', true);
        },
        showRegisterModal() {
            this.$emit('show-register-modal', true);
        },
        doLogout() {
            logout();
            this.$emit('user-logout');
        }
    }
}
</script>

<template>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">Barli</a>
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
                    <div class="d-flex gap-2" v-if="!username">
                        <button class="btn btn-success" @click="showSignInModal()">SignIn</button>
                        <button class="btn btn-info" @click="showRegisterModal()">Register</button>
                    </div>
                    <div class="d-flex gap-2" v-else>
                        <button class="btn btn-outline-primary">{{ username }} - {{ role }}</button>
                        <button class="btn btn-outline-danger" @click="doLogout()">Logout</button>
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
    filter: drop-shadow(0 15px 10px rgba(0,0,0,.4));
}

#content {
    flex: 1;
}
</style>
