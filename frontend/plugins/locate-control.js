import Vue from "vue";
import * as L from "leaflet";
import Vue2LeafletLocatecontrol from 'vue2-leaflet-locatecontrol';
import "leaflet/dist/leaflet.css";

Vue.component('v-locate-control', Vue2LeafletLocatecontrol);

 const LeafletPlugin = {
  install(Vue) {
   Vue.prototype.$L = L;
  }
 };

Vue.use(LeafletPlugin);