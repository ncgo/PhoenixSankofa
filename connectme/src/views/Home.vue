<template>
  <span>
    <div class="bannerTop"></div>
    <v-parallax
      dark
      style="height: 100%"
      src="https://cdn.pixabay.com/photo/2020/06/11/09/37/black-lives-matter-5285956_1280.jpg"
    >
      <div class="bannerTop"></div>
      <v-card class=" topics" max-width="600px">
        <v-card-text>
          <div>#BlackLivesMatter</div>
          <p class="display-1 text--primary">
            black•lives•matter
          </p>
          <p>a movement</p>
          <div class="text--primary">
            <strong>99%</strong> of killings by police from 2013-2019<br />
            have not resulted in officers being charged with a crime
          </div>
        </v-card-text>
        <v-card-actions>
          <v-spacer> </v-spacer>
          <v-btn text color="red accent-4" @click="learnMore">
            Learn More
          </v-btn>
        </v-card-actions>
      </v-card>
      <v-card class="mx-auto card" color="#E0193D" dark width="490px">
        <v-card-title>
          <v-icon large left>
            mdi-twitter
          </v-icon>
          <span class="title font-weight-light">Twitter</span>
        </v-card-title>

        <v-card-text class="headline font-weight-bold">
          @ConnectMeWith_ #BlackLivesMatter
        </v-card-text>

        <v-card-actions>
          <v-list-item class="grow">
            <v-list-item-avatar color="black">
              <v-icon>mdi-link-variant</v-icon>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>Phoenix Sankofa</v-list-item-title>
            </v-list-item-content>

            <v-row align="center" justify="end">
              <v-icon class="mr-1">mdi-heart</v-icon>
              <span class="subheading mr-2">256</span>
              <span class="mr-1">·</span>
              <v-icon class="mr-1">mdi-twitter-retweet</v-icon>
              <span class="subheading">45</span>
            </v-row>
          </v-list-item>
        </v-card-actions>
      </v-card>
      <v-row>
        <div id="titleTop">
          <h2>IT'S TIME TO HAVE A CONVERSATION</h2>
          <v-btn @click="tryItOut"> @ConnectMeWith</v-btn><br />
          <v-btn color="red" @click="$router.push('about')">
            Learn More
          </v-btn>
        </div>
      </v-row>
    </v-parallax>
    <v-row style="position: absolute; top:650px; width: 100%">
      <router-view> </router-view>
    </v-row>
  </span>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  next: false,
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
#textInfo {
  font-family: "Times New Roman";
  text-decoration: bold;
}
#slogan {
  position: absolute;
  text-align: right;
  margin-top: 100px;
}
.card {
  top: 280px;
  margin-left: 5%;
  position: absolute;
}
.bannerTop {
  padding: 3%;
  height: 100%;
  width: 40%;
  position: absolute;
  background-color: black;
  right: 0%;
}
.topics {
  position: absolute;
  left: 22%;
  top: 100px;
  margin-right: 5%;
}
#presentation {
  height: 350px;
  width: 50%;
  position: absolute;
  background-color: black;
  text-align: right;
}
#titleTop {
  position: absolute;
  right: 2%;
  top: 300px;
  color: yellow;
  font-size: 40px;
  width: 400px;
  text-align: right;
  line-height: 150%;
  margin-left: -20px;
}
#titlePage {
  background-color: #98ce00;
  color: white;
  font-size: 40px;
  width: 400px;
  text-align: right;
  line-height: 150%;
  padding: 3%;
}
.imgExp {
  height: 400px;
  width: 400px;
  left: 43%;
  top: -30%;
}
.tweetExp {
  position: absolute;
  height: 400px;
  width: 400px;
  left: 0%;
}
@media only screen and (max-width: 960px) and (min-width: 76px) {
  .bannerTop {
    height: 100%;
    position: absolute;
    left: 0%;
    width: 50%;
  }
  .card {
    margin-top: 250px;
    margin-left: 20%;
    top: 8%;
    position: absolute;
  }
  .topics {
    position: absolute;
    left: 45%;
    top: 15%;
    margin-right: 5%;
  }
  #titleTop {
    position: absolute;
    left: 5%;
    top: 20%;
    margin-right: 5%;
    color: yellow;
    font-size: 20px;
    width: 30%;
    text-align: right;
    line-height: 150%;
  }
}
</style>
