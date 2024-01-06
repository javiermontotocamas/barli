<script>
import { getClaimsFromToken, getAuthToken, getDataOfUser, modDataOfUser } from '../api/apiClient'
import { RouterLink } from 'vue-router'
export default {
  data() {
    return {
      userData: null,
      disableInputs: true,
      errorMessage: ''
    }
  },
  async mounted() {
    this.getUserData()
  },
  methods: {
    async getUserData() {
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const response = await getDataOfUser(entity_id)
      this.userData = await response.json()
    },
    toggleDisableInputs() {
      this.disableInputs = !this.disableInputs;
    },
    async modUser() {
      alert('HOLAA')
      this.errorMessage = ''
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const username = this.userData.user.username
      const resp = await modDataOfUser({ recordData: this.userData, userId: entity_id, username: username })
      const respOk = resp.ok
      const json = await resp.json()
      if (respOk) {
        console.log('Modificados los datos del usuario', json)
        this.userData = json
        this.toggleDisableInputs()
      } else {
        console.log('Hubo un error')
        console.log(json);
        this.errorMessage = json
      }
    }
  }
}
</script>
<template>
  <main class="container-fluid mt-5" v-if="userData">
    <h1 class="text-center mt-2" id="titulo">
      <p>{{ userData.user.username }}</p>
      <button @click="toggleDisableInputs" class="btn btn-secondary">Habilitar Edición</button>
    </h1>
    <div class="row">
      <!-- Columna izquierda -->
      <div class="col-md-12">
        <ol id="listadata">
          <li><span>Nombre usuario:</span>{{ userData.user.username }}<input hidden :disabled="disableInputs" type="text"
              class="form-control" v-model="userData.user.username" required /></li>
          <li><span>Email:</span>{{ userData.user.email }}</li>
          <li><span>Nombre Completo:</span><input :disabled="disableInputs" type="text" class="form-control"
              v-model="userData.fullname" required />
            <div class="row mb-2 text-danger" v-if="errorMessage.fullname">
              {{ errorMessage.fullname.join(", ") }}
            </div>
          </li>
          <li><span>Teléfono móvil:</span><input :disabled="disableInputs" type="phone" class="form-control"
              v-model="userData.phone" required />
            <div class="row mb-2 text-danger" v-if="errorMessage.phone">
              {{ errorMessage.phone.join(", ") }}
            </div>
          </li>
          <li><span>Fecha de nacimiento:</span> <input :disabled="disableInputs" type="date" class="form-control"
              v-model="userData.birthdate" required />
            <div class="row mb-2 text-danger" v-if="errorMessage.birthdate">
              {{ errorMessage.birthdate.join(", ") }}
            </div>
          </li>
        </ol>
      </div>
    </div>
    <div class="row">
      <!-- Div adicional para el botón -->
      <div class="col-md-12 d-flex flex-column align-items-center justify-content-center">
        <button @click="modUser()" class="btn btn-primary" style="width: 100%; height: 100%;">
          <span id="botonActUser"
            style="display:inline-block; font-size: xx-large;white-space: nowrap;">ACTUALIZAR
            DATOS USUARIO</span>
        </button>
      </div>
    </div>
    <div class="row">
      <p id="enlaceMesas"><router-link :to="{ name: 'mainSearch' }" class="nav-link" router-link-active="active">RESERVA
          MESA!</router-link></p>
    </div>
  </main>
</template>
<style scoped>
#titulo {
  padding-top: 5%;
  background-image: url(../assets/cuentaBarimg.jpg);
  height: 100%;
}

#titulo p {
  color: black;
  text-transform: uppercase;
  font-weight: bolder;
  letter-spacing: 1dvi;
  background-color: wheat;
  text-align: center;
  width: 50%;
  margin-left: 25%;
  border: #464646 2px solid;
  border-radius: 10%;
  font-size: xx-large;
}

#listadata {
  counter-reset: li;
  list-style: none, decimal;
  font: 15px 'trebuchet MS', 'lucida sans';
  padding: 0;
  margin-bottom: 4em;
  text-shadow: 0 1px 0 rgba(255, 255, 255, .5);
}

#listadata ol {
  margin: 0 0 0 2em;
}

#listadata {
  list-style-type: none;
  margin: 0;
  margin-left: 1em;
  padding: 0;
  counter-reset: li-counter;
}

#listadata>li {
  position: relative;
  margin-bottom: 1.5em;
  padding: 1.5em;
  background-color: #eaeaea;
}

#listadata>li:before {
  position: absolute;
  top: -0.3em;
  left: -0.5em;
  width: 1.8em;
  height: 1.2em;

  font-size: 2em;
  line-height: 1.2;
  font-weight: bold;
  text-align: center;
  color: #464646;
  background-color: #d0d0d0;

  transform: rotate(-20deg);
  -ms-transform: rotate(-20deg);
  -webkit-transform: rotate(-20deg);
  z-index: 99;
  overflow: hidden;

  content: counter(li-counter);
  counter-increment: li-counter;
}

#listadata span {
  text-transform: uppercase;
  font-weight: bolder;
  background-color: bisque;
  padding: 1%;
  border-radius: 50%;
}


#enlaceMesas {
  margin-top: 1%;
  text-align: center;
  border: 1px solid black;
  padding: 1%;
}

#enlaceMesas a {
  font-size: 2rem !important;
}
</style>

