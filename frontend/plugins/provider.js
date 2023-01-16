import Vue from "vue";
import { OpenStreetMapProvider } from 'leaflet-geosearch';
import "leaflet/dist/leaflet.css";
import { GoogleProvider } from 'leaflet-geosearch';

const provider = new GoogleProvider({ apiKey: 'AIzaSyDqoLIqGcBNiEcPpxSRcKTliFu-HJk-LoE' });

export default ({ app }, inject) => {
    inject('osm', provider)
  }
