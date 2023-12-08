<script>
import { getTablesOfBar, getClaimsFromToken, getAuthToken } from '../api/apiClient'

export default {
  data() {
    return {
      tables: []
    }
  },
  async mounted() {
    const { entity_id } = getClaimsFromToken(getAuthToken())
    const response = await getTablesOfBar(entity_id)
    this.tables = await response.json()
  }
}
</script>

<template>
  <main class="container-fluid">
    <h1>MESAS/RESERVAS</h1>
    <h3>Listado de mesas</h3>
    <ul>
      <li v-for="(table, index) in tables" :key="index">
        {{ table.number }} - Seats: {{ table.seats }} - Status: {{ table.status }} - Outdoor: {{ table.outdoor }}
      </li>
    </ul>
  </main>
</template>

<style></style>
