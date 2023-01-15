<template>
<v-main>
  <v-row>
    <v-col md=3>
  <v-card flat width="20vw" height="35vh" color="#d3d3d3" tile align="center">
    <v-avatar class="profile mt-10" size="164">
      <v-icon size="164" color="#c6535f" v-if="temImagem">mdi-account-circle
        </v-icon>
    </v-avatar>
  </v-card>
    </v-col>
    <v-col class="d-flex" md=9>
      <v-img align-left :src="image3" max-height="35vh" max-width="68vw">
      </v-img>
    </v-col>
  </v-row>
  <v-row class="mt-12" fluid>
    <v-col md=12>
    <v-card flat width="92vw" height="80vh" color="#e9e9e9" tile align="center">
      <v-card-text>
        <v-col>
        <h1> Publicações </h1>
        </v-col>
      </v-card-text>
    </v-card>
    </v-col>
  </v-row>
</v-main>
</template>
<script>
export default {
  name: 'avatar-inst',
  data: function () {
    return {
      temImagem: true,
      image3: require('../assets/imagem-3.jpg'),
    }
  }
}
</script>
