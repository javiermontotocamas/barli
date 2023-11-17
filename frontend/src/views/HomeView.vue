<script>
import { FontAwesomeIcon } from '@/plugins/fontawesome';
import { RouterLink } from 'vue-router';
</script>


<template>
  <main class="container-fluid">
    <div id="carouselExampleCaptions" data-bs-ride="carousel" class="carousel slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"
          aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"
          aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"
          aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="carousel-caption">
            <h5 class="animate__animated animate__fadeInDown" style="animation-delay:1s;">Encuentra <span>Mesa</span></h5>
            <p class="animate__animated animate__fadeInUp" style="animation-delay:2s;">Lorem ipsum dolor sit amet consectetur adipisicing
              elit. Molestias inventore beatae doloribus vel, nisi totam.</p>
            <p class="animate__animated animate__fadeInUp" style="animation-delay:3s;"><a href="#">Learn More</a></p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="carousel-caption">
            <h5 class="animate__animated animate__fadeInDown" style="animation-delay:1s;">Haz <span>Reserva</span></h5>
            <p class="animate__animated animate__fadeInUp" style="animation-delay:2s;">Lorem ipsum dolor sit amet consectetur adipisicing
              elit. Molestias inventore beatae doloribus vel, nisi totam.</p>
            <p class="animate__animated animate__fadeInUp" style="animation-delay:3s;"><a href="#">Learn More</a></p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="carousel-caption">
            <h5 class="animate__animated animate__fadeInDown" style="animation-delay:1s;">No <span>Esperes</span></h5>
            <p class="animate__animated animate__fadeInUp" style="animation-delay:2s;">Lorem ipsum dolor sit amet consectetur adipisicing
              elit. Molestias inventore beatae doloribus vel, nisi totam.</p>
            <p class="animate__animated animate__fadeInUp" style="animation-delay:3s;"><a href="#">Learn More</a></p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <!--About zone-->
    <div class="about-area section-padding" id="about">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 col-sm-12">
            <div class="img-area">
              <img src="../assets/about.jpg" alt="joven conversando">
            </div>
          </div>
          <div class="col-lg-6 col-mg-12">
            <div class="about-text">
              <h2>We Are <span>Innovative</span> People</h2>
              <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae quod nulla aliquid ab iure
                aspernatur quasi facilis debitis, possimus, error dolore culpa, accusamus consectetur minus deserunt
                temporibus minima suscipit. Explicabo veniam maxime aut cum mollitia tempora nulla aliquam quos est error
                laudantium pariatur repellendus obcaecati, repudiandae inventore iste cumque ab?</p>
              <router-link :to="{ name: 'about' }" class="nav-link" router-link-active="active">Contact Us</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Services zone-->
    <div class="services section-padding" id="services">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="section-header text-center">
              <h2>Our <span>Services</span></h2>
              <p>Lorem ipsum dolor sit amet</p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-services text-center">
              <font-awesome-icon icon="martini-glass-citrus" class="icon-services"></font-awesome-icon>
              <h2>Promote Your Bar</h2>
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Molestiae, quia repudiandae. Aut omnis fuga
                inventore.</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-services text-center">
              <font-awesome-icon icon="champagne-glasses" class="icon-services"></font-awesome-icon>
              <h2>More Customers</h2>
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Molestiae, quia repudiandae. Aut omnis fuga
                inventore.</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-services text-center">
              <font-awesome-icon icon="calendar-plus" class="icon-services"></font-awesome-icon>
              <h2>Your Schedule</h2>
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Molestiae, quia repudiandae. Aut omnis fuga
                inventore.</p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-services text-center">
              <font-awesome-icon icon="wrench" class="icon-services"></font-awesome-icon>
              <h2>Reliable</h2>
              <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Molestiae, quia repudiandae. Aut omnis fuga
                inventore.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--Why us zone-->
    <div class="choose section-padding" id="choose">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="section-header text-center">
              <h2>Why <span>Choose Us?</span></h2>
              <p>Lorem ipsum dolor sit amet</p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-7">
            <div class="choose-area text-center">
              <div class="row">
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <div class="single-box">
                    <font-awesome-icon icon="automobile" class="icon-why"></font-awesome-icon>
                    <h2>Why <span>Choose Us?</span></h2>
                    <p>Lorem ipsum dolor sit amet</p>
                  </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <div class="single-box">
                    <font-awesome-icon icon="cogs" class="icon-why"></font-awesome-icon>
                    <h2>Why <span>Choose Us?</span></h2>
                    <p>Lorem ipsum dolor sit amet</p>
                  </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <div class="single-box">
                    <font-awesome-icon icon="adjust" class="icon-why"></font-awesome-icon>
                    <h2>Why <span>Choose Us?</span></h2>
                    <p>Lorem ipsum dolor sit amet</p>
                  </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <div class="single-box">
                    <font-awesome-icon icon="wrench" class="icon-why"></font-awesome-icon>
                    <h2>Why <span>Choose Us?</span></h2>
                    <p>Lorem ipsum dolor sit amet</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-5 col-sm-12">
            <div class="choose-img">
              <img src="../assets/choose.jpg" alt="imagen sevilla">
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--Testimonial zone-->
    <div class="testimonial-section padding" id="testi">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="section-header text-center">
              <h2>Clients <span>Comments</span></h2>
              <p>Lorem ipsum dolor sit amet</p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 col-sm-12">
            <div class="single-client text-center">
              <div class="imgBox">
                <img src="../assets/cara1.jpg" alt="">
              </div>
              <h2>John Doe</h2>
              <p><i>"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Id tenetur obcaecati eius corrupti sit
                  a!"</i></p>
              <h5>HR Manager <br><span>ABC Company</span></h5>
            </div>
          </div>
          <div class="col-lg-4 col-sm-12">
            <div class="single-client text-center">
              <div class="imgBox">
                <img src="../assets/cara2.jpg" alt="">
              </div>
              <h2>John Doe</h2>
              <p><i>"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Id tenetur obcaecati eius corrupti sit
                  a!"</i></p>
              <h5>HR Manager <br><span>ABC Company</span></h5>
            </div>
          </div>
          <div class="col-lg-4 col-sm-12">
            <div class="single-client text-center">
              <div class="imgBox">
                <img src="../assets/cara3.jpg" alt="">
              </div>
              <h2>John Doe</h2>
              <p><i>"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Id tenetur obcaecati eius corrupti sit
                  a!"</i></p>
              <h5>HR Manager <br><span>ABC Company</span></h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<style scoped>
