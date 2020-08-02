<template>
  <v-container style="width: 140%; margin-bottom: 500px margin-top: -3%; margin-left: 0%">
    <div class="bannerTop"></div>
    <v-parallax
      style="height: 600px; width: 150%; margin-top: 7%; margin-left: -5%"
      src="https://nacla.org/sites/default/files/news-stories/marcha16.08.8_0.jpg"
    >
      <v-container style="margin-top: -15%">
        <v-row>
          <v-card
            class="mx-auto tweetExp center"
            color="#E0193D"
            dark
            max-width="550"
          >
            <v-card-title>
              <v-icon large left>
                mdi-twitter
              </v-icon>
              <span class="title font-weight-light">Twitter</span>
            </v-card-title>

            <v-card-text class="headline font-weight-bold">
              @ConnectMeWith_ Is an effort to connect others during COVID and
              beyond to educate and stimulate conversations about social
              movements and organizations.
            </v-card-text>
          </v-card>
          <v-card class="card2" max-width="600px">
            <v-card-text>
              <div>A twitter</div>
              <p class="display-1 text--primary">
                Bot
              </p>
              <p>built with</p>
              <div class="text--primary">
                -Twitter API<br />
                -Python<br />
                -TinyDB<br />
                -Google News API<br />
              </div>
            </v-card-text>
          </v-card>
          <v-img class="imgExp" src="../assets/1.png"></v-img>
        </v-row>
      </v-container>
    </v-parallax>
    <v-parallax
      style="height: 500px; width: 150%; margin-left: -5%"
      src="https://pyxis.nymag.com/v1/imgs/036/07f/fcb0ad3c18fc4b6371e4add4a2681e4208-19-climate-protest-children.rsocial.w1200.jpg"
    >
      <v-container style="margin-top: -20%">
        <v-card
          class="mx-auto tweetExp2 center"
          color="black"
          dark
          max-width="550"
        >
          <v-card-title>
            <v-icon large left>
              mdi-twitter
            </v-icon>
            <span class="title font-weight-light">Twitter</span>
          </v-card-title>

          <v-card-text class="headline font-weight-bold">
            @ConnectMeWith_ circulates educational texts/articles & promotes
            collective care efforts to those who are lifelong learners by
            uplifting marginalized communities through group conversations.
          </v-card-text>
        </v-card>
        <v-card class="card3" max-width="600px">
          <v-card-text>
            <div>COnversations</div>
            <p class="display-1 text--primary">
              on
            </p>
            <div class="text--primary">
              -Black Lives Matter<br />
              -8 de Marzo<br />
              -Climate Change<br />
              -and more<br />
            </div>
          </v-card-text>
        </v-card>
        <v-img class="imgExp2" src="../assets/4.png"></v-img>
      </v-container>
    </v-parallax>
    <v-parallax
      style="height: 500px; width: 150%; margin-left: -5%"
      src="https://thebodyisnotanapology.com/wp-content/uploads/2015/01/tumblr_static_a-better-world-is-possible_copy.png"
    >
      <v-container style="margin-top: -23%">
        <v-card
          class="mx-auto tweetExp3 center"
          color="#6CCFF6"
          dark
          max-width="700"
        >
          <v-card-title>
            <v-icon large left>
              mdi-twitter
            </v-icon>
            <span class="title font-weight-light">Twitter</span>
          </v-card-title>
          <v-card-text class="headline font-weight-bold">
            Twitter offers a community of needed conversation, and
            @ConnectMeWith_ encourages social good efforts. It's time to have a
            conversation, start using @ConnectMeWith_ today.
          </v-card-text>
        </v-card>
        <v-img class="imgExp3" src="../assets/8.png"></v-img>
      </v-container>
    </v-parallax>
    <v-btn class="invite">Try it out now!</v-btn>
  </v-container>
</template>

<script>
export default {
  name: "Instructions",
  index: 0,
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
    };
  },
  components: {},
  computed: {
    changeIndex: function() {
      return Math.floor(Math.random() * this.topics.length);
    },
  },
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
.imgExp {
  height: 400px;
  width: 400px;
  right: 12%;
  position: absolute;
  z-index: 3;
}
.tweetExp {
  height: 240px;
  width: 700px;
  left: 15%;
  position: absolute;
  padding: 1%;
  top: auto;
  z-index: 3;
}
.card2 {
  left: 3%;
  position: absolute;
  z-index: 3;
}
.imgExp2 {
  height: 300px;
  width: 300px;
  left: 5%;
  position: absolute;
  z-index: 3;
}
.tweetExp2 {
  height: 260px;
  width: 700px;
  right: 26%;
  position: absolute;
  padding: 1%;
  z-index: 3;
}
.card3 {
  right: 10%;
  position: absolute;
  z-index: 3;
}
.imgExp3 {
  height: 300px;
  width: 300px;
  right: 15%;
  position: absolute;
  z-index: 3;
}
.tweetExp3 {
  height: 260px;
  width: 800px;
  left: 5%;
  position: absolute;
  padding: 1%;
  z-index: 3;
}
.bannerTop {
  height: 100%;
  width: 41%;
  position: absolute;
  background-color: black;
  right: -2%;
  top: -2%;
}
</style>
