<script>
import { getAbleBars } from '../api/apiClient'
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import { LMarker, LMap, LTooltip, LTileLayer, LIcon, LCircle } from "@vue-leaflet/vue-leaflet";

export default {
  components: {
    LIcon,
    LCircle,
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
  },
  data() {
    return {
      zoom: 13,
      markerLatLng: null,
      barList: [],
      ciudad: 'Sevilla',
      ciudadSeleccionada: {},
      ciudades: [
        { nombre: 'Madrid', latitud: 40.4168, longitud: -3.7038 },
        { nombre: 'Barcelona', latitud: 41.3851, longitud: 2.1734 },
        { nombre: 'Valencia', latitud: 39.4699, longitud: -0.3763 },
        { nombre: 'Sevilla', latitud: 37.3886, longitud: -5.9822 },
        { nombre: 'Zaragoza', latitud: 41.6488, longitud: -0.8891 }
      ],
      // Coordenadas iniciales del mapa (Sevilla)
      buscarForm: {
        numeroPersonas: 0,
        exterior: false,
        distancia: 1,
        mapCenter: [37.3886, -5.9822],
      },
    };
  }, watch: {
    ciudad: function (newCiudad) {
      // Actualizar las coordenadas del mapa al cambiar la ciudad seleccionada
      this.ciudadSeleccionada = this.ciudades.find(city => city.nombre === newCiudad);
      this.buscarForm.mapCenter = [this.ciudadSeleccionada.latitud, this.ciudadSeleccionada.longitud];
    },
    'buscarForm.distancia': function () {
      // Actualiza el zoom cuando cambia la distancia
      this.actualizarZoom();
    }
  },
  methods: {
    prueba() {
      console.log("prueba");
    },
    prueba2() {
      console.log("prueba2");
    },
    actualizarZoom() {
      // Ajusta el nivel de zoom en función de la distancia seleccionada
      this.zoom = 14 - this.buscarForm.distancia;
    },
    showCoordinates(event) {
      // Get latitude and longitude from the clicked point
      const lat = event.latlng.lat;
      const lng = event.latlng.lng;
      this.buscarForm.mapCenter = [lat, lng];
      // Display coordinates
      alert(`Latitude: ${lat}, Longitude: ${lng}`);
    },
    async handleSubmit() {
      this.errorMessage = ''
      const resp = await getAbleBars(this.buscarForm)
      const respOk = resp.ok
      const json = await resp.json()
      if (respOk) {
        this.barList = json;
        console.log('Disponemos a mostrar los bares en el mapa', json)
      } else {
        console.log('Hubo un error')
        console.log(json);
        this.errorMessage = json
      }
    }
  }
};
</script>
<template>
  <main class="container-fluid mt-3">
    <div class="row justify-content-center mt-5">
      <div class="col-md-5 border border-3">
        <!-- Formulario -->
        <form @submit.prevent="handleSubmit" class="mb-4">
          <div class="mb-2 mt-3">
            <label for="numeroPersonas" class="form-label">¿Cuántos sois?</label>
            <input type="number" v-model="buscarForm.numeroPersonas" id="numeroPersonas" class="form-control" max="20"
              min="1" required>
          </div>

          <div class="mb-2">
            <label class="form-check-label">¿Quieres la mesa en el exterior?</label>
            <div class="form-check mt-1">
              <input type="checkbox" v-model="buscarForm.exterior" id="ubicacion" class="form-check-input"> Sí, la quiero
              en el
              exterior.
            </div>
          </div>

          <div class="mb-2">
            <label for="distancia" class="form-label">Distancia máxima desplazamiento (km): {{ buscarForm.distancia
            }}</label>
            <input type="range" v-model="buscarForm.distancia" id="distancia" class="form-range" min="1" max="5" step="1">
          </div>

          <div class="mb-2">
            <label for="ciudad" class="form-label">Ciudad sugerencia:</label>
            <select v-model="ciudad" id="ciudad" class="form-select" required>
              <option v-for="city in ciudades" :key="city.nombre" :value="city.nombre">
                {{ city.nombre }}
              </option>
            </select>
          </div>
          <div class="row justify-content-center">
            <div class="col">
              <div id="mapContainer" class="mb-4">
                <l-map ref="map" v-model:zoom="zoom" :center="buscarForm.mapCenter" @click="showCoordinates">
                  <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" layer-type="base"
                    name="OpenStreetMap">
                  </l-tile-layer>
                  <l-circle :lat-lng="buscarForm.mapCenter" :radius="buscarForm.distancia * 1100" :color="red" />
                  <l-marker v-for="(bar, index) in barList" :key="index" :lat-lng="[bar.latitude, bar.longitude]">
                    <l-tooltip :options="{ permanent: true, interactive: true }">
                      {{ bar.name }}
                      <button v-on:click.stop="prueba2">RESERVA!</button>
                    </l-tooltip>
                  </l-marker>
                </l-map>
              </div>
            </div>
          </div>
          <button type="submit" class="btn btn-primary w-100">Mostrar Bares Disponibles</button>
        </form>
      </div>

    </div>
  </main>
</template>
<style scoped>
main {
  font-size: smaller;
}

#mapContainer {
  width: 100%;
  height: 200px;
}
</style>
