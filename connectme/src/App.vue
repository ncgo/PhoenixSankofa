<template>
  <v-app style="font-family: 'Staatliches';">
    <span>
      <v-navigation-drawer
        app
        v-model="drawer"
        class="lighten-2"
        color="#1FA1F2"
        dark
        disable-resize-watcher
      >
        <v-list>
          <template v-for="(item, index) in items">
            <v-list-item :key="index">
              <v-list-item-content>
                {{ item.title }}
              </v-list-item-content>
            </v-list-item>
            <v-divider :key="`divider-${index}`"></v-divider>
          </template>
        </v-list>
      </v-navigation-drawer>
      <v-app-bar color="#1FA1F2" dark fixed>
        <v-app-bar-nav-icon class="hidden-md-and-up" @click="drawer = !drawer">
        </v-app-bar-nav-icon>
        <v-icon @click="$router.push('/')">mdi-link-variant</v-icon>
        <v-toolbar-title class="mr-1 myTitle" @click="$router.push('/')">{{
          appTitle
        }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn
          class="hidden-sm-and-down mr-3"
          color="#E0193D"
          @click="$router.push('/about')"
          >ABOUT US
        </v-btn>
        <v-btn
          class="hidden-sm-and-down mr-3"
          color="#E0193D"
          @click="$router.push('/data')"
          >DATA
        </v-btn>
        <v-btn color="#6CCFF6 lighten-3" @click="tryItOut">TRY IT OUT</v-btn>
      </v-app-bar>
    </span>
    <v-main>
      <router-view></router-view>
    </v-main>
    <v-card height="400px">
      <v-footer padless fixed>
        <v-card flat tile width="100%" class="blue lighten-1 text-center">
          <v-card-text>
            <v-btn v-for="icon in icons" :key="icon" class="mx-4" icon>
              <v-icon size="24px" color="white">{{ icon }}</v-icon>
            </v-btn>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-text class="white--text">
            {{ new Date().getFullYear() }} —
            <strong>Team Phoenix Sankofa</strong>
          </v-card-text>
        </v-card>
      </v-footer>
    </v-card>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      appTitle: "ConnectMeWith",
      drawer: false,
      items: [
        { title: "MENU" },
        { title: "ABOUT" },
        { title: "MEET THE TEAM" }
      ],
      icons: ["mdi-home", "mdi-twitter", "mdi-twitter-retweet", "mdi-heart"],
      padless: false,
      variant: "fixed"
    };
  },
  methods: {
    tryItOut() {
      window.open(
        "https://twitter.com/intent/tweet?text=@ConnectMeWith_%20blm",
        "_blank"
      );
    }
  }
};
</script>
