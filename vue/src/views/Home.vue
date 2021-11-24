<template>
  <div>
    <div class="row">
    <div class="col-md-3">
      <div @click="Movie" class="card card-1">
        <h3>Total Movie</h3>
        <br>
        <!-- <background-image src="@/assets/1.png" alt="1" > -->
        <p>Get movie data using TMDB API. There are 100 data. Click the View Details button to view information about the movie. You can also register a review.</p>
      </div>    
    </div>
    <div class="col-md-3">
      <div @click="Recommend" class="card card-2">
        <h3>Recommend Movie</h3>
        <br>
        <p>This page offers movie recommendations. There are about three. Randomly recommends 30 movies, other people's likes based on my likes data, high rating-based recommendations.</p>
      </div>
    </div>
    <div class="col-md-3">
      <div @click="Community" class="card card-3">
        <h3>Community</h3>
        <br>
        <p>This is a community page. You can tell your own story with Selowa users. There is also a function to register a comment under the article. Only you can edit or delete posts and comments..</p>
      </div>
    </div>
    <div class="col-md-3">
      <div @click="Profile" class="card card-4">
        <h3>Profile</h3>
        <br>
        <p>This is your profile page. You can watch your favorite movies. Not only that, but my personal information is also displayed. have a nice day.</p>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
    name:"Home",
     methods: {
       onInputKeyword: function (event) {
			// 검색어
			this.$emit('input-search', event.target.value)
    },
    Movie: function () {
        this.$router.push({ name: 'Movie' })
      },
    Recommend: function () {
        this.$router.push({ name: 'Recommend' })
      },
    Community: function () {
        this.$router.push({ name: 'BoardList' })
      },
    Profile: function () {
        this.$router.push({ name: 'Profile' })
      }
    }
}
</script>

<style>

</style>