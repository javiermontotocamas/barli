<script>
import { getAllBars } from '../api/apiClient'

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
        <table class="table table-striped table-bordered table-hover">
            <thead class="table-dark">
                <tr class="text-center">
                    <th>Nombre del Bar</th>
                    <th>Dueño/Usuario del Bar</th>
                    <th>Teléfono de Contacto del Bar</th>
                    <th>Dirección Actual del Establecimiento</th>
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
</style>
