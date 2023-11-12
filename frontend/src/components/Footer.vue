<script>
export default {
  methods: {
    getActualYear() {
      return new Date().getFullYear()
    }
  }
}
</script>

<template>
  <footer>CopyRight - Javier Montoto - {{getActualYear()}}</footer>
</template>

<style scoped>
footer {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 1em;
  background-color: rgba(64, 19, 19, 0.5);
  font-family: Georgia, 'Times New Roman', Times, serif;
  transition: background-color 0.3s; /* Agregar una transición suave a la propiedad background-color */
}

footer:hover {
  background-color:cadetblue /* Cambia el color de fondo al pasar el mouse sobre el footer */
}

</style>