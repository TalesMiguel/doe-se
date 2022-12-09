<template>
  <div align="center">
  <v-row>
    <v-col class="my-7">
      <avatarinst/>
    </v-col>
    <v-col>
      <v-card color="#c3c3c3" align="center" width="72vw">
        <v-container class="mx-5 my-7" fluid>
          <v-text-field required  
              v-model="enderecoAcao" label="Endereço" style="width:60vw" outlined filled background-color="#f6f6f6">
          </v-text-field>
          <v-row class="mb-3">
            <v-icon color="green" size="60">mdi-food-apple</v-icon>
            <v-checkbox v-model="tipoAcao" label="Comida" value="comida"></v-checkbox>
          </v-row>
          <v-row class="mb-3">
            <v-icon color="blue" size="60">mdi-hanger</v-icon>
            <v-checkbox v-model="tipoAcao" label="Roupas" value="roupas"></v-checkbox>
          </v-row>
          <v-row class="mb-3">
            <v-icon color="red" size="60">mdi-hand-heart</v-icon>
            <v-checkbox v-model="tipoAcao" label="Ajuda" value="ajuda"></v-checkbox>
          </v-row>
          <v-btn color="#c6535f" @click="salvar_acao">Salvar</v-btn>
        </v-container>
      </v-card>
    </v-col>
  </v-row>
  </div>
</template>
<script>
import avatarinst from './avatar-inst.vue'
export default {
  name: 'nova-acao',
  layout: 'navbar',
  components: {
    avatarinst
  },
  data () {
    return {
      tipoAcao: [],
      enderecoAcao: '',
      textoErro: "Aldo deu errado:",
      pronto: false,
      falhou: false,
    }
  },
  methods: {
    salvar_acao () {
      if(this.tipoAcao.length && this.enderecoAcao.length){
        const formAcao = new FormData()
        formAcao.append('endereco', this.enderecoAcao)
        this.tipoAcao.forEach((item) => formAcao.append('tipo', '{'+item+'}'))
        //let currentDate = new Date()
        //let data = currentDate.getTime()/1000
        //formAcao.append('timestamp', data)
        formAcao.append('concluido', "false")
        this.$axios.post('add-acao/', formAcao)
        .then(async (mens) => {
            console.log(mens)
             })
        .catch(async (err) => { 
            console.log(err)
             }) 
      } else{
        if(!this.tipoAcao.length) this.textoErro += "\ntipo de ação nao escolhida"
        if(!this.enderecoAcao.length) this.textoErro += "\nEndereço não preenchido"
          window.alert(this.textoErro)
            this.textoErro = "Aldo deu errado:"
      }
    }
  }
}
</script>
