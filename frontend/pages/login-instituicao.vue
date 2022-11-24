<template>
  <div class="center" align="center">
    <v-card
      elevation="10"
      color="#F6E2E2"
      outlined
      width="600"
      height="500"
      ><h1 style="color:#000">Bem vindo!</h1>
        <div class="center" align="center">
          <v-card
            elevation="0"
            color="#c6535f"
            outlined
            width="400"
          ><h2>Login</h2><div align="left">
            <v-container>
              <v-text-field outlined filled label="E-mail">
              </v-text-field>
              <v-text-field outlined filled label="Senha" type="password">
              </v-text-field>
            </v-container>
          </div>
          <div align="right">
           <v-btn
             elevation="0"
             large
             color="#d8d5d5"
             class="mr-2 mb-2"
           >Entrar</v-btn>
          </div>
          <div align="center">
            <v-btn
              text
              color="#000"
              @click="cadastrar"
           >Cadastre sua Instituição aqui</v-btn>
          </div>
          </v-card>
        </div>
    </v-card>
  </div>
</template>

<style>
.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>
<script>

export default {
  name: 'Login-Instituicao',
  layout: "navbar",
  methods: {
    cadastrar () {
      this.$router.push('./cadastro-instituicao')
    }
  }
}
</script>
