<template>
    <v-main>
        <v-container class="mx-16 my-12">
            <v-row style="height:4vw">
                <v-col md="5"></v-col>
                <v-col>
                    <h1> Digite uma ação </h1>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="2" md="2"></v-col>
                <v-col cols="10" md="10" align-self="center">
                    <v-card flat style="width:60vw;height:60vh" color="#d8d5d5" class="d-flex align-center justify-center">
                        <v-container>
                        <v-card-actions class="justify-center my-6">
                            <v-form ref="form">
                                <v-text-field v-model="nome" label="Nome da Instituição" style="width:30vw" outlined filled background-color="#f6f6f6">
                                </v-text-field>

                                <v-select v-model="tipo" :items="itens" label="Tipo" style="width:30vw" outlined filled background-color="#f6f6f6">
                                </v-select>

                                <v-text-field v-model="endereco" label="Endereço" style="width:30vw" outlined filled background-color="#f6f6f6">
                                </v-text-field>
                            </v-form>
                        </v-card-actions>
                        <v-row>
                        <v-col md="12" class="d-flex justify-center">
                        <v-btn @click="enviar" style="width:10vw"> Enviar </v-btn>
                         </v-col>
                        </v-row>
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
        enviar() { 
            console.log(res)
        },
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
    }
  }
}
</script>