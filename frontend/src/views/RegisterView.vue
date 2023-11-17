<script>
import { registerNewCustomerOrBar } from '../api/apiClient'

export default {
  data() {
    return {
      type: 'customer',
      userData: {
        user: {
          username: '',
          password: '',
        },
        fullname: '',
        phone: '',
        email: '',
        birthdate: ''
      },
      barData: {
        user: {
          username: '',
          password: '',
        },
        name: '',
        description: '',
        phone: '',
        email: '',
        address: '',
        latitude: '',
        longitude: ''
      }
    };
  },
  methods: {
    submitForm() {
      if (this.type === 'customer') {
        registerNewCustomerOrBar(this.userData)
          .then((resp) => resp.json())
          .then((datos) => console.log(datos))
          .catch((error) => console.log(error))
      }
      else if (this.type === 'bar') {
        registerNewCustomerOrBar(this.barData)
          .then((resp) => resp.json())
          .then((datos) => console.log(datos))
          .catch((error) => console.log(error))
      }
    }
  }
};
</script>

<template>
  <form @submit.prevent="submitForm" class="form-container">
    <div class="d-flex flex-row w-100">
      <div class="form-check form-check-inline border border-success w-100">
        <input class="form-check-input" type="radio" v-model="type" id="customer" value="customer">
        <label class="form-check-label" for="customer">Customer</label>
      </div>
      <div class="form-check form-check-inline border border-success w-100">
        <input class="form-check-input" type="radio" v-model="type" id="bar" value="bar">
        <label class="form-check-label" for="bar">Bar</label>
      </div>
    </div>
    <hr>
    <div v-if="type === 'customer'">
      <div class="row mb-3">
        <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
        <div class="col-sm-10">
          <input type="email" class="form-control" id="inputEmail3">
        </div>
      </div>
      <div class="form-group">
        <label for="username" class="mr-2">Username:</label>
        <input type="text" id="username" class="form-control" v-model="userData.user.username" required />
      </div>
      <div class="form-group">
        <label for="password" class="mr-2">Password:</label>
        <input type="password" id="password" class="form-control" v-model="userData.user.password" required />
      </div>
      <div class="form-group">
        <label for="fullname" class="mr-2">Nombre Completo:</label>
        <input type="text" id="fullname" class="form-control" v-model="userData.fullname" required />
      </div>
      <div class="form-group">
        <label for="phone" class="mr-2">Teléfono:</label>
        <input type="phone" id="phone" class="form-control" v-model="userData.phone" required />
      </div>
      <div class="form-group">
        <label for="email" class="mr-2">Email:</label>
        <input type="email" id="email" class="form-control" v-model="userData.email" required />
      </div>
      <div class="form-group">
        <label for="birthdate" class="mr-2">Fecha de Nacimiento:</label>
        <input type="date" id="birthdate" class="form-control" v-model="userData.birthdate" required />
      </div>
    </div>

    <div v-else-if="type === 'bar'">
      <div class="form-group">
        <label for="username" class="mr-2">Username:</label>
        <input type="text" id="username" class="form-control" v-model="barData.user.username" required />
      </div>
      <div class="form-group">
        <label for="password" class="mr-2">Password:</label>
        <input type="password" id="password" class="form-control" v-model="barData.user.password" required />
      </div>
      <div class="form-group">
        <label for="name" class="mr-2">Nombre Comercio:</label>
        <input type="text" id="name" class="form-control" v-model="barData.name" required />
      </div>
      <div class="form-group">
        <label for="description" class="mr-2">Descripción</label>
        <textarea id="description" class="form-control" v-model="barData.description" rows="4" required />
      </div>
      <div class="form-group">
        <label for="phone" class="mr-2">Teléfono:</label>
        <input type="phone" id="phone" class="form-control" v-model="barData.phone" required />
      </div>
      <div class="form-group">
        <label for="email" class="mr-2">Email:</label>
        <input type="email" id="email" class="form-control" v-model="barData.email" required />
      </div>
      <div class="form-group">
        <label for="address" class="mr-2">Dirección:</label>
        <input type="text" id="address" class="form-control" v-model="barData.address" required />
      </div>
      <div class="form-group">
        <label for="latitude" class="mr-2">Latitud:</label>
        <input type="text" id="latitude" class="form-control" v-model="barData.latitude" required />
      </div>
      <div class="form-group">
        <label for="longitude" class="mr-2">Longitud:</label>
        <input type="text" id="longitude" class="form-control" v-model="barData.longitude" required />
      </div>
    </div>

    <button type="submit">REGISTRO</button>
  </form>
</template>
<style scoped>
.form-container {
  max-width: 250px;
  margin: auto;
  width: 100%;
}

form {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

label {
  font-weight: bold;
  font-size: medium;
}

input,
button {
  padding: 4px;
  margin-bottom: 7px;
}

button {
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}
</style>