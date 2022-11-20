<template>
  <v-app>
   <v-app-bar
      color='#f6e2e2'
      fixed
      app
      flat
      height="70vh"
      class="px-6"
    >

      <v-btn text class="mr-4" @click="home">
        <v-toolbar-title>
        <div style="font-size:25pt" class="mr-4 font-weight-bold">
          Doe-se
        </div>
        </v-toolbar-title>

        <v-icon color="red" large> mdi-heart </v-icon>

      </v-btn>

      <v-spacer />

      <v-container>

        <v-row>
          <v-spacer />
          <v-btn color="#d8d5d5" class="my-8 mx-6 font-weight-light" style="min-width:14vh" depressed @click="quem">
            Quem Somos
          </v-btn>

          <v-btn color="#d8d5d5" class="my-8 mx-6 font-weight-light" style="min-width:14vh" depressed @click="contato">
            Contato
          </v-btn>

          <v-btn color="#d8d5d5" class="my-8 mx-6 font-weight-light" depressed @click="loginInstituicao">
            Espaço para Instituições
          </v-btn>

          <v-btn rounded color="#c6535f" class="my-8 mx-6" style="min-width:14vh">
            <v-toolbar-title>
              <div style="color:#f4f4f4;font-size:9pt">
                Quero Doar
              </div>
            </v-toolbar-title>
          </v-btn>

          <v-menu
            bottom
            min-width="100px"
            offset-y
          >

            <template v-slot:activator="{ on }">
              <v-btn
                icon
                x-large
                v-on="on"
                class="my-6 ml-6"
              >
                <v-avatar
                  color="#d8d5d5"
                  size="56"
                >
                  <v-icon> mdi-account </v-icon>
                </v-avatar>
              </v-btn>
            </template>

            <v-card
              color="#e9eaeb"
            >
              <v-list-item-content class="justify-center">
                <div class="text-center">
                  <v-btn
                    text
                    class="font-weight-light"
                    @click="entrar"
                  >
                    Entrar
                  </v-btn>

                  <v-divider class="my-3"></v-divider>

                  <v-btn
                    text
                    class="font-weight-light" @click="cadastrarUsuario"
                  >
                    Cadastre-se
                  </v-btn>
                </div>
              </v-list-item-content>
            </v-card>
        </v-menu>

        </v-row>
      </v-container>

      <v-spacer />

    </v-app-bar>

    <v-footer
      app
    >
      <span> &copy; {{ new Date().getFullYear() }} </span>
    </v-footer>

    <Nuxt />

  </v-app>
</template>

<script>
export default {
  name: 'NavbarLayout',
  methods: {
    home () {
      this.$router.push('./')
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
      })
    },
    entrar () {
      this.$router.push('./login-usuario')
    },
    quem () {
      this.home()
      window.scrollTo({
        top: 840,
        left: 0,
        behavior: 'smooth'
      })
    },
    contato () {
      this.home()
      window.scrollTo({
        top: 1700,
        left: 0,
        behavior: 'smooth'
      })
    },
    cadastrarUsuario () {
      this.$router.push('./cadastro-usuario')
    },
    loginInstituicao () {
      this.$router.push('./login-instituicao')
    }
  }
}
</script>

<style scoped>
  .v-application {
    background-color: #f4f4f4;
  }
</style>
