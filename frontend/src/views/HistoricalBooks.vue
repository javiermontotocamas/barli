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
         this.bars = await getAllBars(); // Obtener todos los bares al montar el componente
      } catch (error) {
         console.error('Error al obtener los bares:', error);
      }
   },
   methods: {
      async fetchBookings() {
         if (this.selectedBar) {
            try {
               this.bookings = await getBookingsByBar(this.selectedBar); // Obtener las reservas del bar seleccionado

               // Verificar si el array de reservas está vacío después de obtenerlo
               if (this.bookings.length === 0) {
                  this.showNoBookingsMessage = true;
               } else {
                  this.showNoBookingsMessage = false;
               }
               // Generar los gráficos
               const response = await generateCharts(this.selectedBar);
               console.log(response)
               console.log(this.lineChartPath)
               this.lineChartPath = '..' + response.line_chart;
               console.log(this.lineChartPath)
               this.pieChartPath = response.pie_chart;
            } catch (error) {
               console.error('Error al obtener las reservas:', error);
            }
         }
      },
      formatDateTime(dateTimeString) {
         const dateTime = new Date(dateTimeString);
         const formattedDate = dateTime.toLocaleDateString();
         const formattedTime = dateTime.toLocaleTimeString();
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
   /* Color naranja */
   font-size: 4em;
   /* Tamaño de fuente grande */
   font-weight: bold;
   text-shadow: 2px 5px #000;
   /* Sombra de texto */
   margin-bottom: 20px;
   /* Espacio inferior */
}


.table {
   background-color: #fff;
   /* Fondo blanco para la tabla */
}

.table-hover tbody tr:hover {
   background-color: #f1f1f1;
   /* Fondo al pasar el mouse por una fila */
}

.table thead th {
   background-color: #343a40;
   /* Fondo oscuro para el encabezado */
   color: #fff;
   /* Texto blanco para el encabezado */
}

.table-bordered {
   border: 2px solid #343a40;
   /* Borde para la tabla */
}

.table-striped tbody tr:nth-of-type(odd) {
   background-color: rgba(0, 0, 0, 0.05);
   /* Rayas alternas en la tabla */
}

.text-center {
   vertical-align: middle;
   /* Alinear verticalmente el texto en el centro */
}
img {
   max-width: 100%; /* Ajustar imagen al contenedor */
   display: block; /* Asegurar que la imagen esté centrada */
   margin: 0 auto; /* Alinear imagen al centro */
}
</style>