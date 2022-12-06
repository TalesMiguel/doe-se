<template>
    <v-container fluid class="my-16">
        <v-card flat>
            <v-img class="text aling-end" src="https://raw.githubusercontent.com/Riiber0/doe-se/main/frontend/assets/imagem-3.jpg" max-height="20vh">
            </v-img>
        </v-card>
        <v-container fluid class="my-20">
            <v-row>
                <v-col>
                    <v-card flat width="24vw" height="400" color="#d3d3d3" tile align="center">
                        <v-avatar class="profile" size="164">
                            <v-icon size="164" color="#c6535f" v-if="temImagem">mdi-account-circle
                                </v-icon>
                        </v-avatar>
                        <h1 style="color: #d6535f">{{nomeInst}}</h1>
                        <v-container>
                            <v-row>
                                <v-col>
                                    <div align="right">
                                        <v-icon color="green" size="60" >mdi-food-apple</v-icon>
                                    </div>
                                </v-col>
                                <v-col class="my-3">
                                    <div align="left">
                                        <h2>Comida</h2>
                                    </div>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card>
                </v-col>
                <v-col>
                    <v-container fluid class="my-20">
                    <v-card flat width="60vw" color="#d3d3d3" tile align="center">
                        <v-row>
                            <v-col
                                v-for="n in 9"
                                :key="n"
                                class="my-1"
                                cols="4">
                                <v-img
                                    :src="`https://picsum.photos/500/300?image=${n * 5 + 5}`"
                                    aspect-ratio="1.5"
                                    class="grey lighten-2">
                                </v-img>
                            </v-col>
                        </v-row>
                    </v-card>
                </v-container>
                </v-col>
            </v-row>
        </v-container>
    </v-container>
</template>

<script>
export default {
  name: 'pagina-instituicao',
  layout: 'navbar',
  data: function () {
    return {
      temImagem: true,
      nomeInst: 'placeHolder'
    }
  }
}
</script>