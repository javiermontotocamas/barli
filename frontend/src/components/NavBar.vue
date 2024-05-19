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
      this.$emit('show-signin-modal', true)
    },
    showRegisterModal() {
      this.$emit('show-register-modal', true)
    },
    doLogout() {
      logout()
      this.$emit('user-logout')
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
              <router-link :to="{ name: 'home' }" class="nav-link" router-link-active="active">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'about' }" class="nav-link" router-link-active="active">About</router-link>
            </li>
          </ul>
          <div class="d-flex gap-2" v-if="!username">
            <button class="btn btn-success" @click="showSignInModal()">SignIn</button>
            <button class="btn btn-info" @click="showRegisterModal()">Register</button>
          </div>
          <div class="d-flex gap-2" v-else>
            <ul v-if="role == 'bar'" class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item">
                <router-link :to="{ name: 'ads' }" class="nav-link" router-link-active="active">Gestión
                  Anuncios</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'manageBooks' }" class="nav-link"
                  router-link-active="active">Mesas/Reservas</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'barUser' }" class="nav-link" router-link-active="active">Cuenta
                  Bar</router-link>
              </li>
            </ul>
            <ul v-else-if="role == 'user'" class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item">
                <router-link :to="{ name: 'mainSearch' }" class="nav-link"
                  router-link-active="active">RESERVA</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'user' }" class="nav-link" router-link-active="active">Gestión
                  Cuenta</router-link>
              </li>
            </ul>
            <ul v-else-if="role == 'admin'" class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item">
                <router-link :to="{ name: 'histbooks' }" class="nav-link"
                  router-link-active="active">Historico Reservas</router-link>
              </li>
              <li class="nav-item">
                <router-link :to="{ name: 'all_bars' }" class="nav-link"
                  router-link-active="active">Bares Suscritos</router-link>
              </li>
            </ul>
            <button class="btn btn-outline-primary">{{ username }}</button>
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
  filter: drop-shadow(0 15px 10px rgba(0, 0, 0, 0.4));
}

#content {
  flex: 1;
}
</style>
