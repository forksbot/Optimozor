<template>
  <div class="about">
    <Navbar />
  <br>
  <div>
    <v-container>
      <v-layout row wrap>
        <v-flex md2 xl3></v-flex>
        <v-flex md8 xl6 xs12>
          <div class="mainsec hidden-sm-and-down"> <!-- Main -->
            <img src="../assets/me.jpg" alt="" height="120" class="profilepic">
            <br>
            <br>
            <h2 class="profilename">What's up Internet</h2>
            <h4 class="profiledescription font-weight-thin">I'm Merwane.</h4>
            <br>
            <br>
            <div class="quote font-weight-medium font-italic">I created this project because I needed it, and I thought other people could use it! If it reaches 500 upvotes on ProductHunt, I will opensource it on GitHub. Feel free to ask me questions on Twitter or buy me a coffee if you like it!</div>
            <br>
            <br>
            <a href='https://ko-fi.com/J3J3U6LA' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
            <br>
            <v-btn :href=" 'https://twitter.com/intent/tweet?text='+tweet" target="_blank" depressed color="cyan" class="text-none">
              <div style="color: white; font-weight: bold;">Tweet</div>
            </v-btn>
            <br>
            <br>
            <v-btn href="https://www.producthunt.com/posts/optimozor" target="_blank" depressed color="deep-orange">
            <div style="color: white; font-weight: bold;">Upvote on Product Hunt <v-icon>arrow_drop_up</v-icon></div>
            </v-btn>
          </div>
          <!-- Mobile -->
          <div class="hidden-md-and-up" style="color: white; font-weight: bold; text-align: center;">
            <br>
            <br>
            <img src="../assets/me.jpg" alt="" height="120" class="profilepic">
            <br>
            <br>
            <h2 class="profilename">What's up Internet</h2>
            <h4 class="profiledescription font-weight-thin">I'm Merwane.</h4>
            <br>
            <br>
            <div class="quote font-weight-medium font-italic">I created this project because I needed it, and I thought other people could use it! If it reaches 500 upvotes on ProductHunt, I will opensource it on GitHub. Feel free to ask me questions on Twitter or buy me a coffee if you like it!</div>
            <br>
            <a href='https://ko-fi.com/J3J3U6LA' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
            <br>
            <v-btn :href=" 'https://twitter.com/intent/tweet?text='+tweet" target="_blank" depressed color="cyan" class="text-none">
              <div style="color: white; font-weight: bold;">Tweet</div>
            </v-btn>
            <br>
            <br>
            <v-btn href="https://www.producthunt.com/posts/optimozor" target="_blank" depressed color="deep-orange">
            <div style="color: white; font-weight: bold;">Upvote on Product Hunt <v-icon>arrow_drop_up</v-icon></div>
            </v-btn>
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
  name: 'About',
  components: {
    Navbar
  },
  data() {
    return {
      tweet: 'Check out Optimozor! a free tool to automatically summarize, optimize and translate your essays/texts by @merwanedr https://optimozor.herokuapp.com'
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mainsec{
  color: white;
  font-weight: bold;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
.profilepic{
  border-radius: 100px;
  border: 2px solid white;
}
.profilename{
  font-size: 24px;
  font-family: 'Ubuntu', sans-serif;
}
.profiledescription{
  font-size: 20px;
  padding-top: 5px;
}
.quote{
  font-size: 16px;
  max-width: 500px;
  text-align: left;
}
</style>
