<script>
import { getAllUsers } from '../api/apiClient'

export default {
    data() {
        return {
            users: [] 
        };
    },
    async mounted() {
        try {
            this.users = await getAllUsers(); 
        } catch (error) {
            console.error('Error al obtener los usuarios:', error);
        }
    }
};
</script>

<template>
    <main class="container-fluid mt-3 mt-3 d-flex justify-content-center align-items-center flex-column">
        <h1 class="mt-5 custom-heading display-4">USUARIOS CLIENTES DE BARLI</h1>
        <div class="table-responsive mt-5">
            <table class="table table-striped table-bordered table-hover">
                <thead class="table-dark">
                    <tr class="text-center">
                        <th>Id del Usuario</th>
                        <th>Nombre del Usuario</th>
                        <th>Telefono del Usuario</th>
                        <th>Correo Electrónico del Usuario</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user, x in users" :key="user.id" class="text-center">{{ console.log(users) }}
                        <td>{{ user.id }}</td>
                        <td>{{ user.fullname }}</td>
                        <td>{{ user.phone }}</td>
                        <td>{{ user.user.email }}</td>
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
