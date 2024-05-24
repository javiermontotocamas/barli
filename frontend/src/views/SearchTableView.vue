<script>
import { getAbleBars, getAdsOfBar, getClaimsFromToken, getAuthToken, pendTableBar, getTableforBook, postBook, checkUserBook } from '../api/apiClient'
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import { LMarker, LMap, LTooltip, LTileLayer, LIcon, LCircle } from "@vue-leaflet/vue-leaflet";
import ModalLayer from '../views/ModalLayer.vue';

export default {
  components: {
    LIcon,
    LCircle,
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
    ModalLayer
  },
  data() {
    return {
      respCheckUserBookjson: [],
      showCurrentBook: false,
      barSeleccionado: null,
      showModalWindow: false,
      zoom: 13,
      markerLatLng: null,
      ads: [],
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
  }, async mounted() {
    this.checkbooks()
  }
  , watch: {
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
    closeModalWindow() {
      this.showModalWindow = false;
      this.barSeleccionado = null;
    },
    async openModalWindow(bar) {
      this.showModalWindow = true;
      this.barSeleccionado = bar;
      const response = await getAdsOfBar(this.barSeleccionado.id)
      this.ads = await response.json()
      if (this.ads.length > 2) {
        const randomIndices = this.getRandomIndices(2, this.ads.length);
        this.ads = [this.ads[randomIndices[0]], this.ads[randomIndices[1]]];
      }
    },
    async checkbooks() {
      //COMPROBAMOS SI USUARIO TIENE RESERVA
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const respCheckUserBook = await checkUserBook(entity_id)
      this.respCheckUserBookjson = await respCheckUserBook.json()
      if (this.respCheckUserBookjson.length>0) {
        console.log(this.respCheckUserBookjson)
        this.showCurrentBook = true
      } else {
      }
    }
    ,
    async bookTable() {
      //PRIMERO GET, DESPUES PATCH Y LUEGO PUT
      const { entity_id } = getClaimsFromToken(getAuthToken())
      let tableId = null;
      //GET
      const respGetTable = await getTableforBook({ barId: this.barSeleccionado.id, datosMesa: this.buscarForm })
      const respGetTableOk = respGetTable.ok
      if (respGetTableOk) {
        const respGetTablejson = await respGetTable.json();
        tableId = respGetTablejson[0].id
        //PATCH
        const responsePatchTable = await pendTableBar({ barId: this.barSeleccionado.id, tableId: tableId })
        const respPatchTableOk = responsePatchTable.ok
        if (respPatchTableOk) {
          //PUT
          const respPostBook = await postBook({ userId: entity_id, tableId: tableId })
          const respPostBookOk = respPostBook.ok
          const jsonPostBook = await respPostBook.json()
          if (respPostBookOk) {
            location.reload()
            console.log(jsonPostBook)
            this.checkbooks()
          } else {
            console.log('Hubo un error')
            console.log(jsonPostBook)
          }
        }
        else {
          alert('No se ha podido reservar la mesa')
        }
      }
      else {
        alert('NO HAY MESAS DISPONIBLES')
      }

    },
    getRandomIndices(num, max) {
      const indices = [];
      while (indices.length < num) {
        const randomIndex = Math.floor(Math.random() * max);
        if (!indices.includes(randomIndex)) {
          indices.push(randomIndex);
        }
      }
      return indices;
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
      } else {
        console.log('Hubo un error')
        console.log(json);
        this.errorMessage = json
      }
    }, formatDateTime(dateTime) {
      const date = new Date(dateTime);

      // Agrega 20 minutos
      date.setMinutes(date.getMinutes() + 20);

      // Obtiene los componentes de la hora
      const hours = date.getHours();
      const minutes = date.getMinutes();

      // Formatea en un string "HH:MM"
      const formattedTime = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;

      return formattedTime;
    },
  }
};
</script>
<template>
  <main class="container-fluid mt-3">
    <ModalLayer v-if="showModalWindow" @close-modal="closeModalWindow">
      <template v-slot:titulo>
        <p class="h3">{{ barSeleccionado.name }}</p>
      </template>
      <template v-slot:cuerpo>
        <div class="row">
          <div v-if="ads.length > 0" class="col-md-3">
            <div>
              <p>PROMOCION</p>
              <hr>
              <p>{{ ads[0].product_name }}</p>
              <p>Rebaja: {{ ads[0].reduction }}%</p>
            </div>
          </div>
          <div :class="ads.length > 0 ? 'col-md-6' : 'col-md-12'">
            <div class="border p-3 mb-4 mt-4">{{ barSeleccionado.description }}</div>
          </div>
          <div v-if="ads.length >= 1" class="col-md-3">
            <div v-if="ads.length === 1" class="col-md-3">
              <div>
                <p>PROMOCION</p>
                <hr>
                <p>{{ ads[0].product_name }}</p>
                <p>Rebaja: {{ ads[0].reduction }}%</p>
              </div>
            </div>
            <!-- Si hay dos, mostrar solo el segundo -->
            <div v-if="ads.length === 2">
              <div v-for="(ad, index) in ads.slice(1)" :key="index">
                <p>PROMOCION</p>
                <hr>
                <p>{{ ad.product_name }}</p>
                <p>Rebaja: {{ ad.reduction }}%</p>
              </div>
            </div>
            <!-- Si hay más de dos anuncios, mostrar uno aleatorio diferente al primero -->
            <div v-else>
              <div v-for="(ad, index) in ads.slice(1)" :key="index">
                <p>PROMOCION</p>
                <hr>
                <p>{{ ad.product_name }}</p>
                <p>Rebaja: {{ ad.reduction }}%</p>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <hr>
          <h5>{{ barSeleccionado.address }}</h5>
          <h6>Telefono de contacto: {{ barSeleccionado.phone }}</h6>
        </div>
      </template>
      <template v-slot:pie>
        <div class="col-12"><button v-on:click="bookTable(this.bar)" class="w-100">Hacer reserva</button></div>
      </template>
    </ModalLayer>

    <div v-if="!showCurrentBook" class="row justify-content-center mt-5">
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
                  <l-circle :lat-lng="buscarForm.mapCenter" :radius="buscarForm.distancia * 1350" />
                  <l-marker v-for="(bar, index) in barList" :key="index" :lat-lng="[bar.latitude, bar.longitude]">
                    <l-tooltip :options="{ permanent: true, interactive: true }">
                      {{ bar.name }}
                      <button v-on:click.stop="openModalWindow(bar)">RESERVA!</button>
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
    <!-- Div para mostrar el contenido del json si showCurrentBook es true -->
    <div v-else class="row justify-content-center mt-5">
      <h1>¡Ya tienes una reserva!</h1>
      <table class="reservation-table">
        <tr>
          <td>Bar:</td>
          <td>{{ respCheckUserBookjson[0]['bar']['name'] }}</td>
        </tr>
        <tr>
          <td>Dirección:</td>
          <td>{{ respCheckUserBookjson[0]['bar']['address'] }}</td>
        </tr>
        <tr>
          <td>Teléfono:</td>
          <td>{{ respCheckUserBookjson[0]['bar']['phone'] }}</td>
        </tr>
        <tr>
          <td>Hora a la que el bar es libre de anular la reserva:</td>
          <td>{{ formatDateTime(respCheckUserBookjson[0]['initial_datetime']) }}</td>
        </tr>
      </table>
      <h2>¡Recuerda que si no llegas en 20 minutos, el bar puede anular la reserva!</h2>

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

.reservation-container {
  text-align: center;
  margin: 50px auto;
  padding: 20px;
  border: 2px solid #ccc;
  border-radius: 10px;
}

.reservation-table {
  margin: 20px auto;
  border-collapse: collapse;
}

.reservation-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
</style>
