document.addEventListener('DOMContentLoaded', function () {
    initMap();
});

var map;

function initMap() {

    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 52.243656, lng: 21.030119},
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false,
    });
    getPlaces('pt');
}

function getPlaces(type){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var data = $.parseJSON(xhttp.responseText);
            console.log(data);
        }
    };
    xhttp.open('GET', '', true);
    xhttp.send();
}










