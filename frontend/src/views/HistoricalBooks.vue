<script>
import { getAllBars, getBookingsByBar, generateCharts } from '../api/apiClient';

export default {
   data() {
      return {
         bars: [],
         selectedBar: null,
         bookings: [],
         showNoBookingsMessage: false,
         lineChartPath: '',
         pieChartPath: ''
      };
   },
   async mounted() {
      try {
         this.bars = await getAllBars();
      } catch (error) {
         console.error('Error al obtener los bares:', error);
      }
   },
   methods: {
      async fetchBookings() {
         if (this.selectedBar) {
            try {
               this.bookings = await getBookingsByBar(this.selectedBar);

               if (this.bookings.length === 0) {
                  this.showNoBookingsMessage = true;
                  this.lineChartPath = '';
                  this.pieChartPath = '';
               } else {
                  this.showNoBookingsMessage = false;
                  const response = await generateCharts(this.selectedBar);
                  console.log(response)
                  console.log(this.lineChartPath)
                  this.lineChartPath = '..' + response.line_chart;
                  console.log(this.lineChartPath)
                  this.pieChartPath = response.pie_chart;
               }
            } catch (error) {
               console.error('Error al obtener las reservas:', error);
            }
         }
      },
      formatDateTime(dateTimeString) {
         const dateTime = new Date(dateTimeString);
         const formattedDate = dateTime.toLocaleDateString();
         const formattedTime = dateTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }); // Cambiado para no mostrar los segundos
         return `${formattedDate} ${formattedTime}`;
      }
   }
};
</script>

<template>
   <main class="container-fluid mt-0">
      <h1 class="text-center mt-5 custom-heading display-4">Reservas Completadas por Bar y Cliente</h1>
      <div class="form-group">
         <label for="barSelect">Selecciona un Bar:</label>
         <select v-model="selectedBar" class="form-control" id="barSelect">
            <option v-for="bar in bars" :key="bar.id" :value="bar.id">{{ bar.name }}</option>
         </select>
      </div>
      <button @click="fetchBookings" class="btn btn-primary mt-3">Traer Reservas</button>
      <div v-if="showNoBookingsMessage" class="alert alert-warning mt-3" role="alert">
         No hay reservas para este bar.
      </div>
      <template v-if="bookings.length">
         <div class="table-responsive">
            <table class="table table-striped table-bordered table-hover mt-3">
               <thead class="table-dark">
                  <tr class="text-center">
                     <th>ID de la Reserva</th>
                     <th>Id del Usuario</th>
                     <th>Fecha/Hora de la Reserva</th>
                  </tr>
               </thead>
               <tbody>
                  <tr v-for="booking in bookings" :key="booking.id" class="text-center">
                     <td>{{ booking.id }}</td>
                     <td>{{ booking.user }}</td>
                     <td>{{ formatDateTime(booking.initial_datetime) }}</td>
                  </tr>
               </tbody>
            </table>
         </div>
      </template>
      <template v-if="lineChartPath">
         <img :src="lineChartPath" alt="Gráfico de Línea" class="chart-img mt-3">
      </template>

      <template v-if="pieChartPath">
         <img :src="pieChartPath" alt="Gráfico de Tarta" class="chart-img mt-3">
      </template>
   </main>
</template>

<style scoped>
.custom-heading {
   color: #ff6600;
   font-size: 4em;
   font-weight: bold;
   text-shadow: 2px 5px #000;
   margin-bottom: 20px;
}

.table-responsive {
   max-height: 400px;
   overflow-y: auto;
}

.table {
   background-color: #fff;
}

.table-hover tbody tr:hover {
   background-color: #f1f1f1;
}

.table thead th {
   background-color: #343a40;
   color: #fff;
   position: sticky;
   top: 0;
   z-index: 1;
}

.table-bordered {
   border: 2px solid #343a40;
}

.table-striped tbody tr:nth-of-type(odd) {
   background-color: rgba(0, 0, 0, 0.05);
}

.text-center {
   vertical-align: middle;
}

img {
   max-width: 100%;
   display: block;
   margin: 0 auto;
}
</style>