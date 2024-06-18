<script>
import { getAllBars } from '../api/apiClient'

export default {
    data() {
        return {
            bars: []
        };
    },
    async mounted() {
        try {
            this.bars = await getAllBars(); 
        } catch (error) {
            console.error('Error al obtener los bares:', error);
        }
    }
};
</script>

<template>
    <main class="container-fluid mt-3 d-flex justify-content-center align-items-center flex-column">
        <h1 class="mt-5 custom-heading display-4">BARES CLIENTES DE BARLI</h1>
        <div class="table-responsive mt-5">
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
        </div>
    </main>
</template>

<style scoped>
.custom-heading {
    color: white;
    font-size: 4em;
    font-weight: bold;
    text-shadow: 2px 5px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
    background-color: #ff6600;
    border-radius: 50%;
    padding: 20px;
    text-align: center;
    display: inline-block;
}

.table-responsive {
    width: 100%;
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

.container-fluid {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    flex-direction: column;
}
</style>
