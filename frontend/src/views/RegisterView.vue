<script>
export default {
  data() {
    return {
      formData: {
        fullName: '',
        password: '',
        phone: '',
        email: '',
        birthdate: ''
      }
    };
  },
  methods: {
    submitForm() {
      console.log('Datos enviados:', this.formData);
    }
  }
};
</script>

<template>
  <form @submit.prevent="submitForm" class="form-container">
    <label for="fullName">Nombre Completo:</label>
    <input type="text" id="fullName" v-model="formData.fullName" required />
    <label for="password">Password:</label>
    <input type="password" id="password" v-model="formData.password" required />
    <label for="phone">Teléfono:</label>
    <input type="tel" id="phone" v-model="formData.phone" required />
    <label for="email">Correo Electrónico:</label>
    <input type="email" id="email" v-model="formData.email" required />
    <label for="birthdate">Fecha de Nacimiento:</label>
    <input type="date" id="birthdate" v-model="formData.birthdate" required />
    <button type="submit">REGISTRO</button>
  </form>
</template>
<style scoped>
.form-container {
  max-width: 250px;
  margin: auto;
}
form {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
label {
  font-weight: bold;
}
input, button {
  padding: 4px;
  margin-bottom: 7px;
}
button {
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}
</style>