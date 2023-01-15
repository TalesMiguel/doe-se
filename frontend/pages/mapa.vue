<template>
    <v-main>
        <v-container fluid style="height: 89vh">
            <v-row class="mt-10" style="max-height: 20vh">
                <v-col md="3"></v-col>
                <v-col md="9" align="center" align-self="end" class="mb-2">
                    <h2 class="ml-16"> Projetos sociais próximos a você! </h2>
                </v-col>
            </v-row>
            <v-row align="center" style="height: 40vh">
                <v-col md=3 align="right" align-self="center">
                    <v-card flat style="width:25vw;height:60vh" color="#d8d5d5" class="ml-16">
                        <v-card-title class="justify-center"> <p class="font-size: 32px mt-8 mb-4">
                            Pesquisar
                        </p> </v-card-title>
                        <v-card-actions class="justify-center">
                                <v-form ref="form" v-on:submit.prevent="buscarEndereco()">
                                    <v-row>
                                        <v-col class="ml-3"> 
                                            <v-text-field v-model="endereco" required :rules="[v => !!v || '']" flat label="Digite seu endereço" filled style="width: 18vw">
                                            </v-text-field>
                                        </v-col>
                                        <v-col class="mt-3">
                                            <v-btn @click='buscarEndereco()' icon> <v-icon>mdi-magnify</v-icon> </v-btn>
                                        </v-col>
                                    </v-row>
                                </v-form>
                        </v-card-actions>
                        <v-row class="justify-center pa-0">
                            <v-card-title>
                            <p class="font-size:32px">
                                Filtrar
                            </p>
                            </v-card-title>
                        </v-row>
                        <v-row class="justify-left pa-0 ml-16">
                            <v-checkbox v-model='roupa' @click="filtrar('Roupa')" label="Roupa" class='mx-6'></v-checkbox>
                        </v-row>
                        <v-row class="justify-left pa-0 ml-16">
                            <v-checkbox v-model='comida' @click="filtrar('Comida')" label="Comida" class='mx-6'></v-checkbox>
                        </v-row>
                         <v-row class="justify-left pa-0 ml-16">
                            <v-checkbox v-model='trabalho' @click="filtrar('Trabalho')" label="Voluntariado" class='mx-6'></v-checkbox>
                        </v-row>
                        <v-spacer/>
                        <v-card-actions class="justify-center my-8">
                            <v-btn depressed @click="limparFiltros" :disabled="vazio" max-height="30px" min-width="150px">
                                <p class="mt-4" style="font-size: 12px"> Limpar filtros </p>
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
                <v-col md=9 align="right" align-self="center">
                <client-only>
                    <l-map :zoom="zoom" :center="center" style="height:700px;width:1250px;z-index: 0" ref="map" class="mr-10">
                        <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                        <l-marker :lat-lng="markerLatLng"></l-marker>
                        <l-geo-json :geojson="markers" :options="options"></l-geo-json>
                        <v-locate-control/>
                        <v-geo :options="geosearchOptions"></v-geo>
                        
                    </l-map>
                </client-only>
                </v-col>
            </v-row>
        </v-container>
    </v-main>
</template>

<script>
export default {
    name: 'MapaPage',
    layout: 'navbar',
    mounted() {
        this.getGeoJson()
        if(this.$route.query.endereco !== undefined)
        {
            this.processarEnderecoDjango(this.$route.query.endereco)
        }
    },
    methods:
    {
        buscarEndereco() 
        {
            if(this.$refs.form.validate()){
                this.processarEnderecoDjango(this.endereco)
            }
        },

        processarEnderecoDjango(par) 
        {
                this.loading = true
                const formAcao = new FormData()
                formAcao.append('endereco', par)
                this.$axios.post('get-coord/', formAcao)
                .then(async (response) => { 
                    this.center = [ response.data[0], response.data[1] ]
                    this.markerLatLng = [ response.data[0], response.data[1] ]
                    this.$refs.form.reset()})
                .catch(async (err) => { console.log(err) }) 
        },

        getGeoJson() 
        {
            this.loading = true
            this.$axios.get('get-geojson/')
                .then(async (response) => { this.markers = (response.data); })
                .catch(async (err) => { console.log("Erro " + err)} )
        },

        removeItem(value) 
        {
            var index = this.options.filtro.indexOf(value);
            if (index > -1) {
                this.options.filtro.splice(index, 1);
            }
        },

        filtrar(acao)
        {
            switch (acao)
            {
                case 'Roupa':
                    if(this.options.filtro.includes('Roupa')) { this.removeItem('Roupa'); } 
                    else { this.options.filtro.push('Roupa'); this.vazio = false; }
                    break;

                case 'Comida':
                    if(this.options.filtro.includes('Comida')) { this.removeItem('Comida'); } 
                    else { this.options.filtro.push('Comida'); this.vazio = false; }
                    break;

                case 'Trabalho':
                    if(this.options.filtro.includes('Trabalho')) { this.removeItem('Trabalho'); } 
                    else { this.options.filtro.push('Trabalho'); this.vazio = false; }
                    break;
                
                default:
                    break;
            }

            if(this.options.filtro.length === 0) { this.vazio = true; }
        },

        limparFiltros() 
        {
            this.options.filtro = []
            this.roupa = false
            this.comida = false
            this.trabalho = false
            this.vazio = true
        }
    },
    data() {
        return {
            center: [-23.19251217538178, -45.893768442266534],
            markers: null,
            vazio: true,
            zoom: 14,
            roupa: false,
            comida: false,
            trabalho: false,
            vazio: true,
            endereco: null,
            markerLatLng: [0, 0],
            geosearchOptions: { 
                provider: this.$osm,
                showMarker: true, 
                showPopup: false, 
                autoClose: true,
                searchLabel: 'Entre seu endereço', 
                keepResult: true,
            },
            options: {
                filtro: [],
                /*
                pointToLayer: function pointToLayer(feature, latlng) {
                    if(feature.properties.tipo.includes('Comida'))
                    {
                        return L.marker(latlng, {icon: L.icon({iconSize: [50, 50], iconUrl:""})})
                    }
                    if(feature.properties.tipo.includes('Roupa'))
                    {
                        return L.marker(latlng, {icon: L.icon({iconSize: [50, 50], iconUrl:""})})
                    }
                },
                */
                onEachFeature: function onEachFeature(feature, layer) {
                    var texto = "<b>" + feature.properties.nome + "</b>" + "<br>" + feature.properties.tipo.toString() + "<br>" + feature.geometry.coordinates;
                    layer.bindPopup(texto);
                    //layer.bindTooltip(feature.properties.nome);
                },

                filter: function(feature) {
                    if(this.filtro.length === 0) { return true; }
                    if(this.filtro.includes('Roupa') && feature.properties.tipo.includes('Roupa')) {  return true; }
                    if(this.filtro.includes('Comida') && feature.properties.tipo.includes('Comida')) { return true; }
                    if(this.filtro.includes('Trabalho') && feature.properties.tipo.includes('Trabalho')) { return true; }
                },
            }
        }
    },
}
</script>

<style scoped>
    @import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";
    @import "https://unpkg.com/leaflet-geosearch@2.6.0/assets/css/leaflet.css";
</style>
