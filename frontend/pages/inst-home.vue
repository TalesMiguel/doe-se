<template>
  <v-container fluid class="my-16">
    <v-card flat>
      <v-img class="text aling-end" :src="image3" max-height="15vh">
        <h1 align="left" style="color:#F08080">{{instname}}</h1>
        <div align="center">
          <v-toolbar color="#d3d3d3" flat max-width="1000" min-width="500">
            <v-tabs
              background-color="#d3d3d3" max-height="30"
              v-model="opcoes_inst" fixed-tabs slider-color="#FF5757"
            >
              <v-tab v-for="opcao in opcoes" :key="opcao" style="color: #000">
                {{ opcao }}
              </v-tab>
            </v-tabs>
          </v-toolbar>
        </div>
      </v-img>
    </v-card>
    <v-tabs-items v-model="opcoes_inst" id="tab-item-custom" class="my-4">
      <v-tab-item>
        <v-row>
          <v-col>
            <avatarinst/>
          </v-col>
          <v-col>
            <v-card flat width="72vw" color="#d3d3d3" tile>
            </v-card>
          </v-col>
        </v-row>
      </v-tab-item>
      <v-tab-item>
        <fixacadastroinst/>
      </v-tab-item>
      <v-tab-item>
        <novapublicacao/>
      </v-tab-item>
      <v-tab-item>
        <novaacao/>
      </v-tab-item>
    </v-tabs-items>
  </v-container>
</template>

<script>
import avatarinst from '../components/avatar-inst.vue'
import fixacadastroinst from '../components/tab-dados.vue'
import novapublicacao from '../components/tab-nova-publicacao.vue'
import novaacao from '../components/tab-nova-acao.vue'

export default {
  name: 'inst-home',
  layout: 'navbar',
  components: {
    avatarinst,
    fixacadastroinst,
    novapublicacao,
    novaacao
  },
  data: function () {
    return {
      instname: 'place holder',
      opcoes_inst: null,
      image3: require('../assets/imagem-3.jpg'),
      opcoes: ['publicações', 'dados cadastrais', 'nova publicação', 'nova ação', 'notificações', 'ajuda']
    }
  }
}
</script>

<style>
#tab-item-custom {
  background-color: transparent !important;
}

.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>
