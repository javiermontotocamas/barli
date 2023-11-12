<script>
export default {
  data() {
    return {
      formData: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    submitForm() {
      fetch('http://localhost:8000/api/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.formData),
      })
      .then((resp) => resp.json())
      .then((datos) => console.log(datos))
      .catch((error) => console.log(error));
    }
  }
};
</script>

<template>
  <form @submit.prevent="submitForm" class="form-container">
    <label for="username">Nombre de Usuario:</label>
    <input type="text" id="username" v-model="formData.username" required />
    <label for="password">Password:</label>
    <input type="password" id="password" v-model="formData.password" required />
    <button type="submit">LOGIN</button>
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
  gap: 10px;
}
label {
  font-weight: bold;
}
input, button {
  padding: 8px;
  margin-bottom: 10px;
}
button {
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}
</style>