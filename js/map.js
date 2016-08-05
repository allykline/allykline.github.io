function initMap() {
        // var locations = [
        //   ['Bondi Beach', -33.890542, 151.274856],
        //   ['Coogee Beach', -33.923036, 151.259052],
        //   ['Cronulla Beach', -34.028249, 151.157507],
        //   ['Manly Beach', -33.80010128657071, 151.28747820854187],
        //   ['Maroubra Beach', -33.950198, 151.259302],
        // ];
        var mapDiv = document.getElementById('map');
        var map = new google.maps.Map(mapDiv, {
            center: {lat: 37.515946, lng: -122.303908},
            zoom: 8
        });

        // var marker, i;

        // for (i = 0; i < locations.length; i++) {  
        //   marker = new google.maps.Marker({
        //     position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        //     map: map
        //   });

        //   }
