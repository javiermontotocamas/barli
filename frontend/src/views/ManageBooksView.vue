<script>
import { getTablesOfBar, getClaimsFromToken, getAuthToken, getDataOfBar, createTableOfBar, deleteTableOfBar, updateTableStatus } from '../api/apiClient'
import { FontAwesomeIcon } from '@/plugins/fontawesome'

export default {
  data() {
    return {
      barData: [],
      tables: [],
      errorMessage: '',
      errorDelMessage: '',
      numerosMesas: [],
      selectedTableId: null,
      newTable: {
        number: '',
        status: 'FREE',
        seats: '',
        outdoor: false,
      }
    }
  },
  computed: {
    outdoorTables() {
      return this.tables.filter(table => table.outdoor);
    }, indoorTables() {
      return this.tables.filter(table => !table.outdoor);
    }, freeTables() {
      return this.tables.filter(table => table.status === 'FREE');
    },
    totalMesas() {
      // Suma de las mesas interiores y exteriores
      return this.tables.length;
    },
    busyPercentage() {
      // Calcula el porcentaje de mesas "BUSY" en relación con el total
      const busyTables = this.tables.filter(table => table.status === 'BUSY').length;
      return Math.floor((busyTables / this.totalMesas) * 100) || 0; // Evita división por cero y limita a un numero entero
    },
  },
  async mounted() {
    const { entity_id } = getClaimsFromToken(getAuthToken())
    const response = await getTablesOfBar(entity_id)
    this.tables = await response.json()
    this.numerosMesas = this.tables.map(table => table.number);
    this.getBarData()
  },
  methods: {
    async getBarData() {
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const response = await getDataOfBar(entity_id)
      this.barData = await response.json()
    },
    async addTable() {
      this.errorMessage = ''
      const { entity_id } = getClaimsFromToken(getAuthToken())
      // Encontrar el número más bajo disponible
      let nuevoNumeroMesa = 1;
      while (this.numerosMesas.includes(nuevoNumeroMesa)) {
        nuevoNumeroMesa++;
      }
      this.newTable.number = nuevoNumeroMesa;
      const resp = await createTableOfBar({ recordData: this.newTable, barId: entity_id })
      const respOk = resp.ok
      const json = await resp.json()
      if (respOk) {
        console.log('Nueva mesa incuida,comprobar en admin', json)
        this.numerosMesas.push(nuevoNumeroMesa);
        location.reload()
      } else {
        console.log('Hubo un error')
        console.log(json);
        this.errorMessage = json
      }
    },
    async delTable() {
      if (this.selectedTableId === null) {
        // Si no se ha seleccionado ninguna mesa, manejar la lógica apropiada
        alert('Selecciona una mesa antes de eliminarla.');
      }
      const { entity_id } = getClaimsFromToken(getAuthToken());
      // Utiliza this.selectedTableId para obtener el ID de la mesa seleccionada
      const resp = await deleteTableOfBar({ tableId: this.selectedTableId, barId: entity_id });
      const respOk = resp.ok;
      if (respOk) {
        location.reload();
      } else {
        this.errorDelMessage = 'Hubo un error al eliminar la mesa.';
      }
    },
    async changeTableStatus(tableNumber, newStatus) {

      const { entity_id } = getClaimsFromToken(getAuthToken());
      const table = this.tables.find(table => table.number === tableNumber);
      if (table.status === newStatus) {
        // No hace falta cambiar el estado si ya está en el estado deseado
        return;
      }
      // Realiza la actualización del estado en el backend
      const resp = await updateTableStatus({ tableId: table.id, barId: entity_id, newStatus });
      const respOk = resp.ok;
      const json = await resp.json()
      alert(JSON.stringify(json));
      if (respOk) {
        // Actualiza el estado en la interfaz
        location.reload()
      } else {
        console.error('Hubo un error al cambiar el estado de la mesa.');
      }
    },
  }
}
</script>

