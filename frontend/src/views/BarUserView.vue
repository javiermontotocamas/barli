<script>
import { getClaimsFromToken, getAuthToken, getDataOfBar, modDataOfBar } from '../api/apiClient'
import { RouterLink } from 'vue-router'
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import { LMarker, LMap, LTooltip, LTileLayer } from "@vue-leaflet/vue-leaflet";

export default {
  data() {
    return {
      barData: null,
      disableInputs: true,
      zoom: 50,
      errorMessage: ''
    }
  },
  async mounted() {
    this.getBarData()
  },
  methods: {
    async getBarData() {
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const response = await getDataOfBar(entity_id)
      this.barData = await response.json()
    },
    toggleDisableInputs() {
      this.disableInputs = !this.disableInputs;
    },
    async modBar() {
      this.errorMessage = ''
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const username = this.barData.user.username
      const resp = await modDataOfBar({ recordData: this.barData, barId: entity_id, username: username })
      const respOk = resp.ok
      const json = await resp.json()
      if (respOk) {
        console.log('Modificados los datos del bar', json)
        this.barData = json
        this.toggleDisableInputs()
      } else {
        console.log('Hubo un error')
        console.log(json);
        this.errorMessage = json
      }
    }
  },
  components: {
    LMarker,
    LMap,
    LTooltip,
    LTileLayer
  }
}
</script>
<template>
  <main class="container-fluid mt-5" v-if="barData">
    <h1 class="text-center mt-2" id="titulo">
      <p>{{ barData.user.username }}</p>
      <button @click="toggleDisableInputs" class="btn btn-secondary">Habilitar Edición</button>
    </h1>
    <div class="row" style="height: 100vh; margin-bottom: 13%;">
      <!-- Columna izquierda -->
      <div class="col-md-6">
        <ol id="listadata">
          <li><span>Nombre usuario:</span>{{ barData.user.username }}<input hidden :disabled="disableInputs" type="text"
              class="form-control" v-model="barData.user.username" required /></li>
          <li><span>Email:</span>{{ barData.user.email }}</li>
          <li><span>Nombre del bar:</span><input :disabled="disableInputs" type="text" class="form-control"
              v-model="barData.name" required />
            <div class="row mb-2 text-danger" v-if="errorMessage.name">
              {{ errorMessage.name.join(", ") }}
            </div>
          </li>
          <li><span>Descripción del bar:</span> <textarea :disabled="disableInputs" style="width: 100%;" maxlength="150"
              rows="4" v-model="barData.description"></textarea>
            <div class="row mb-2 text-danger" v-if="errorMessage.description">
              {{ errorMessage.description.join(", ") }}
            </div>
          </li>
          <li><span>Teléfono móvil:</span><input :disabled="disableInputs" type="phone" class="form-control"
              v-model="barData.phone" required />
            <div class="row mb-2 text-danger" v-if="errorMessage.phone">
              {{ errorMessage.phone.join(", ") }}
            </div>
          </li>
          <li><span>Dirección del establecimiento:</span> <input :disabled="disableInputs" type="text"
              class="form-control" v-model="barData.address" required />
            <div class="row mb-2 text-danger" v-if="errorMessage.address">
              {{ errorMessage.address.join(", ") }}
            </div>
          </li>
          <li><span>Latitud:</span> <input :disabled="disableInputs" type="text" class="form-control"
              v-model="barData.latitude" required />
            <div class="row mb-2 text-danger" v-if="errorMessage.latitude">
              {{ errorMessage.latitude.join(", ") }}
            </div>
          </li>
          <li><span>Longitud:</span> <input :disabled="disableInputs" type="text" class="form-control"
              v-model="barData.longitude" required />
            <div class="row mb-2 text-danger" v-if="errorMessage.longitude">
              {{ errorMessage.longitude.join(", ") }}
            </div>
          </li>
        </ol>
      </div>
      <!-- Div adicional para el botón -->
      <div class="col-md-1 d-flex flex-column align-items-center justify-content-center">
        <button @click="modBar()" class="btn btn-primary" style="width: 100%; height: 100%;">
          <span id="botonActBar"
            style="display:inline-block; font-size: xx-large; writing-mode: vertical-rl;white-space: nowrap;">ACTUALIZAR
            DATOS BAR</span>
        </button>
      </div>
      <!-- Columna derecha -->
      <div class="col-md-5">
        <div id="mapContainer">
          <l-map ref="map" v-model:zoom="zoom" :center="[barData.latitude, barData.longitude]">
            <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" layer-type="base"
              name="OpenStreetMap"></l-tile-layer>
            <l-marker :lat-lng="[barData.latitude, barData.longitude]">
              <l-tooltip>
                {{ barData.name }} en {{ barData.address }}
              </l-tooltip>
            </l-marker>
          </l-map>
        </div>
      </div>
    </div>
    <div class="row">
      <p id="enlaceMesas"><router-link :to="{ name: 'manageBooks' }" class="nav-link" router-link-active="active">Acceder
          a MIS MESAS</router-link></p>
    </div>
    <div class="row">
      <p id="enlaceAds"><router-link :to="{ name: 'ads' }" class="nav-link" router-link-active="active">Acceder
          a MIS PROMOCIONES</router-link></p>
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

#mapContainer {
  width: 90%;
  height: 90%;
}

#enlaceMesas {
  margin-top: 7%;
  text-align: center;
  border: 1px solid black;
  padding: 1%;
}

#enlaceMesas a {
  font-size: 2rem !important;
}

#enlaceAds {
  text-align: center;
  border: 1px solid black;
  padding: 1%;
}

#enlaceAds a {
  font-size: 2rem !important;
}
</style>
