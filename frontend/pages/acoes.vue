<template>
    <v-main>
        <v-container class="mx-16 my-12">
            <v-row style="height:10vh">
            </v-row>
            <v-row>
                <v-col cols="5" md="5">
                    <v-card flat style="width:35vw;height:60vh" color="#d8d5d5" class="d-flex align-center justify-center">
                        <v-container>
                        <v-card-title class="d-flex justify-center"> Digite uma ação </v-card-title>
                        <v-card-actions class="justify-center my-6">
                            <v-form ref="form">
                                <v-text-field required :rules="[v => !!v || 'Name is required']"
                                    v-model="nome" label="Nome da Instituição" style="width:30vw" outlined filled background-color="#f6f6f6">
                                </v-text-field>

                                <v-select required multiple chips deletable-chips :rules="[v => !!v || 'Item is required']" 
                                    v-model="tipo" :items="itens" label="Tipo" style="width:30vw" outlined filled background-color="#f6f6f6">
                                </v-select>

                                <v-text-field required :rules="[v => !!v || 'Item is required']" 
                                    v-model="endereco" label="Endereço" style="width:30vw" outlined filled background-color="#f6f6f6">
                                </v-text-field>
                            </v-form>
                        </v-card-actions>
                        <v-row>
                            <v-col md="12" class="d-flex justify-center">
                                <v-btn @click="enviar" style="width:10vw"> Enviar </v-btn>
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
                <v-col cols="7" md="7">
                    <v-card flat style="width:55vw;height:60vh" color="#d8d5d5" class="d-flex justify-center">
                        <v-container>
                            <v-card-title class="d-flex justify-center"> Lista de ações </v-card-title>
                            <v-container fluid style="height:50vh" class="d-flex align-center justify-center">
                            <v-card-actions v-for="(acao,i) in acoes" :key="i" class="d-flex align-center justify-center my-6">
                                <p>Nome da Instituição: {{ acao.nome }}
                                <br><br>Tipo: {{ acao.tipo }}
                                <br><br>Endereço: {{ acao.endereco }}
                                </p>
                                <v-col style="width:5vw"></v-col>
                            </v-card-actions>
                            </v-container>
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
  mounted() {
    this.get()
  },
  methods: {
        enviar() {
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
                .then(async (mens) => { this.acoes = (mens.data.todos); console.log(mens.data.todos)})
                .catch(async (err) => { console.log("Erro " + err)} )
        }
  },
  data() {
    return {
        nome: '',
        tipo: null,
        endereco: '',
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