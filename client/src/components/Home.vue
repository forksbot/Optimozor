<template>
  <div class="home">
    <Navbar />
  <div>
    <v-container>
      <v-layout row wrap>
        <v-flex md2 xl3></v-flex>
        <v-flex md8 xl6 xs12>
          <div class="mainsec"> <!-- Main -->
            <img src="../assets/logo.png" height="50" alt="">
            <h1 class="display-1 font-weight-light">Welcome to Optimozor</h1>
            <br>
            <h5 class="headline font-weight-light hidden-sm-and-down">Optimozor is a place where you can automatically optimize and summarize your notes, texts and courses. You can also use Optimozor to correct, translate and export your essays to PDFs.</h5>
            <h5 class="body-2 font-weight-light hidden-md-and-up">Optimozor is a place where you can automatically optimize and summarize your notes, texts and courses. You can also use Optimozor to correct, translate and export your essays to PDFs.</h5>
            <br>
            <br>
            <div style="color: red;" v-show="errormsgTitle">Please include a title.</div>
            <br>
            <v-text-field
            label="Give a title to your document"
            maxlength="100"
            solo
            v-model="title"
          ></v-text-field>
            <v-textarea
          solo
          flat
          name="input-7-4"
          label="Start now simply by pasting your text here! (Don't include titles)"
          maxlength="100000"
          v-model="text"
        ></v-textarea>
        <div style="color: red;" v-show="errormsgText">Please include at least 2500 Characters in your text.</div>
        <br>
        <div style="text-align: right;">{{text.length}}/100000 Characters</div>
          <v-layout row wrap>
            <v-flex md5 xs12>
              <div style="text-align: left; font-size: 20px;">Translation:</div>
      <v-radio-group row dark value="none" v-model="language">
        <v-radio color="white" label="None" value="none"></v-radio>
        <v-radio color="white" label="🇫🇷" value="french"></v-radio>
        <v-radio color="white" label="🇩🇪" value="german"></v-radio>
        <v-radio color="white" label="🇪🇸" value="spanish"></v-radio>
      </v-radio-group>
            </v-flex>
            <v-flex md2><!-- empty --></v-flex>
            <v-flex md5 xs12>
               <div style="text-align: left; font-size: 20px;">Options:</div>
            <v-checkbox
              label="Correct (experimental)"
              color="white"
              value="true"
              v-model="correct"
              hide-details
              dark
            ></v-checkbox>
            </v-flex>
          </v-layout>
          <div>
            <br>
            <br>
            <div style="color: white;">{{status}}</div>
            <v-progress-linear color="white" v-show="loadingStatus" :indeterminate="true"></v-progress-linear>
            <v-btn @click="post_essay()" :disabled="loadingStatus" depressed large color="white"><div style="color: #222f3e;">Launch</div></v-btn>
            <br>
            <br>
            <div style="font-weight: normal;">Optimozor will automatically summarize your essay.</div>
            <div>-</div>
            <div style="font-weight: normal;"><strong @click="demoText()">Click here</strong> to paste a demo text.</div>
          </div>
          </div>
        </v-flex>
        <v-flex md2 xl3></v-flex>
      </v-layout>
    </v-container>
  </div>
  </div>
</template>

<script>
import axios from 'axios';
import Navbar from '../assets/Navbar';
export default {
  name: 'Home',
  components: {
    Navbar
  },
  data() {
    return {
      title: '',
      text: '',
      language: '',
      correct: '',
      status: '',
      loadingStatus: false,
      errormsgText: false,
      errormsgTitle: false
    }
  },
  methods: {
    async post_essay(){
    // at least 2500 Char description
    if (this.title == '') {
      this.errormsgTitle = true;
    } else if (this.text.length < 2500) {
      this.errormsgText = true;
    } else {
    this.errormsgText = false;
    this.errormsgTitle = false;
    this.loadingStatus = true;
    this.status = 'Please wait ...';
    var essay_data = {
      'text': this.text,
      'title': this.title,
      'translation': this.language,
      'correct': this.correct
    };
    axios.post("api/", essay_data, { // full shit http://127.0.0.1:5000/api/
    headers: { 
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json'
     }
    }).then(results => {
      this.$store.state.title = results.data.title;
      this.$store.state.text = results.data.text;
      this.$store.state.summary = results.data.summary;
      this.$store.state.definitions = results.data.definitions;
      this.$store.state.translationLang = this.language;
      this.status = false;
      this.$router.push({
          name: 'Render'
        })
    })
    }
    },
    demoText(){
      this.title = 'The Blockchain Utopia.';
      this.text = "The idea of the Blockchain is actually an idea that has been sold to us as a revolutionary, life-changing idea. But what could the Blockchain actually bring into our lives? The best way to explain how something works is to explain it to a child, then to an adult, and see if both have the same concept. So, how would you explain the Blockchain to an 8 year old kid? I would say that you first have to teach him how a simple supermarket works. The idea behind a store is to act as a platform between consumers and producers. The farmer grows his carrots and sends them to Walmart, and Walmart sells them to someone else. The supermarket acts as an entity of trust because the farmer can’t just sell his carrots from his field, he has neither the manpower nor the means to do that. Blockchain’s idea is to eliminate trust platforms like Walmart to build trust from an agreement between two entities. To an adult, Imagine that you would like to sell your smartphone. You will probably go to a platform like Ebay to deposit it, you will ship it and you will wait for a buyer. But all of this is thanks to the trust you place in Ebay, a publicly traded, multi-billion dollar company that is very often the target of cyberattacks. In other words, if someone attacked the Ebay servers and deleted their databases, you will be the first victim because the traceability of your smartphone will be lost and there will be no more evidence that your phone belongs to you. It can really be scary when you imagine the same scenario with banks, insurance companies or notarial acts. The world needs a decentralized platform that records each element and ensures that it’s not editable or deletable. And that’s where Blockchain comes in. I will not go into details about how the Blockchain works, I’m sure there are thousands of articles about it on the Internet. But what interests us here is the concept, and what it brings concretely. I consider the Blockchain to be one of the four major technological revolution of our generation after the transistor, the personal computer and the Internet. Just like the Internet, the Blockchain brings something to our community. The Internet has made people from all over the world collaborate on common ideas and projects, and it is the tool that has enabled the greatest accumulation of data of the human species. The Blockchain aims for an equally high ideal, it wants to create trust between these people, and thereby, allow them to disrupt the foundation of things that were believed to be unchangeable, such as ownership, transactions or interactions. Imagine a world where you could own a tiny portion of a famous painting, or a square meter of a luxury apartment in the heart of Manhattan. Imagine a world where you could sell or buy something without using a third-party platform. This world would mean that we could all have a share of something (No, it’s not communism!) and invest in safe values no matter how rich we are. In 20 years, we may be able to live in a society transformed by Blockchain and artificial intelligence, our consumption habits could be completely disrupted, our interactions with people, money and governments could be drastically different. I’m not talking about the current state of things in which Blockchain applications are expensive and less convenient than more “classic” solutions. I’m talking about what it could represent in a few years. For those who think Blockchain is just a Buzzword to excite investors, remember that in the early days of the Internet, people were thinking of recipe pages, not Uber or Airbnb. Technology has been, is and will always be the element of our society that will move us forward and lead us to the apex of our civilization. We are at the dawn of a digital revolution.";
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mainsec{
  color: white;
  font-weight: bold;
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
  padding-top: 5px;
}
.quote{
  font-size: 20px;
  max-width: 500px;
}
</style>
