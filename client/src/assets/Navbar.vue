<template>
<div>
    <v-toolbar flat color="transparent">
    <router-link to="/"><v-toolbar-title style="color: white; font-family: 'Ubuntu', sans-serif;">Optimozor</v-toolbar-title></router-link>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn to="/about" color="#222f3e" flat depressed small fab class="white--text">
        <v-icon style="font-size: 23px;">account_circle</v-icon>
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</div>
</template>
<script>
export default {
  name: 'Navbar'
}
</script>
<style scoped>
a, a:visited{
  color: white;
  text-decoration: none;
}
</style>