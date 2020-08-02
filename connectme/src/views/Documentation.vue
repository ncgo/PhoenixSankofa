<template>
  <span>
  <div>
    <v-alert
      v-model="alert"
      dismissible
      close-icon="mdi-delete"
      color="cyan"
      border="left"
      elevation="2"
      colored-border
      icon="mdi-twitter"
      style="z-index: 99;"
      fixed
    >
      Coming soom right at you!
    </v-alert>

    <div class="text-center">
      <v-btn
        v-if="!alert"
        dark
        @click="alert = true"
      >
        Coming Soon
      </v-btn>
    </div>
  </div>
    <div class="bannerTop"></div>
    <v-parallax
      dark
      style="height: 100%"
      src="https://cdn.pixabay.com/photo/2020/06/11/09/37/black-lives-matter-5285956_1280.jpg"
    >
      <div fixed class="bannerTop">
      <div id="titleTop">
          <h2>LET'S TALK DOCUMENTATION</h2>
          <v-btn @click="tryItOut"> Tweet @ Me!</v-btn><br />
          <v-btn color="red" @click="alert = true">
            Learn More
          </v-btn>
        </div></div>
        <v-container style="width: 50%; right: 0%">
        <v-img src="../assets/steps.png"></v-img>
        <v-img src="../assets/tools.png"></v-img>
        </v-container>
    </v-parallax>
  </span>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Documentation",
  data() {
    return {
      topicsArr: [
        "Black Lives Matter",
        "blm",
        "8 de Marzo",
        "Climate Change",
        "Me too",
        "Take a Knee",
      ],
      alert: true
    };
  },
  components: {},
  computed: {},
  methods: {
    learnMore() {
      window.open("https://blacklivesmatter.com/", "_blank");
    },
    tryItOut() {
      window.open(
        "https://twitter.com/intent/tweet?text=@ConnectMeWith_%20blm",
        "_blank"
      );
    },
  },
};
</script>

<style lang="scss" scoped>
.bannerTop {
  padding: 3%;
  height: 100%;
  width: 40%;
  position: absolute;
  background-color: black;
  left: 0%;
}
#titleTop {
  position: absolute;
  top: 300px;
  color: yellow;
  font-size: 40px;
  width: 400px;
  text-align: left;
  line-height: 150%;
  margin-left: -20px;
}

</style>
