<script>
import { getAdsOfBar, deleteAdOfBar, getClaimsFromToken, getAuthToken, createAdOfBar } from '../api/apiClient'
export default {
  data() {
    return {
      ads: [],
      //Declaro el formulario que almacena los datos del nuevo anuncio
      errorMessage: '',
      newAd: {
        product_name: '',
        reduction: ''
      }
    }
  },
  async mounted() {
    this.getAds()
  },
  methods: {
    async getAds() {
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const response = await getAdsOfBar(entity_id)
      this.ads = await response.json()
    },
    async deleteAd(adId) {
      const { entity_id } = getClaimsFromToken(getAuthToken())
      const response = await deleteAdOfBar(entity_id, adId)
      const respOk = response.ok;
      if (respOk) {
        alert("Anuncio borrado correctamente");
        this.getAds();
      }
      else {
        alert("Ocurrio un problema al borrar el anuncio");
      }
    },
    async addAd() {
      this.errorMessage = ''
      const { entity_id } = getClaimsFromToken(getAuthToken())
      if (this.newAd.reduction >= 5 && this.newAd.reduction <= 95) {
        const resp = await createAdOfBar({ recordData: this.newAd, barId: entity_id })
        const respOk = resp.ok
        const json = await resp.json()
        if (respOk) {
          console.log('Subido el nuevo anuncio', json)
          this.getAds()
        } else {
          console.log('Hubo un error')
          console.log(json);
          this.errorMessage = json
        }
      } else {
        alert("El valor debe estar entre 5 y 95");
      }
    }
  }
}
</script>
<template>
  <main class="container-fluid mt-5">
    <h1 class="text-center mt-5 custom-heading">GESTION ANUNCIOS SOBRE PRODUCTOS DEL BAR</h1>
    <table class="table table-hover border-dark" style="opacity: 0.9;">
      <thead class="table-dark">
        <tr class="text-center">
          <th>PRODUCTO</th>
          <th>REDUCCIÓN DE PRECIO</th>
          <th>ACCIONES</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(ad, index) in ads" :key="index">
          <td class="text-center">{{ ad.product_name }}</td>
          <td class="text-center">{{ ad.reduction }}</td>
          <td>
            <button @click="deleteAd(ad.id)" class="w-100">Eliminar</button>
          </td>
        </tr>
        <tr>
          <td><input class="w-100" type="text" placeholder="Nombre alimento" v-model="newAd.product_name" /></td>
          <td><input class="w-100" type="number" placeholder="Proporción descuento" min="5" max="95"
              v-model="newAd.reduction" /></td>
          <td>
            <button @click="addAd()" class="w-100">Nueva promoción</button>
            <p class="w-50" id="showError">{{ errorMessage }}</p>
          </td>
        </tr>
      </tbody>
    </table>
  </main>
</template>

<style scoped>
main {
  height: 100vh;
  margin-bottom: 0%;
  background-image: url(../assets/food-prices.jpg);
  background-size: contain;
  background-position: center;
}

.custom-heading {
  padding: 10px 20px;
  border: 2px solid #4CAF50;
  border-radius: 20px;
  background-color: #f2f2f2;
  color: #333;
}
</style>
