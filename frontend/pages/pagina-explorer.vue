<template>
    <v-main>
    <v-container fluid>
      <v-app-bar color="pink">
        <v-toolbar dense width="10">
          <v-text-field hide-details single-line clearable>
          </v-text-field>
              <v-btn icon>
                <v-icon>mdi-magnify</v-icon>
              </v-btn>
        </v-toolbar>
        <v-spacer></v-spacer>
      </v-app-bar>
      <v-list>
        <v-list-item-group>
            <template v-for="(item, index) in items">
              <v-list-item style="width: 100vw;" v-if="!active" @click="inst_home">
                <v-list-item-avatar>
                  <v-icon size="50" color="#c6535f" v-if="item.temImagem">mdi-account-circle
                  </v-icon>
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title v-text="item.Instituicao" align="left">
                  </v-list-item-title>
                  <v-list-item-subtitle class="text--primary" v-text="item.tipo" align="left">
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list-item-group>
        </v-list>
    </v-container>
  </v-main>
</template>


<script>
export default {
  name: 'pagina-explorer',
  layout: 'navbar',
  data: () => ({
    selected: [2],
    items: [
        {
          temImagem: true,
          tipo: 'Tipo de instituição',
          Instituicao: 'Instituição zzzz-zzzz',
        },
        {
          temImagem: true,
          tipo: 'Tipo de instituição',
          Instituicao: 'Instituição zzzz-zzzz',
        },
        {
          temImagem: true,
          tipo: 'Tipo de instituição',
          Instituicao: 'Instituição zzzz-zzzz',
        },
        {
          temImagem: true,
          tipo: 'Tipo de instituição',
          Instituicao: 'Instituição zzzz-zzzz',
        },
        {
          temImagem: true,
          tipo: 'Tipo de instituição',
          Instituicao: 'Instituição zzzz-zzzz',
        },
        {
          temImagem: true,
          tipo: 'Tipo de instituição',
          Instituicao: 'Instituição zzzz-zzzz',
        },
        {
          temImagem: true,
          tipo: 'Tipo de instituição',
          Instituicao: 'Instituição zzzz-zzzz',
        },
        {
          temImagem: true,
          tipo: 'Tipo de instituição',
          Instituicao: 'Instituição zzzz-zzzz',
        },
    ],
  }),
  methods: {
    inst_home (){
      this.$router.push('./inst-home')
    }
  }
}

</script>
<style>
.center {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>