<template>
  <main class="container-fluid mt-5">
    <div class="mt-2 p-4" id="contenedorTitulo">
      <h1>{{ barData.name }} - MIS MESAS</h1>
      <h1>Numero de Mesas: {{ totalMesas }}</h1>
      <h3>Grado de Ocupación</h3>
      <div class="progress">
        <div class="progress-bar" :style="{ width: `${busyPercentage}%` }" role="progressbar" aria-valuenow="25"
          aria-valuemin="0" aria-valuemax="100">
          {{ busyPercentage }}%
        </div>
      </div>
    </div>
    <div class="row-container mb-0 text-center">
      <div class="row text-center d-inline-block mt-5">
        <h1 class="d-md-block d-none mb-0 border border-dashed border-dark">MAPA DE MESAS</h1>
      </div>
    </div>
    <div class="row text-center">
      <div id="inT" class="col-md-6">
        <h2 class="mt-1">MESAS INTERIOR</h2>
        <ul style="list-style-type: none;">
          <li v-for="(table, index) in indoorTables" :key="index">
            Mesa número: {{ table.number }}- Plazas: {{ table.seats }} - Estado: {{ table.status }}
            <button @click="changeTableStatus(table.number, 'BUSY')" v-if="table.status !== 'BUSY'"
              style="background-color: red;">OCUPAR MESA</button>
            <button @click="changeTableStatus(table.number, 'FREE')" v-if="table.status !== 'FREE'"
              style="background-color: greenyellow;">LIBERAR MESA</button>
            <hr>
          </li>
        </ul>
      </div>
      <div id="outT" class="col-md-6">
        <h2 class="mt-1">MESAS EXTERIOR</h2>
        <ul style="list-style-type: none;">
          <li v-for="(table, index) in outdoorTables" :key="index">
            Mesa número: {{ table.number }}- Plazas: {{ table.seats }} - Estado: {{ table.status }} - Exterior: {{
              table.outdoor }}
            <button @click="changeTableStatus(table.number, 'BUSY')" v-if="table.status !== 'BUSY'"
              style="background-color: red;">OCUPAR MESA</button>
            <button @click="changeTableStatus(table.number, 'FREE')" v-if="table.status !== 'FREE'"
              style="background-color: greenyellow;">LIBERAR MESA</button>
            <hr>
          </li>
        </ul>
      </div>
    </div>
    <div class="row text-center mb-0">
      <h1 class="d-md-block d-none mb-0 ">CRUD MESAS</h1>
    </div>
    <div class="row text-center">
      <div id="plusblock" class="col-md-6">
        <h2>AÑADIR MESA</h2>
        <table class="table table-hover border-dark">
          <thead class="table-dark">
            <tr>
              <th>Numero de asientos</th>
              <th>Ubicación mesa</th>
              <th>ACCIONES</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input class="w-100" type="number" placeholder="Numero de asientos" v-model="newTable.seats" /></td>
              <td><select v-model="newTable.outdoor">
                  <option :value="false">Interior</option>
                  <option :value="true">Exterior</option>
                </select>
              </td>
              <td class="text-center align-middle">
                <button class="round-button" @click="addTable()"><font-awesome-icon
                    icon="plus"></font-awesome-icon></button>
                <p class="w-50" id="showError">{{ errorMessage }}</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div id="minusblock" class="col-md-6">
        <h2>ELIMINAR MESA</h2>
        <table class="table table-hover border-darks">
          <thead class="table-dark">
            <tr>
              <th>Numero de mesa</th>
              <th>ACCIONES</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><select v-model="selectedTableId">
                  <option :value="null" disabled>Selecciona una mesa</option>
                  <option v-for="table in freeTables" :key="table.id" :value="table.id">
                    {{ table.number }} - Seats: {{ table.seats }} - Outdoor: {{ table.outdoor }}
                  </option>
                </select></td>
              <td class="text-center align-middle">
                <button class="round-button" @click="delTable()"><font-awesome-icon
                    icon="minus"></font-awesome-icon></button>
                <p class="w-50" id="showDelError">{{ errorDelMessage }}</p>
              </td>
            </tr>
          </tbody>
        </table>
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
  width: 35%;
  margin-left: 33%;
  border: #464646 2px solid;
  border-radius: 10%;
  font-size: 3vw;
}

#contenedorTitulo h3 {
  text-transform: capitalize;
  text-align: center;
  font-weight: bold;
  background-color: antiquewhite;
  border: #464646 2px solid;
  border-radius: 10%;
  width: 20%;
  margin-left: 40%;
  font-size: 2vw;
}

#inT {
  background-image: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.3)), url(../assets/indoorTable.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  border: solid 2px;
  max-height: 50vh;
  overflow-y: auto;
  font-style: italic;
}

#outT {
  background-image: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.3)), url(../assets/outdoorTable.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  border: solid 2px;
  max-height: 50vh;
  overflow-y: auto;
  font-style: italic;
}

#inT h2,
#outT h2 {
  border: 1px solid black;
  width: 50%;
  margin-left: 25%;
  background-color: rgba(164, 203, 54, 0.7);
}

#inT li,
#outT li {
  width: 100%;
  font-weight: bold;
  background-color: rgba(255, 255, 255, 0.2);
}

/* BOTON DE AÑADIR MESA */
.round-button {
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #3498db;
  /* Color de fondo del botón */
  color: white;
  /* Color del icono */
  border: none;
  cursor: pointer;
  font-size: 18px;
  outline: none;
}

.round-button:hover {
  background-color: #2980b9;
  /* Cambia el color al pasar el ratón sobre el botón */
}

/* ZONA AÑADIR MESA */
#plusblock {
  background: #D5E4E8 none repeat scroll 0 0;
  border: 3px solid #B5CAD0;
  margin: 15px 0px;
  padding: 20px;
}

#plusblock h2 {
  font-family: Georgia, "Times New Roman", Times, serif;
  font-weight: normal;
  text-shadow: 0 0 1px #000;
  color: #444444;
  font-size: 2em;
  padding: 2px 0 0;
  line-height: 1.2em;
  margin: 0 0 10px;
}

#minusblock {
  background: #D5E4E8 none repeat scroll 0 0;
  border: 3px solid #B5CAD0;
  margin: 15px 0px;
  padding: 20px;
}

#minusblock h2 {
  font-family: Georgia, "Times New Roman", Times, serif;
  font-weight: normal;
  text-shadow: 0 0 1px #000;
  color: #444444;
  font-size: 2em;
  padding: 2px 0 0;
  line-height: 1.2em;
  margin: 0 0 10px;
}</style>
