import Vue from "vue";
import { OpenStreetMapProvider } from 'leaflet-geosearch';
import "leaflet/dist/leaflet.css";

export default ({ app }, inject) => {
    inject('osm', new OpenStreetMapProvider())
  }