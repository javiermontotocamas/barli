<script>
import { registerNewCustomerOrBar } from '../api/apiClient'

export default {
  data() {
    return {
      registered: false,
      errorMessage: '',
      type: 'customer',
      userData: {
        user: {
          username: '',
          password: '',
          email: ''
        },
        fullname: '',
        phone: '',
        birthdate: ''
      },
      barData: {
        user: {
          username: '',
          password: '',
          email: ''
        },
        name: '',
        description: '',
        phone: '',
        address: '',
        latitude: '',
        longitude: ''
      }
    };
  },
  methods: {
    async submitForm() {
      this.errorMessage = '';

      let record;
      if (this.type === 'customer') {
        record = this.userData;
      }
      else if (this.type === 'bar') {
        record = this.barData;
      }

      const resp = await registerNewCustomerOrBar({ type: this.type, recordData: record })
      const respOk = resp.ok
      const json = await resp.json()
      if (respOk) {
        console.log("Dado de alta con exito", json);
        this.registered = true;
      }
      else {
        console.log("Hubo un error");
        this.errorMessage = json.detail;
      }
    }
  }
};
</script>

<template>
  <div v-if="registered">
    <h6>Registrado correctamente. Ya puede hacer login</h6>
  </div>
  <form @submit.prevent="submitForm" class="form-container" v-else>
    <div v-if="errorMessage !== ''" class="d-flex flex-row w-100 text-danger">
      {{ errorMessage }}
    </div>
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
      <div class="row mb-2">
        <label for="username" class="col-sm-4 col-form-label">Nickname:</label>
        <div class="col-sm-8">
          <input type="text" id="username" class="form-control" v-model="userData.user.username" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="password" class="col-sm-4 col-form-label">Contraseña:</label>
        <div class="col-sm-8">
          <input type="password" id="password" class="form-control" v-model="userData.user.password" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="fullname" class="col-sm-4 col-form-label">Nombre:</label>
        <div class="col-sm-8">
          <input type="text" id="fullname" class="form-control" v-model="userData.fullname" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="phone" class="col-sm-4 col-form-label">Teléfono:</label>
        <div class="col-sm-8">
          <input type="phone" id="phone" class="form-control" v-model="userData.phone" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="email" class="col-sm-4 col-form-label">Email:</label>
        <div class="col-sm-8">
          <input type="email" id="email" class="form-control" v-model="userData.user.email" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="birthdate" class="col-sm-4 col-form-label">Fecha Nacimiento:</label>
        <div class="col-sm-8">
          <input type="date" id="birthdate" class="form-control" v-model="userData.birthdate" required />
        </div>
      </div>
    </div>

    <div v-else-if="type === 'bar'">
      <div class="row mb-2">
        <label for="username" class="col-sm-4 col-form-label">Username:</label>
        <div class="col-sm-8">
          <input type="text" id="username" class="form-control" v-model="barData.user.username" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="password" class="col-sm-4 col-form-label">Password:</label>
        <div class="col-sm-8">
          <input type="password" id="password" class="form-control" v-model="barData.user.password" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="name" class="col-sm-5 col-form-label">Bar Name:</label>
        <div class="col-sm-7">
          <input type="text" id="name" class="form-control" v-model="barData.name" required />
        </div>
      </div>
      <div class="form-group mb-2">
        <label for="description" class="mr-2">Description:</label>
        <textarea id="description" class="form-control" v-model="barData.description" rows="4" required />
      </div>
      <div class="row mb-2">
        <label for="phone" class="col-sm-4 col-form-label">Phone:</label>
        <div class="col-sm-8">
          <input type="phone" id="phone" class="form-control" v-model="barData.phone" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="email" class="col-sm-4 col-form-label">Email:</label>
        <div class="col-sm-8">
          <input type="email" id="email" class="form-control" v-model="barData.user.email" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="address" class="col-sm-4 col-form-label">Adress:</label>
        <div class="col-sm-8">
          <input type="text" id="address" class="form-control" v-model="barData.address" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="latitude" class="col-sm-4 col-form-label">Latitude:</label>
        <div class="col-sm-8">
          <input type="text" id="latitude" class="form-control" v-model="barData.latitude" required />
        </div>
      </div>
      <div class="row mb-2">
        <label for="longitude" class="col-sm-4 col-form-label">Lonitude:</label>
        <div class="col-sm-8">
          <input type="text" id="longitude" class="form-control" v-model="barData.longitude" required />
        </div>
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