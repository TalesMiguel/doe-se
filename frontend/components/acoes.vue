<template>
    <v-main>
        <v-row>
            <v-col cols="6" md="6">
                <v-card flat style="width:42vw;height:60vh" color="#d8d5d5" class="d-flex justify-center">
                    <v-container>
                    <v-card-title class="d-flex justify-center"> Criar ação </v-card-title>
                    <v-card-actions class="justify-center my-6">
                        <v-form ref="form">
                            <v-text-field required :rules="[v => !!v || 'Name is required']"
                                v-model="nome" label="Nome" style="width:30vw" outlined filled background-color="#f6f6f6">
                            </v-text-field>

                            <v-select required multiple chips deletable-chips :rules="[v => !!v || 'Item is required']" 
                                v-model="tipo" :items="itens" label="Tipo" style="width:30vw" outlined filled background-color="#f6f6f6">
                            </v-select>

                            <v-text-field required :rules="[v => !!v || 'Item is required']" 
                                v-model="endereco" label="Endereço" style="width:30vw" outlined filled background-color="#f6f6f6">
                            </v-text-field>

                            <v-row>
                                <v-col>
                                    <v-text-field required :rules="[v => !!v || 'Item is required']" 
                                        v-model="inicio" label="Data de início" type="date" outlined filled background-color="#f6f6f6">
                                    </v-text-field>
                                </v-col>
                                <v-col>
                                    <v-text-field required :rules="[v => !!v || 'Item is required']" 
                                        v-model="fim" label="Data de fim" type="date" outlined filled background-color="#f6f6f6">
                                    </v-text-field>
                                </v-col>
                            </v-row>

                        </v-form>
                    </v-card-actions>
                    <v-row>
                        <v-col md="12" class="d-flex justify-center">
                            <v-btn @click="enviar" style="width:10vw" color="green"> Criar </v-btn>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col md="12" class="d-flex justify-center">
                        <p v-if="pronto" class="mt-4" style="color:green;font-size:20px">Enviado!</p>
                        <p v-if="falhou" class="mt-4" style="color:red;font-size:20px">Falhou.</p>
                        </v-col>
                    </v-row>
                    </v-container>
                </v-card>
            </v-col>
            <v-col cols="6" md="6">
                <v-card flat style="width:44vw;height:60vh" color="#d8d5d5" class="d-flex justify-center">
                    <v-container>
                        <v-card-title class="d-flex justify-center"> Ações criadas </v-card-title>
                        <v-container fluid style="height:50vh" class="d-flex align-center justify-center">
                          <v-virtual-scroll v-if="acoes != null" :items="acoes" item-height="64">
                            <template v-slot:default="{ item }">
                              <v-list-item :key="item">
                                <v-list-item-content>
                                  <v-list-item-title>
                                    <strong>{{ item.nome }}</strong>
                                  </v-list-item-title>
                                  {{item.endereco}}, {{item.inicio}}
                                </v-list-item-content>
                                <v-list-item-action>
                                  <v-icon small>
                                    mdi-close
                                  </v-icon>
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
  mounted() {
    this.get()
  },
  methods: {
        enviar() 
        {
            if(this.$refs.form.validate()){ 
                const formAcao = new FormData()
                formAcao.append('nome', this.nome)
                formAcao.append('tipo', '{' + this.tipo + '}')
                formAcao.append('endereco', this.endereco)
                this.$axios.post('add-acao/', formAcao)
                .then(async (mens) => { this.$refs.form.reset(); this.pronto = true; 
                    await new Promise(r => setTimeout(r, 2000)); this.pronto = false })
                .catch(async (err) => { this.$refs.form.reset(); this.falhou = true;
                    await new Promise(r => setTimeout(r, 2000)); this.falhou = false }) 
            }
        },

        get() {
            this.$axios.get('get-acao/')
                .then(async (mens) => { this.acoes = (mens.data.acoes); console.log(mens.data.acoes)})
                .catch(async (err) => { console.log("Erro " + err)} )
        },

        converte() 
        {
            var s = this.inicio
            var arr = s.split('-')
            var novo = ""

            var i = 0

            for(i = 0; i < 2; i++)
            {
                novo += arr[i] + '.'
            }

            novo += arr[2]

            console.log(novo)
        },
  },
  data() {
    return {
        nome: '',
        tipo: null,
        endereco: '',
        inicio: '',
        fim: '',
        itens: [
            'Roupa',
            'Comida',
            'Trabalho',
        ],
        pronto: false,
        falhou: false,
        acoes: null,
    }
  }
}
</script>
