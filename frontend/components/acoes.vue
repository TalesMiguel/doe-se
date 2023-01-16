<template>
  <v-main>
    <v-row>
      <v-col
        cols="6"
        md="6"
      >
        <v-card
          flat
          style="width:42vw;height:60vh"
          color="#d8d5d5"
          class="d-flex justify-center"
        >
          <v-container>
            <v-card-title class="d-flex justify-center">
              Criar ação
            </v-card-title>
            <v-card-actions class="justify-center my-6">
              <v-form ref="form">
                <v-text-field
                  v-model="nome"
                  required
                  :rules="[v => !!v || 'Name is required']"
                  label="Nome"
                  style="width:30vw"
                  outlined
                  filled
                  background-color="#f6f6f6"
                />

                <v-select
                  v-model="tipo"
                  required
                  multiple
                  chips
                  deletable-chips
                  :rules="[v => !!v || 'Item is required']"
                  :items="itens"
                  label="Tipo"
                  style="width:30vw"
                  outlined
                  filled
                  background-color="#f6f6f6"
                />

                <v-text-field
                  v-model="endereco"
                  required
                  :rules="[v => !!v || 'Item is required']"
                  label="Endereço"
                  style="width:30vw"
                  outlined
                  filled
                  background-color="#f6f6f6"
                />

              </v-form>
            </v-card-actions>
            <v-row>
              <v-col
                md="12"
                class="d-flex justify-center"
              >
                <v-btn
                  style="width:10vw"
                  color="green"
                  @click="enviar"
                >
                  Criar
                </v-btn>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                md="12"
                class="d-flex justify-center"
              >
                <p
                  v-if="pronto"
                  class="mt-4"
                  style="color:green;font-size:20px"
                >
                  Enviado!
                </p>
                <p
                  v-if="falhou"
                  class="mt-4"
                  style="color:red;font-size:20px"
                >
                  Falhou.
                </p>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
      <v-col
        cols="6"
        md="6"
      >
        <v-card
          flat
          style="width:44vw;height:60vh"
          color="#d8d5d5"
          class="d-flex justify-center"
        >
          <v-container>
            <v-card-title class="d-flex justify-center">
              Ações criadas
            </v-card-title>
            <v-container
              fluid
              style="height:50vh"
              class="d-flex align-center justify-center"
            >
              <v-virtual-scroll
                v-if="acoes != null"
                :items="acoes"
                item-height="96"
              >
                <template #default="{ item }">
                  <v-list-item :key="item">
                    <v-list-item-content>
                      <v-list-item-title>
                        <h3>
                          <strong>{{ item.nome }}</strong>
                        </h3>
                      </v-list-item-title>
                      Endereço: {{ item.endereco }}
                      <br>
                      Tipo da Doação: {{ item.tipo }}
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-btn small
                        icon
                        mdi-close
                        color="red"
                        @click="deletar(item)"
                      > <v-icon>mdi-close</v-icon>
                      </v-btn>
                    </v-list-item-action>
                  </v-list-item>
                </template>
              </v-virtual-scroll>
            </v-container>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-main>
</template>

<script>
export default {
  name: 'IndexPage',
  layout: 'navbar',
  mounted () {
    this.get()
  },
  methods: {
    enviar () {
      if (this.$refs.form.validate()) {
        const formAcao = new FormData()
        formAcao.append('nome', this.nome)
        formAcao.append('tipo', '{' + this.tipo + '}')
        formAcao.append('endereco', this.endereco)
        this.$axios.post('add-acao/', formAcao)
          .then(async () => {
            this.$refs.form.reset(); this.pronto = true
            await new Promise(r => setTimeout(r, 2000)); this.pronto = false
          })
          .catch(async () => {
            this.$refs.form.reset(); this.falhou = true
            await new Promise(r => setTimeout(r, 2000)); this.falhou = false
          })
      }
    },

    deletar (acao) {
      this.$axios.post('delete-acao/', acao)
        .then(async () => {
          this.$refs.form.reset(); this.pronto = true
          await new Promise(r => setTimeout(r, 2000)); this.pronto = false
        })
        .catch(async () => {
          this.$refs.form.reset(); this.falhou = true
          await new Promise(r => setTimeout(r, 2000)); this.falhou = false
        })
    },

    editar (acao) {
      this.$axios.post('edit-acao/', acao)
        .then(async () => {
          this.$refs.form.reset(); this.pronto = true
          await new Promise(r => setTimeout(r, 2000)); this.pronto = false
        })
        .catch(async () => {
          this.$refs.form.reset(); this.falhou = true
          await new Promise(r => setTimeout(r, 2000)); this.falhou = false
        })
    },

    get () {
      this.$axios.get('get-acao/')
        .then(async (mens) => { this.acoes = (mens.data.acoes); console.log(mens.data.acoes) })
        .catch(async (err) => { console.log('Erro ' + err) })
    },
  },
  data () {
    return {
      nome: '',
      tipo: null,
      endereco: '',
      itens: [
        'Roupa',
        'Comida',
        'Trabalho'
      ],
      pronto: false,
      falhou: false,
      acoes: null
    }
  }
}
</script>
