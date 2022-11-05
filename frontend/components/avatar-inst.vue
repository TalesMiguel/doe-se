<template>
  <v-card flat width="24vw" color="#d3d3d3" tile align="center">
    <v-avatar class="profile" size="164">
      <v-icon size="164" color="#c6535f" v-if="temImagem">mdi-account-circle
        </v-icon>
    </v-avatar>
    <h2 style="color: #d6535f">{{nomeInst}}</h2>
  </v-card>
</template>
<script>
export default {
  name: 'avatar-inst',
  data: function () {
    return {
      temImagem: true,
      nomeInst: 'placeHolder'
    }
  }
}
</script>
