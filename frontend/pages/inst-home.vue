<template>
  <v-container class="mt-16">
    <v-row style="height: 10vh"> <v-col class="ma-5"> <h1> {{instname}} </h1> </v-col></v-row>
    <v-row>
    <v-card flat>
          <v-toolbar color="#d3d3d3" flat width="92vw" height="60vh">
            <v-tabs
              background-color="#d3d3d3"
              v-model="opcoes_inst" grow slider-color="#FF5757"
            >
              <v-tab v-for="opcao in opcoes" :key="opcao" style="color: black">
                {{ opcao }}
              </v-tab>
            </v-tabs>
          </v-toolbar>
    </v-card>
    </v-row>
    <v-tabs-items v-model="opcoes_inst" id="tab-item-custom" class="my-4">
      <v-tab-item>
        <v-row>
          <v-col>
            <avatarinst/>
          </v-col>
          <v-col>
            <v-card flat width="92vw" color="#d3d3d3" tile>
            </v-card>
          </v-col>
        </v-row>
      </v-tab-item>
      <v-tab-item>
        <fixacadastroinst/>
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
import novaacao from '../components/acoes.vue'

export default {
  name: 'inst-home',
  layout: 'navbar',
  components: {
    avatarinst,
    fixacadastroinst,
    novaacao
  },
  data: function () {
    return {
      instname: 'Nome',
      opcoes_inst: null,
      image3: require('../assets/imagem-3.jpg'),
      opcoes: ['atividades', 'dados cadastrais', 'ações', 'notificações']
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
