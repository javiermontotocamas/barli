<script></script>

<template>
  <main class="d-flex flex-column p-4 gap-2">
    <div class="col mt-4">
      <div class="column">
        <div class="content">
          <p class="titulo">Funciones de la Aplicación</p>
          <div class="row">
            <div class="col-md-6">
              <div class="card">
                <p class="subtitulo">Ultima versión</p>
                <ul class="custom-list">
                  <li>
                    Gestionar usuarios de tipo "Customer" junto sus acciones:
                    <ul>
                      <li>Edición de información propia.</li>
                      <li>
                        Capacidad para reservar una mesa en una cantidad determinada de kilómetros (de 1 a 5), con un
                        número concreto de acompañantes y seleccionando si quiere que la mesa esté fuera o dentro del
                        bar.
                        EL PROGRAMA ESTÁ DISEÑADO PARA SOLO PERMITIR BUSCAR BARES EN LA PENÍNSULA IBÉRICA.
                      </li>
                    </ul>
                  </li>
                  <hr>
                  <li>
                    Gestionar usuarios de tipo "Bar" junto a sus acciones:
                    <ul>
                      <li>Edición de información propia, entre la que está la ubicación del bar mediante el ingreso de
                        la
                        latitud y longitud determinada.</li>
                      <li>
                        Creación de anuncios, dependiendo del número de estos se mostrarán de diferente manera a la hora
                        de que el usuario customer vea la carta que se muestra cuando tiene la opción de reservar o no,
                        junto a la descripción. Estas dos cosas están pensadas como parte de los argumentos que tiene un
                        bar para atraer la reserva.
                      </li>
                      <li>
                        Incluye una página de gestión de las mesas, desde aquí podemos ver qué grado de ocupación en
                        porcentaje de nuestro bar está siendo usado, junto a un mapa de nuestras mesas, diferenciando
                        entre
                        las exteriores e interiores y viendo las que tienen petición de reserva. También podemos añadir
                        mesas nuevas o eliminar mesas dentro de unas condiciones lógicas.
                      </li>
                    </ul>
                  </li>
                </ul>
              </div>
            </div>
            <div class="col-md-6">
              <div class="card">
                <p class="subtitulo">Ideas para próximas versiones</p>
                <ul class="custom-list">
                  <li>
                    En la ventana modal de registro de bar, este no tiene que ingresar su latitud y longitud concreta
                    sino
                    tan solo pinchar en un punto del mapa.
                  </li>
                  <li>
                    Inclusión de una carta para el bar compuesta por productos y precios promoviendo así el afán de
                    transparencia de la aplicación.
                  </li>
                  <li>
                    Sistema de votación propio de los usuarios hacia los bares y lo que es novedoso, votación de los
                    platos
                    de la carta para que tanto los otros usuarios como el dueño del bar pueda ver qué platos están
                    gustando.
                  </li>
                  <li>
                    Todo esto conllevaría a una ventana para usuarios públicos con un buscador de bares pero sin la
                    limitación de las mesas, para así entrar y ver la carta, pero no sus promociones. Así se seguiría
                    fomentando el registro de clientes.
                  </li>
                  <li>Más...</li>
                </ul>
              </div>
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
}

.column {
  width: 100%;
}

.content {
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  padding: 20px;
  margin-bottom: 20px;
}

.titulo {
  color: black;
  text-align: center;
  font-size: 3em;
  font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  transition: all 0.3s;
  position: relative;
  display: block;
  padding: 5px;
}

.titulo:hover {
  font-size: 2.5em;
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
  position: relative;
  display: block;
  padding: 5px;
}

.subtitulo:hover {
  font-size: 1.5em;
}

.custom-list {
  list-style-type: none;
  padding-left: 0;
}

.custom-list ul {
  padding-left: 20px;
}

.custom-list li {
  color: darkolivegreen;
  font-family: "Latin Modern Roman";
  font-style: italic;
  font-size: 1.2vw;
  font-weight: 500;
  margin-bottom: 15px;
}

.custom-list ul li {
  margin-top: 5px;
  color: #555;
}

.card {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
}

hr {
  border: 0;
  border-top: 1px solid #ccc;
  margin: 20px 0;
}
</style>
