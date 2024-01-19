<script>
import { login, setAuthToken, setRefreshToken, getClaimsFromToken } from '../api/apiClient'
import router from '../router/index'

export default {
  emits: ['user-logged', 'close-modal'],
  data() {
    return {
      errorMessage: '',
      formData: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async submitForm() {
      let record
      this.errorMessage = ''
      console.log(this.formData)
      record = this.formData
      console.log(record)
      const resp = await login(record)
      const respOk = resp.ok
      const json = await resp.json()
      if (respOk) {
        // TODO: Redirigir a la pagina correspondiente
        setAuthToken(json.access)
        setRefreshToken(json.refresh)
        const claims = getClaimsFromToken(json.access)
        if (claims.role === 'user') {
          this.$router.push({ name: 'mainSearch' });
        } else if (claims.role === 'bar') {
          this.$router.push({ name: 'manageBooks' });
        }
        this.$emit('user-logged', { username: claims.username, role: claims.role })
        this.$emit('close-modal', true)
        this.formData.username = ''
        this.formData.password = ''
      } else {
        console.log('Hubo un error')
        this.errorMessage = json.detail
      }
    }
  }
}
</script>

<template>
  <form @submit.prevent="submitForm" class="form-container">
    <div v-if="errorMessage !== ''" class="d-flex flex-row w-100 text-danger">
      {{ errorMessage }}
    </div>
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

input,
button {
  padding: 8px;
  margin-bottom: 10px;
}

button {
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}
</style>
