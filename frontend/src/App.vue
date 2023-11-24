<script>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';
import ModalLayer from './views/ModalLayer.vue';
import SignInView from './views/SignInView.vue';
import RegisterView from './views/RegisterView.vue';


export default {
  components: {
    NavBar,
    Footer,
    ModalLayer,
    SignInView,
    RegisterView,
    RouterView
  },
  data() {
    return {
      username: "",
      role: "",
      showModalSiginOrRegister: false,
      modalMode: "",
      modalTitle: ""
    }
  },
  methods: {
    showSignIn() {
      this.showModalSiginOrRegister = true;
      this.modalMode = "signin";
      this.modalTitle = "INICIO DE SESION";
    },
    showRegister() {
      this.showModalSiginOrRegister = true;
      this.modalMode = "register";
      this.modalTitle = "FORMULARIO DE REGISTRO";
    },
    closeModal() {
      this.showModalSiginOrRegister = false;
      this.modalMode = "";
      this.modalTitle = "";
    },
    userLogged(userLoggedObject) {
      this.username = userLoggedObject.username;
      this.role = userLoggedObject.role;
    },
    userLoggedOut() {
      this.username = '';
    }
  }
}
</script>

<template>
  <NavBar :username="username" :role="role"
    @show-signin-modal="showSignIn"
    @show-register-modal="showRegister"
    @user-logout="userLoggedOut"
  />

  <div id="content">
    <RouterView />
  </div>

  <ModalLayer v-if="showModalSiginOrRegister" @close-modal="closeModal">
    <template v-slot:titulo>
      {{ modalTitle }}
    </template>
    <template v-slot:cuerpo v-if="modalMode == 'signin'">
      <SignInView @user-logged="userLogged" @close-modal="closeModal" />
    </template>
    <template v-slot:cuerpo v-if="modalMode == 'register'">
      <RegisterView />
    </template>
  </ModalLayer>

  <Footer class="sticky-bottom" />
</template>

<style scoped>
/* #app{
  min-height: 100vh;
} */

#content {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
Footer {
  position: sticky;
  bottom: 0;
  width: 100%;
}

</style>
