<script>
import { getTablesOfBar, getClaimsFromToken, getAuthToken, getDataOfBar } from '../api/apiClient'

export default {
  data() {
    return {
      barData: [],
      tables: []
    }
  },
  computed: {
    outdoorTables() {
      return this.tables.filter(table => table.outdoor);
    }, indoorTables() {
      return this.tables.filter(table => !table.outdoor);
    },
    totalMesas() {
      // Suma de las mesas interiores y exteriores
      return this.tables.length;
    },
    busyPercentage() {
      // Calcula el porcentaje de mesas "BUSY" en relación con el total
      const busyTables = this.tables.filter(table => table.status === 'BUSY').length;
      return (busyTables / this.totalMesas) * 100 || 0; // Evita división por cero
    },
  },
  async mounted() {
    const { entity_id } = getClaimsFromToken(getAuthToken())
    const response = await getTablesOfBar(entity_id)
    this.tables = await response.json()
    this.getBarData()
  },
  methods: {
    async getBarData() {
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const response = await getDataOfBar(entity_id)
      this.barData = await response.json()
    }
  }
}
</script>

<template>
  <main class="container-fluid mt-5">
    <div class="mt-2 p-4" id="contenedorTitulo">
      <h1 id="titulo" class="text-center p-2">{{ barData.name }} - MIS MESAS</h1>
    </div>
    <div class="row text-center vh-100">
      <h1>Numero de Mesas: {{ totalMesas }}</h1>
      <h2>Grado de Ocupación</h2>
      <div class="progress">
        <div class="progress-bar" :style="{ width: `${busyPercentage}%` }" role="progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
          {{ busyPercentage }}%
        </div>
      </div>
      <div id="inT" class="col-md-6 h-50">
        <h2 class="mt-1">MESAS INTERIOR</h2>
        <ul>
          <li v-for="(table, index) in indoorTables" :key="index">
            {{ table.number }} - Seats: {{ table.seats }} - Status: {{ table.status }} - Outdoor: {{ table.outdoor }}
          </li>
        </ul>
      </div>
      <div id="outT" class="col-md-6 h-50">
        <h2 class="mt-1">MESAS EXTERIOR</h2>
        <ul>
          <li v-for="(table, index) in outdoorTables" :key="index">
            {{ table.number }} - Seats: {{ table.seats }} - Status: {{ table.status }} - Outdoor: {{ table.outdoor }}
          </li>
        </ul>
      </div>

    </div>
  </main>
</template>

<style scoped>
#contenedorTitulo {
  height: 100%;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  max-width: 100%;
  background-image: url(../assets/tableWide.jpg);
}

#contenedorTitulo h1 {
  color: black;
  text-transform: capitalize;
  font-weight: bolder;
  background-color: wheat;
  text-align: center;
  width: 50%;
  margin-left: 25%;
  border: #464646 2px solid;
  border-radius: 10%;
  font-size: xx-large;
}

#inT {
  background-image: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.3)), url(../assets/indoorTable.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}

#outT {
  background-image: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.3)), url(../assets/outdoorTable.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
