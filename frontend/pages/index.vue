<template>
    <v-main>
      <v-container fluid style="height: 250vh" class="mx-16 my-12">
        <v-row justify="left" class="ml-14 mt-8">
          <v-col md="1"> </v-col>
          <v-col md="7" align="center">
            <div style="height: 8vh">
            <p style="font-size: 28px"> Encontre projetos sociais próximos a você!</p>
            </div>
            <v-autocomplete
              v-model="select"
              :loading="loading"
              :items="items"
              :search-input.sync="search"
              cache-items
              flat
              hide-no-data
              hide-details
              label="Digite seu endereço"
              filled
              class="d-flex justify-end mb-6"
            ></v-autocomplete>
          </v-col>
          <v-col>
            <v-btn rounded class="mx-6 my-15" style="min-width:14vh" color="#c6535f">
              <div style="color:#f4f4f4;font-size:13px"> Buscar </div> </v-btn> </v-col>
        </v-row>
        <v-row justify="left" class="ml-4 mt-8" style="height: 62vh">
          <v-col md="6" align="center">
            <h1 style="font-size: 56px"> Quem você quer <br>
            ajudar hoje? </h1>
            <p style="font-size: 32px" class="font-weight-light mt-4"> A Doe-se oferece uma nova<br>
            maneira de engajar nos<br>
            projetos sociais mais<br>
            próximos de você!</p>
          </v-col>
          <v-col md="1">
          </v-col>
          <v-col md="4" justify="center">
            <v-card flat style="max-width: 65vh" color="#f6e2e2" class="mt-4">
              <v-card-title class="justify-center"> <h1 class="font-size: 48px my-8">
                  Faça sua doação
              </h1> </v-card-title>
              <v-card-actions class="justify-center">
                <v-btn color="#c6535f" style="min-width: 16vh" class="mb-6">
                  <div style="font-size:13px;color:#f4f4f4">
                    Doação Única
                  </div>
                </v-btn>
              </v-card-actions>
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
          </v-col>
        </v-row>
        <v-divider style="max-width: 92vw"> </v-divider>

        <v-row class="ma-10" style="height:75vh">
          <v-col md="5" align="center">
            <h2 style="font-size: 56px"> Quem somos? </h2>
            <p style="font-size: 30px" align="center" class="font-weight-light mt-4">
            Aqui na Doe-se temos como objetivo fortalecer
            a generosidade e a cultura de doação.<br> <br>

            Juntos, com sua participação, construimos um futuro melhor
            entre o setor social, pessoas e empresas.</p>
          </v-col>
          <v-col md="1"> </v-col>
          <v-col align-self="center">
            <v-card style="max-width:41vw" height="56vh" color="#f4f4f4" elevation="4">
              <v-card-actions class="justify-center">
            <v-img
              max-height="54vh"
              max-width="40vw"
              src="https://images.unsplash.com/photo-1579208570378-8c970854bc23?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1222&q=80">
            </v-img>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-divider style="max-width: 92vw"> </v-divider>

        <v-row justify="left" class="mx-10" style="height: 80vh">
          <v-col md="5" align="center">
            <h3 style="font-size: 50px" align="center"> Fale conosco! </h3>
            <p style="font-size: 30px" align="center" class="font-weight-light mt-4">
              Tem alguma pergunta ou gostaria <br>
              de nos conhecer melhor? Contate-Nos!</p>
          </v-col>
          <v-col md="1"> </v-col>
          <v-col md="5" align-self="center">
            <v-card style="max-width:125vw" height="63vh" color="#f6e2e2">
              <v-form>
                <v-container fluid>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="6"
                    >
                      <v-text-field maxlength='100'
                        v-model="first"
                        label="Nome"
                        outlined
                        solo
                        flat
                      ></v-text-field>
                    </v-col>

                    <v-col
                      cols="12"
                      sm="6"
                    >
                      <v-text-field maxlength='100'
                        v-model="first"
                        label="E-mail"
                        outlined
                        solo
                        flat
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-form>
              <v-form>
                <v-container fluid>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="12"
                    >
                      <v-text-field maxlength='60'
                        v-model="first"
                        label="Assunto"
                        outlined
                        solo
                        flat
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-form>
              <v-container fluid>
                <v-textarea maxlength='200'
                  counter
                  outlined
                  solo
                  flat
                  label="Escreva sua mensagem"
                  auto-grow
                ></v-textarea>
                <v-btn block style="min-width:15vh" color="#c6535f">
                <div style="color:#f4f4f4;font-size:13px"> Enviar </div> </v-btn>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
</template>

<script>
export default {
  name: 'IndexPage',
  layout: 'navbar',
  methods: {
    entrar () {
      this.$router.push('./UserLogin')
    },
    cadastrarUsuario () {
      this.$router.push('./CadastroUsuario')
    }
  }
}
</script>
