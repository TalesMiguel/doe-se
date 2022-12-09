import Vue from "vue";
import * as L from "leaflet";
import VGeosearch from 'vue2-leaflet-geosearch';
import "leaflet/dist/leaflet.css";

Vue.component('v-geo', VGeosearch);

const LeafletPlugin = {
    install(Vue) {
        Vue.prototype.$L = L;
    }
};

Vue.use(LeafletPlugin);