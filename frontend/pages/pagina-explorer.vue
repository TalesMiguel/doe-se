<template>
    <v-main>
    <v-container fluid>
      <v-app-bar color="pink">
        <v-toolbar dense width="10">
          <input placeholder="Pesquisar" v-model="search" type="text" class="form-control" size="105"/>
        </v-toolbar>
        <v-spacer></v-spacer>
      </v-app-bar>
      <v-list>
        <v-list-item-group>
            <div v-for="item in filteredItem">
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
            </div>
          </v-list-item-group>
        </v-list>
    </v-container>
  </v-main>
</template>


<script>
export default {
  name: 'pagina-explorer',
  layout: 'navbar',
  data: function() {
    return{
      items: [
          {
            temImagem: true,
            tipo: 'Tipo de instituição',
            Instituicao: 'Instituição de Animais',
          },
          {
            temImagem: true,
            tipo: 'Tipo de instituição',
            Instituicao: 'Instituição de Reflorestamento',
          },
          {
            temImagem: true,
            tipo: 'Tipo de instituição',
            Instituicao: 'Instituição Bom Prato',
          },
          {
            temImagem: true,
            tipo: 'Tipo de instituição',
            Instituicao: 'Instituição XYZ',
          },
          {
            temImagem: true,
            tipo: 'Tipo de instituição',
            Instituicao: 'Instituição Sabonete',
          },
          {
            temImagem: true,
            tipo: 'Tipo de instituição',
            Instituicao: 'Instituição BK',
          },
          {
            temImagem: true,
            tipo: 'Tipo de instituição',
            Instituicao: 'Instituição ZYX',
          },
          {
            temImagem: true,
            tipo: 'Tipo de instituição',
            Instituicao: 'Instituição YXZ',
          },
      ],
      search:""
    };
  },
  methods: {
    inst_home (){
      this.$router.push('./inst-home')
    },
  },
  computed: {
    filteredItem: function () {
      var self = this;
      return this.items.filter(function (item) {
        return item.Instituicao.toLowerCase().indexOf(self.search.toLowerCase()) >= 0});
    }
  }
}
</script>
