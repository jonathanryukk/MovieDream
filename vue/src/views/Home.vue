<template>
  <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="https://cdn.shopify.com/s/files/1/1416/8662/files/OFA-Sizes-world2_2048x2048.jpg?v=1513021592" class="d-block w-100" style="height:650px">
        <div class="carousel-caption d-none d-md-block">
          <h3>Movie dream</h3>
          <h4>Free your time</h4>
        </div>
      </div>
      <div class="carousel-item">
        <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FNBD8R%2FbtqEd9xLdMt%2FVvfGb1dzkdgqh6bJKk3As0%2Fimg.jpg" class="d-block w-100" style="height:650px">
        <div class="carousel-caption d-none d-md-block">
          <h3>Movie dream</h3>
          <h4>Free your time</h4>
        </div>
      </div>
      <div class="carousel-item">
        <img src="https://t1.daumcdn.net/cfile/tistory/99C9A2475E42854726" class="d-block w-100" style="height:650px" >
        <div class="carousel-caption d-none d-md-block">

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
</template>
<script>
export default {
    name:"Home",
     methods: {

    }
}
</script>

<style>
.row{
  justify-content: center;
  justify-items: center;
  margin: 50px;
  width: 90%;
}

</style>