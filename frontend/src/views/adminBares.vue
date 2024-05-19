<script>
import { getAllBars, getClaimsFromToken, getAuthToken } from '../api/apiClient'
export default {
    data() {
        return {
            bars: [] // Inicializar una propiedad para almacenar los bares
        };
    },
    async mounted() {
        try {
            this.bars = await getAllBars(); // Obtener los bares y asignarlos a la propiedad
        } catch (error) {
            console.error('Error al obtener los bares:', error);
        }
    }
};
</script>
<template>
    <main class="container-fluid mt-3">
        <h1 class="text-center mt-5 custom-heading display-4">BARES CLIENTES DE BARLI</h1>
        <table class="table table-striped table-bordered">
            <thead class="table-dark">
                <tr class="text-center">
                    <th>Nombre del Bar</th>
                    <th>Dueño/Usuario del Bar</th>
                    <th>Telefono de Contacto del Bar</th>
                    <th>Direccion actual del establecimiento</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="bar in bars" :key="bar.id" class="text-center">
                    <td>{{ bar.name }}</td>
                    <td>{{ bar.user.username }}</td>
                    <td>{{ bar.phone }}</td>
                    <td>{{ bar.address }}</td>
                </tr>
            </tbody>
        </table>
    </main>
</template>
<style scoped>
.custom-heading {
    color: #ff6600;
    /* Color naranja */
    font-size: 3em;
    /* Tamaño de fuente grande */
}
</style>