<script>
</script>

<template>
  <main class="d-flex justify-content-between flex-column flex-md-row p-4 gap-2">
    <div class="col">
      <div class="column" id="empresa">
        <div class="content">
          <p class="titulo">Sobre Barli</p>
          <p>Bienvenido a Barli, tu compañero perfecto para encontrar el bar ideal. En Barli, entendemos que la
            experiencia
            de salir a disfrutar de un buen momento con amigos o seres queridos debe ser sencilla y agradable. Es por eso
            que hemos creado esta aplicación única, diseñada para hacer que la búsqueda de bares sea más fácil y eficiente
            que nunca.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="column" id="autor">
        <div class="content">
          <p class="titulo">Sobre Javier Montoto</p>
          <p>Hola, soy Javier Montoto, un apasionado programador de 28 años con un toque de creatividad. Vivo en la
            hermosa
            ciudad de Sevilla, donde encuentro inspiración en cada rincón de esta tierra rica en cultura y tradición.
            Desde
            joven, me he sentido atraído por el mundo de la programación, y he invertido tiempo y energía en cultivar mis
            habilidades en este campo en constante evolución.</p>
        </div>
      </div>
    </div>
    <div class="col">
      <div class="column" id="contacto">
        <div class="content">
          <p class="titulo">Contacto</p>
          <p>Teléfono: +34 123 456 789 (Número de teléfono ficticio)</p>
          <p>Email: javier.montoto@example.com (Dirección de correo electrónico ficticia)</p>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
main {
  justify-content: space-between;
  height: 25rem;
}

.column {
  /* Ajusta el ancho de cada columna según tu preferencia */
  height: 100%;
  /* Establece una altura fija para todas las columnas */
}

.content {
  color: darkolivegreen;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  border: 1mm solid rgb(120, 13, 228);
  /* Cambia el color de fondo según tu preferencia */
  padding: 20px;
  border-radius: 10px;
  height: 100%;
}

/* Define colores de fondo diferentes para cada columna */
#empresa .content {
  background-color: rgba(255, 215, 0, 0.3);
  /* Ejemplo de color de fondo dorado */
}

#autor .content {
  background-color: rgba(0, 122, 204, 0.3);
  /* Ejemplo de color de fondo azul */
}

#contacto .content {
  background-color: rgba(255, 87, 51, 0.3);
  /* Ejemplo de color de fondo naranja */
}

.titulo {
  color: black;
  text-align: center;
  font-size: 24px;
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  transition: all 0.3s;
  /* Agrega una transición suave a todos los cambios */
  position: relative;
  display: block;
  padding: 5px;
}

.titulo:hover {
  font-size: 28px;
  /* Cambia el tamaño de fuente al pasar el cursor por encima */
}

.content .titulo::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(to right, #b47dcd, #e878a2, #eb85ab);
  z-index: 1;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.5s ease-in-out;
}

.content .titulo:hover::before {
  transform: scaleX(1);
}</style>
