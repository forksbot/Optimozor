<template>
  <div class="render">
    <Navbar />
  <div>
    <v-container>
      <v-layout row wrap>
        <v-flex md2 xl3></v-flex>
        <v-flex md8 xl6 xs12>
          <v-combobox
    v-model="queries"
    label="You can highlight a word by searching it here."
    :items="items"
    chips
    flat
    clearable
    solo
    multiple
    maxlength="18"
  >
    <template v-slot:selection="data">
      <v-chip
        :selected="data.selected"
        color="#222f3e"
        class="white--text"
        @input="remove(data.item)"
      >
        <strong>{{ data.item }}</strong>&nbsp;
      </v-chip>
    </template>
  </v-combobox>
          <!-- Modify something -->
          <v-dialog
      v-model="dialog"
      width="500"
      fullscreen
      transition="slide-y-reverse-transition"
    >
      <template v-slot:activator="{ on }">
        <v-btn
          color="red"
          dark
          block
          depressed
          style="margin-bottom: 17px;"
          v-on="on"
        >
          <div class="text-none"><strong>Click here to modify something</strong></div>
        </v-btn>
      </template>

      <v-card color="#222f3e">
        <br>
        <br>
        <div
          class="font-weight-light headline white--text"
          color="#222f3e"
          primary-title
          style="text-align: center;"
        >
          Modify something:
        </div>
        <v-layout row wrap>
          <v-flex md2 xl3></v-flex>
          <v-flex md8 xl6 xs12>
            <div style="color: white; padding: 20px;">
              <div style="font-weight: bold; font-size: 20px;">Title:</div>
              <v-text-field
            label="Give a title to your document"
            maxlength="100"
            solo
            v-model="title"
          ></v-text-field>
        <div style="font-weight: bold; font-size: 20px;">Summary:</div>
        <v-textarea
          solo
          flat
          name="input-7-5"
          label="Summary"
          maxlength="100000"
          v-model="summary"
        ></v-textarea>
        <div style="text-align: center;">
          <v-btn
            color="white"
            depressed
            @click="dialog = false"
          >
            <div style="color: #222f3e;">Save</div>
          </v-btn>
        </div>
            </div>
          </v-flex>
          <v-flex md2 xl3></v-flex>
        </v-layout>
      </v-card>
    </v-dialog>
          <br>
          <div class="mainsec" id="exportthis"> <!-- Main -->
            <br>
            <br>
            <h3 class="font-weight-light" style="font-size: 36px; text-align: center;">{{title}}</h3>
            <br>
            <br>
            <br>
            <div>
                <div><span style="font-size: 20px;"><strong>{{summaryTitle}}:</strong></span></div>
                <br>
                <p style="font-size: 17px;">
                <span>
                {{summary}}
                </span>
                </p>
                <br>
                <div style="text-align: center;">___</div>
                <br>
                <div><span style="font-size: 20px;"><strong>{{essayTitle}}:</strong></span></div>
                <br>
                <!-- main text -->
                <p class="maintext">
                <text-highlight :queries="queries">
                {{description}}
                </text-highlight>
                </p>
                <br>
                <div style="text-align: center;">___</div>
                <br>
                <div>
                <span style="font-size: 20px;"><strong>{{definitionsTitle}}:</strong></span></div>
                <br>
                <div><span style="font-size: 16px;"><strong>{{definitions.word_1.word}}: </strong>{{definitions.word_1.definition}}</span>
                <br>
                <br>
                <span style="font-size: 16px;"><strong>{{definitions.word_2.word}}: </strong>{{definitions.word_2.definition}}</span>
                <br>
                <br>
                <span style="font-size: 16px;"><strong>{{definitions.word_3.word}}: </strong>{{definitions.word_3.definition}}</span>
                </div>
                <br>
                <br>
                <div style="text-align: center; color: gray;">Created on <a href="https://optimozor.herokuapp.com">Optimozor</a>, a <a href="https://twitter.com/merwanedr">@merwanedr</a> project.</div>
            </div>
          </div>
        </v-flex>
        <v-flex md2 xl3></v-flex>
      </v-layout>
      <v-tooltip left>
        <template v-slot:activator="{ on }">
      <v-btn
              dark
              fab
              bottom
              right
              small
              color="white"
              style="position: fixed;"
              v-on="on"
              @click="generate()"
            >
              <v-icon color="#222f3e">save</v-icon>
            </v-btn>
            </template>
        <span>Save as PDF</span>
      </v-tooltip>
    </v-container>
  </div>
  </div>
</template>

<script>
import Navbar from '../assets/Navbar';
import html2pdf from 'html2pdf.js';
export default {
  name: 'Render',
  components: {
    Navbar
  },
  data() {
      return {
          queries: [],
          items: [],
          description : '',
          summary: '',
          title: '',
          definitions: [],
          summaryTitle: '',
          essayTitle: '',
          definitionsTitle: '',
          dialog: false
      }
    },

  methods: {
      remove (item) {
        this.chips.splice(this.chips.indexOf(item), 1)
        this.chips = [...this.chips]
      },
      generate(){
        window.scrollTo(0,0);
        setTimeout(function(){ console.log("Saved!"); }, 1000);
        var element = document.getElementById('exportthis');
        var opt = {
        margin:       1,
        filename:     'essay.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' },

      };
        html2pdf().set(opt).from(element).save();
      }
  },
  beforeCreate() {
    if(this.$store.state.title == ''){
      this.$router.push({
          name: 'Home'
        })
    }
  },
  created() {
    this.title = this.$store.state.title;
    this.description = this.$store.state.text;
    this.summary = this.$store.state.summary;
    this.definitions = this.$store.state.definitions;
    if (this.$store.state.translationLang == 'french') {
      this.summaryTitle = 'Résumé';
      this.essayTitle = 'Texte';
      this.definitionsTitle = 'Définitions'
    } else if (this.$store.state.translationLang == 'spanish') {
      this.summaryTitle = 'Resumen';
      this.essayTitle = 'Texto';
      this.definitionsTitle = 'Definiciones'
    } else if (this.$store.state.translationLang == 'german') {
      this.summaryTitle = 'Zusammenfassung';
      this.essayTitle = 'Text';
      this.definitionsTitle = 'Definitionen'
    } else {
      this.summaryTitle = 'Summary';
      this.essayTitle = 'Text';
      this.definitionsTitle = 'Definitions'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mainsec{
    background-color: white;
    padding: 30px;
}
.maintext{
    font-size: 17px;
    line-height: 26px;
}
a, a:visited{
  text-decoration: none;
  color: #222f3e;
}
</style>
