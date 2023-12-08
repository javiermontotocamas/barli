<script>
import { getClaimsFromToken, getAuthToken, getDataOfBar } from '../api/apiClient'
import { RouterLink } from 'vue-router'
import CustomInputSection from '../components/CustomInputSection.vue'

import L from "leaflet";
import "leaflet/dist/leaflet.css";
import { LMarker, LMap, LTooltip, LTileLayer } from "@vue-leaflet/vue-leaflet";

export default {
  data() {
    return {
      nombreBar: "",
      descripcion: "",
      telefono: "",
      direccion: "",
      componenteActivo: null,
      barData: null,
      zoom: 50
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
    cambiarNombre(nuevoNombre) {
      this.nombreBar = nuevoNombre;
    },
    cambiarDescripcion(nuevaDescripcion) {
      this.descripcion = nuevaDescripcion;
    },
    cambiarTelefono(nuevoTelefono) {
      this.telefono = nuevoTelefono;
    },
    cambiarDireccion(nuevaDireccion) {
      this.direccion = nuevaDireccion;
    },
    activarComponente(componente) {
      // Desactivar todos los componentes y activar el componente seleccionado
      if (this.componenteActivo === componente) {
        this.componenteActivo = null;
      } else {
        this.componenteActivo = componente;
      }
    }
  },
  components: {
    CustomInputSection,
    LMarker,
    LMap,
    LTooltip,
    LTileLayer
  }
}
</script>
<template>
  <main class="container-fluid mt-5" v-if="barData">
    <h1 class="text-center mt-2" id="titulo">{{ barData.user.username }}</h1>
    <div class="row">
      <!-- Columna izquierda -->
      <div class="col-md-7">
        <ol id="listadata">
          <li><span>Nombre usuario:</span>{{ barData.user.username }}</li>
          <li><span>Email:</span>{{ barData.user.email }}</li>
          <li><span>Nombre del bar:</span><input type="text" class="form-control" v-model="barData.name" /></li>
          <li><span>Descripción del bar:</span> {{ barData.description }}</li>
          <li><span>Teléfono móvil:</span> {{ barData.phone }}</li>
          <li><span>Dirección del establecimiento:</span> {{ barData.address }}</li>
          <li><span>Latitud:</span> {{ barData.latitude }}</li>
          <li><span>Longitud:</span> {{ barData.longitude }}</li>
        </ol>
      </div>

      <!-- Columna derecha -->
      <div class="col-md-5 bg-secondary">
        <div style="height:100%; width:100%">
          <l-map ref="map" v-model:zoom="zoom" :center="[ barData.latitude, barData.longitude ]">
            <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" layer-type="base"
              name="OpenStreetMap"></l-tile-layer>
            <l-marker :lat-lng="[ barData.latitude, barData.longitude ]">
              <l-tooltip>
              {{ barData.name }} en {{ barData.address }}
              </l-tooltip>
            </l-marker>
          </l-map>
        </div>
        <!--
        <div class="row">
          <div class="col-12 border border-dark">
            <CustomInputSection title="Cambiar nombre del bar" :value="nombreBar" @change="cambiarNombre"
              :active="componenteActivo === 'nombreBar'" @activate="activarComponente('nombreBar')" type="text" />
          </div>
        </div>


        <div class="row">
          <div class="col-12 bg-success">
            <CustomInputSection title="Cambiar descripción" :value="descripcion" @change="cambiarDescripcion"
              :active="componenteActivo === 'descripcion'" @activate="activarComponente('descripcion')" type="textarea" />
          </div>
        </div>

        <div class="row">
          <div class="col-12 bg-danger">
            <CustomInputSection title="Cambiar teléfono" :value="telefono" @change="cambiarTelefono"
              :active="componenteActivo === 'telefono'" @activate="activarComponente('telefono')" type="tel" />
          </div>
        </div>

        <div class="row">
          <div class="col-12 border border-dark">
            <CustomInputSection title="Cambiar dirección" :value="direccion" @change="cambiarDireccion"
              :active="componenteActivo === 'direccion'" @activate="activarComponente('direccion')" type="text" />
          </div>
        </div>
        -->
      </div>
    </div>
    <div class="row mt-3">
      <p id="enlaceMesas"><router-link :to="{ name: 'manageBooks' }" class="nav-link" router-link-active="active">Acceder
          a MIS MESAS</router-link></p>
    </div>
  </main>
</template>
<style scoped>
#titulo {
  padding-top: 5%;
  background-image: url(../assets/cuentaBarimg.jpg);
  height: 100%;
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
  text-align: center;
  border: 1px solid black;
  padding: 1%;
  background-color: ;
}

#enlaceMesas a {
  font-size: 2rem !important;
}
</style>
