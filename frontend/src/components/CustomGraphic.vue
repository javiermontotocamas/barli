<template>
    <div>
      <line-chart :chart-data="lineChartData" :options="lineChartOptions"></line-chart>
      <pie-chart :chart-data="pieChartData" :options="pieChartOptions"></pie-chart>
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { Line, Pie } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, LineController, CategoryScale, LinearScale, ArcElement, PieController } from 'chart.js';
  
  ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, LineController, CategoryScale, LinearScale, ArcElement, PieController);
  
  export default defineComponent({
    components: {
      LineChart: {
        extends: Line,
        props: ['chartData', 'options'],
      },
      PieChart: {
        extends: Pie,
        props: ['chartData', 'options'],
      }
    },
    props: {
      bookings: Array,
    },
    data() {
      return {
        lineChartData: {
          labels: [],
          datasets: [
            {
              label: 'Historico de Reservas',
              data: [],
              backgroundColor: 'rgba(54, 162, 235, 0.2)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1,
            },
          ],
        },
        pieChartData: {
          labels: [],
          datasets: [
            {
              data: [],
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
              ],
              borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
              ],
              borderWidth: 1,
            },
          ],
        },
        lineChartOptions: {
          responsive: true,
          scales: {
            x: {
              type: 'time',
              time: {
                unit: 'day'
              }
            },
            y: {
              beginAtZero: true,
            },
          },
        },
        pieChartOptions: {
          responsive: true,
        },
      };
    },
    watch: {
      bookings(newBookings) {
        this.updateLineChart(newBookings);
        this.updatePieChart(newBookings);
      },
    },
    methods: {
      updateLineChart(bookings) {
        const dates = bookings.map(booking => new Date(booking.initial_datetime));
        this.lineChartData.labels = dates;
        this.lineChartData.datasets[0].data = bookings.map(() => 1); // Solo cuenta el número de reservas
      },
      updatePieChart(bookings) {
        const userCounts = {};
        bookings.forEach(booking => {
          if (userCounts[booking.user]) {
            userCounts[booking.user]++;
          } else {
            userCounts[booking.user] = 1;
          }
        });
        this.pieChartData.labels = Object.keys(userCounts);
        this.pieChartData.datasets[0].data = Object.values(userCounts);
      },
    },
  });
  </script>
  