<script></script>

<template>
  <main class="d-flex flex-column p-4 gap-2">
    <div class="col mt-4">
      <div class="column">
        <div class="content">
          <p class="titulo">Funciones de la Aplicación</p>
          <div class="row">
            <div class="col-md-6">
              <p class="subtitulo">Ultima versión</p>
              <ul>
                <li>Gestionar usuarios de tipo "Customer" junto sus acciones:
                  <ul>
                    <li>Edición de información propia.</li>
                    <li>Capacidad para reservar una mesa en una cantidad determinada de kilometros (de 1 a 5), con un
                      numero concreto de acompañantes y seleccionando si quiere que la mesa este fuera o dentro del bar.
                      EL PROGRAMA ESTA DISEÑADO PARA SOLO PERMITIR BUSCAR BARES EN LA PENÍNSULA IBÉRICA.
                    </li>
                  </ul>
                </li>
                <hr>
                <li>Gestionar usuarios de tipo "Bar" junto a sus acciones:
                  <ul>
                    <li>Edición de información propia, entre la que esta la ubicación del bar mediante el ingreso de la
                      latitud y longitud determinada.</li>
                    <li>Creación de anuncios, dependiendo del numero de estos se mostraran de diferente manera a la hora
                      de que el usuario customer vea la carta que se muestra cuando tiene la opcion de reservar o no,
                      junto a la descripcion. Estas dos cosas están pensadas como parte de los argumentos que tiene un
                      bar
                      para atraer la reserva.</li>
                    <li>
                      Incluye una pagina de gestion de las mesas, desde aqui podemos ver que grado de ocupacion en
                      porcentaje de nuestro bar esta siendo usado, junto a un mapa de nuestras mesas, diferenciando
                      entre
                      las exteriores e interiores y viendo las que tienen petición de reserva. También podemos añadir
                      mesas nuevas o eliminar mesas dentro de unas condiciones lógicas.
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
            <div class="col-md-6">
              <p class="subtitulo">Ideas para próximas versiones</p>
              <ul>
                <li>
                  En la ventana modal de registro de bar, este no tiene que ingresar su latitud y longitud concreta sino
                  tan solo pinchar en un punto del mapa.
                </li>
                <li>
                  Inclusion de una carta para el bar compuesta por productos y precios promoviendo asi el afán de
                  transparencia de la aplicación.
                </li>
                <li>
                  Sistema de votación propio de los usuarios hacia los bares y lo que es novedoso, votación de los
                  platos
                  de la carta para que tanto los otros usuarios como el dueño del bar pueda ver que platos estan
                  gustando.
                </li>
                <li>Todo esto conllevaría a una ventana para usuarios publicos con un buscador de bares pero sin la
                  limitación de las mesas, para así entrar y ver la carta, pero no sus promociones. Así se seguiría
                  fomentando el registro de clientes.</li>
                <li>Más...</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div class="col">
      <div class="column">
        <div class="content">
          <p class="titulo">Sobre el Creador</p>
          <div class="row">
            <div class="col-md-12 text-center">
              <img src="../assets/Javier montoto_page-0001.jpg" alt="Curriculum Vitae" width="75%" height="100%">
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
main {
  justify-content: space-between;
  height: auto;
  /* Cambiado a auto para adaptarse al contenido */
}

.column {
  /* Ajusta el ancho de cada columna según tu preferencia */
  width: 100%;
  /* 100% para ocupar todo el ancho */
}

.content {
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  /* Cambia el color de fondo según tu preferencia */
  padding: 20px;
  margin-bottom: 20px;
  /* Añadido para separar las columnas */
}

.titulo {
  color: black;
  text-align: center;
  font-size: 3em;
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  transition: all 0.3s;
  /* Agrega una transición suave a todos los cambios */
  position: relative;
  display: block;
  padding: 5px;
}

.titulo:hover {
  font-size: 2.5em;
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
}


.subtitulo {
  color: slategray;
  text-align: center;
  font-size: 2em;
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  transition: all 0.3s;
  /* Agrega una transición suave a todos los cambios */
  position: relative;
  display: block;
  padding: 5px;
}

.subtitulo:hover {
  font-size: 1.5em;
  /* Cambia el tamaño de fuente al pasar el cursor por encima */
}

li {
  color: darkolivegreen;
  font-family: "Latin Modern Roman";
  font-style: italic;
  font-size: 1.1vw;
  margin-bottom: 15px; /* Espacio inferior */
}

/*Agregacion final 10-05-2024*/
.col-md-6 {
  background-color: #f9f9f9;
  /* Color de fondo */
  padding: 20px;
  /* Espaciado interno */
  border-radius: 10px;
  /* Bordes redondeados */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  /* Sombra */
}

ul {
  list-style-type: none;
  /* Quita los puntos de la lista */
  padding-left: 0;
  /* Quita el padding izquierdo */
}
ul ul li {
  margin-top: 5px; /* Espacio superior */
  color: #555; /* Color del texto secundario */
}
hr {
  border: 0; /* Sin borde */
  border-top: 1px solid #ccc; /* Línea horizontal */
  margin: 20px 0; /* Espaciado superior e inferior */
}
</style>
