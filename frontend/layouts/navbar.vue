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

          <v-btn rounded color="#c6535f" class="my-8 mx-6" style="min-width:14vh" @click="dialog = true">
            <v-toolbar-title>
              <div style="color:#f4f4f4;font-size:9pt">
                Quero Doar
              </div>
            </v-toolbar-title>
          </v-btn>

        </v-row>
      </v-container>

    </v-app-bar>

    <v-dialog v-model="dialog" width="25vw">
      <v-card flat color="#d8d5d5" class="mt-4">
        <v-card-title class="justify-center"> <h1 class="font-size: 48px my-8">
            Faça sua doação
        </h1> </v-card-title>
        <v-card-actions class="justify-center">
          <v-btn color="#c6535f" style="min-width: 16vh" class="mb-6" @click="entrar">
            <div style="font-size:13px;color:#f4f4f4">
              Entrar
            </div>
          </v-btn>
        </v-card-actions>
        <v-card-actions class="justify-center">
            <v-btn color="#c6535f" style="min-width: 16vh" class="mb-10" @click="cadastrarUsuario">
            <div style="font-size:13px;color:#f4f4f4">
              Cadastre - se
            </div>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-footer app>
      <span> &copy; {{ new Date().getFullYear() }} </span>
    </v-footer>

    <Nuxt />

  </v-app>
</template>

<script>
export default {
  name: 'NavbarLayout',
  data() {
    return{
      dialog: false
    }
  },
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
      this.dialog = false
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
      this.dialog = false
      this.$router.push('./cadastro-usuario')
    },
    loginInstituicao () {
      this.$router.push('./login-instituicao')
    },
    explorar () {
      this.dialog = false
      this.$router.push('./explorar')
    }
  }
}
</script>

<style scoped>
  .v-application {
    background-color: #f4f4f4;
  }
</style>
