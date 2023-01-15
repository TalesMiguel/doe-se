<template>
    <v-main>
        <v-container>
            <v-row>
                <v-col>
                    <h1 class="ml-6 mt-4"> Explorar </h1>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-card>
                        <v-tabs
                        background-color="#9e9e9e"
                        center-active
                        dark
                        >
                            <v-tab @click="drawer = false">Projetos em destaque</v-tab>
                            <v-tab @click="drawer = true">Buscar projetos</v-tab>
                        </v-tabs>

                    </v-card>
                </v-col>
            </v-row>
 
            <v-row v-if="drawer">
                <v-col md="3">
                    <v-navigation-drawer
                        v-model="drawer"
                        width="21vw"
                    >
                        <v-card  flat style="height:70vh" color="#d8d5d5" class="d-flex align-center justify-center">
                        </v-card>
                    </v-navigation-drawer>
                </v-col>
                <v-col md="9">
                    <v-card flat style="width:70vw;height:70vh" color="#d8d5d5" class="d-flex align-center justify-center">
                    </v-card>
                </v-col>
            </v-row>
            <v-row v-else>
                <v-col md="12" class="d-flex align-center justify-center">
                    <v-card flat style="width:92vw;height:70vh" color="#d8d5d5" class="d-flex align-center justify-center">
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
  data() {
    return {
        drawer: null,
    }
  }
}
</script>