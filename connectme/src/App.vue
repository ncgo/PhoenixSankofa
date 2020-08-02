<template>
  <v-app style="font-family: 'Staatliches';">
    <span>
      <v-navigation-drawer
        app
        v-model="drawer"
        class="lighten-2"
        color="#E0193D"
        dark
        disable-resize-watcher
      >
        <v-list>
          <template v-for="(item, index) in items">
            <v-list-item :key="index" :to="item.link">
              <v-list-item-content>
                {{ item.title }}
              </v-list-item-content>
            </v-list-item>
            <v-divider :key="`divider-${index}`"></v-divider>
          </template>
        </v-list>
      </v-navigation-drawer>
      <v-app-bar color="blue" dark fixed>
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
          >ABOUT
        </v-btn>
        <v-btn
          class="hidden-sm-and-down mr-3"
          color="#E0193D"
          @click="$router.push('/data')"
          >DATA
        </v-btn>
        <v-btn
          class="hidden-sm-and-down mr-3"
          color="#E0193D"
          @click="$router.push('/documentation')"
          >DOCUMENTATION
        </v-btn>
        <v-btn
          class="hidden-sm-and-down mr-3"
          color="#E0193D"
          @click="$router.push('/team')"
          >MEET THE TEAM
        </v-btn>
        <v-btn color="#6CCFF6 lighten-3" @click="tryItOut">TRY IT OUT</v-btn>
      </v-app-bar>
    </span>
    <v-main>
      <router-view></router-view>
    </v-main>
    <v-footer dark padless fixed>
      <v-card class="flex" flat tile>
        <v-card-title class="blue">
          <strong class="subheading">Made with love and power</strong>
          <v-spacer></v-spacer>
          <v-btn
            v-for="icon in icons"
            :key="icon.title"
            :to="icon.link"
            class="mx-4"
            dark
            icon
          >
            <v-icon size="24px">{{ icon.icon }}</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text class="py-2 red--text text-center">
          {{ new Date().getFullYear() }} —
          <strong> Team Phoenix Sankofa</strong>
        </v-card-text>
      </v-card>
    </v-footer>
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
        { title: "HOME", link: "/home" },
        { title: "ABOUT", link: "/about" },
        { title: "MEET THE TEAM", link: "/team" },
        { title: "DATA VISUALIZATION", link: "/data" }
      ],
      icons: [
        { title: "Home", icon: "mdi-home", link: "/home" },
        {
          title: "Twitter",
          icon: "mdi-twitter",
          link: "/twitterAccount"
        },
        {
          title: "Try",
          icon: "mdi-twitter-retweet",
          link: "/TryItOut"
        },
        { title: "like", icon: "mdi-heart", link: "/home" }
      ],
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
