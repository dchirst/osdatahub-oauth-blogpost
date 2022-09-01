<script>
	export let name;
	import { onMount } from "svelte";
	import L from "leaflet";

  // Initialise Map
  let map;
  let marker;
  onMount(() => {
	fetch("/api/oauth-function").then((response) => response.json()).then((response) => alert(response))

	var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 19,
		attribution: '© OpenStreetMap'
	});
	    map = L.map("map", { zoomControl: false,
			center: [51.505, -0.09],
    		zoom: 13,
			layers: [osm]
		});
    L.control.zoom({ position: "topright" }).addTo(map);

  });
</script>

<div id="map" style="position: fixed" />

<style>
  #map {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    cursor: pointer;
  }

	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>