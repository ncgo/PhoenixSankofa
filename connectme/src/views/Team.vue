<template>
  <span>
    <div>
    <v-img class="mt-10" src="../assets/team.png">
    </v-img></div>
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
