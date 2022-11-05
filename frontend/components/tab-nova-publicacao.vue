<template>
  <div align="center">
  <v-card flat color="#d3d3d3" width="60vw" title>
    <v-row>
      <v-col cols="1">
        <v-avatar size="80">
        <v-icon v-if="!temImagem" color="#c6535f" size="80">mdi-account-circle</v-icon>
        <v-img v-if="temImagem" :src="userImagem"/>
        </v-avatar>
      </v-col>
      <v-col align="left" cols="2">
        <h2 style="color: black" class="my-5">{{instname}}</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col aling="center" cols="11" class="mx-10">
        <v-textarea rows="4" background-color="white" @click:append="postar">
          <template slot="append">
            <v-btn @click="postar" icon><v-icon color="#c3c3c3">mdi-send</v-icon></v-btn>
            <v-btn @click="coloca_imagem" icon><v-icon color="#c3c3c3">mdi-image</v-icon></v-btn>
          </template>
        </v-textarea>
      </v-col>
    </v-row>
  </v-card>
  </div>
</template>
<script>
export default {
  name: 'nova-publicacao',
  data: () => ({
    temImagem: false,
    userImagem: require('../assets/imagem-3.jpg'),
    instname: 'place holder'
  }),
  methods: {
    postar () {
      window.alert('postado')
    },
    coloca_imagem () {
      window.alert('imagem')
    }
  }
}
</script>
