<template>
  <div class="center" align="center">
    <v-card
      elevation="10"
      color="#F6E2E2"
      width="600"
      height="500"
      >
      <v-card-text class="justify-center">
        <h1 style="color:#000000" class="mt-3">Bem vindo!</h1>
      </v-card-text>
      <div class="center" align="center">
        <v-card
          elevation="0"
          color="#c6535f"
          outlined
          width="400"
        >
          <v-card-text class="justify-center"><h2 style="color:#f4f4f4">Login</h2></v-card-text>
          <div align="left">
            <v-container>
              <v-text-field solo filled outlined flat label="E-mail">
              </v-text-field>
              <v-text-field solo filled outlined flat label="Senha" type="password">
              </v-text-field>
            </v-container>
          </div>
          <div align="right">
            <v-btn
              depressed
              large
              color="#d8d5d5"
              class="mb-4 mr-6 font-weight-light"
            >Entrar</v-btn>
          </div>
          <div align="center">
            <v-btn
              text
              color="#f4f4f4"
              class="mb-2"
              @click="cadastrar"
            >É novo, Cadastre-se aqui</v-btn>
          </div>
        </v-card>
      </div>
    </v-card>
 </div>
</template>

<script>
export default {
  name: 'Login-Usuario',
  layout: 'navbar',
  methods: {
    cadastrar () {
      this.$router.push('./cadastro-usuario')
    }
  }
}
</script>

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