* {
  font-family: montserrat;
}

/* carousel*/
.carousel {
  background-image: url(../assets/home.jpg);
  background-size: cover;
  background-position: center;
}

.carousel-item {
  height: 100vh;
  min-height: 300px;
}

.carousel-caption {
  bottom: 220px;
  z-index: 2;
  left: 8%;
}

.carousel-caption h5 {
  font-size: 45px;
  margin-top: 25px;
  color: #08194a;
  font-weight: 700;
  text-align: left;
}

.carousel-caption span {
  color: #e53f29;
  font-weight: 900
}

.carousel-caption p {
  width: 60%;
  font-size: 18px;
  line-height: 1.8;
  color: #08194a;
  text-align: left;
}

.carousel-caption a {
  text-transform: uppercase;
  text-decoration: none;
  background: #08194a;
  padding: 5px 20px;
  display: inline-block;
  color: #fff;
  margin-top: 15px;
  border-radius: 5px;
}

/*About(second) zone */
.img-area img {
  width: 100% !important;
}

.about-text h2 {
  font-size: 45px;
  font-weight: 700;
  color: #08194a;
}

.about-text h2 span {
  color: #e53f29;
}

.about-text a {
  text-transform: uppercase;
  text-decoration: none;
  background: #08194a;
  padding: 5px 20px;
  display: inline-block;
  color: #fff;
  border-radius: 5px;
}

/*Services zone */
.section-header {
  margin-bottom: 40px;
}

.section-header h2 {
  color: #08194a;
  font-size: 45px;
  font-weight: 700;
}

.section-header span {
  color: #e53f29;
}

.single-services {
  background: #08194a;
  color: #fff;
  padding: 30px 15px;
}

.icon-services {
  font-size: 45px;
  margin-bottom: 30px;
}

.single-services h2 {
  font-family: fantasy;
}

/*Why Us zone */
.choose-img img {
  width: 80%;
  padding-left: 30%;
}

.single-box {
  padding: 20px;
}

.icon-why {
  font-size: 35px;
  margin-bottom: 25px;
  color: #e53f29;
}

.single-box h2 {
  font-family: fantasy;
  color: #08194a;
}

/* Testimonial Zone */
.imgBox {
  width: 80px;
  height: 80px;
  overflow: hidden;
  border-radius: 50%;
  margin: 0 auto 25px;
}

.imgBox img {
  width: 100%;
}

.single-client {
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
  padding: 30px 15px;
}

.single-client h2 {
  color: #08194a;
  font-family: fantasy;
}

.single-client h5 {
  color: #08194a;
  font-weight: 600;
  font-size: 15px;
}

.single-client h5 span {
  font-size: 12px;
  text-transform: uppercase;
}
</style>

