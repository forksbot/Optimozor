<template>
  <div class="nf">
    <Navbar />
  <br>
  <div>
    <v-container>
      <v-layout row wrap>
        <v-flex md2 xl3></v-flex>
        <v-flex md8 xl6 xs12>
          <div class="mainsec"> <!-- Main -->
            <img src="../assets/logo.png" height="50" alt="">
            <div class="display-3 font-weight-thin">OOPS</div>
            <div class="display-1 font-weight-light">404 Error</div>
          </div>
        </v-flex>
        <v-flex md2 xl3></v-flex>
      </v-layout>
    </v-container>
  </div>
  </div>
</template>

<script>
import Navbar from '../assets/Navbar';
export default {
  name: 'Nf',
  components: {
    Navbar
  },
  data() {
    return {
      
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mainsec{
  color: white;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

</style>
