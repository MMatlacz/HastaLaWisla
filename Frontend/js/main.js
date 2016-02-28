document.addEventListener('DOMContentLoaded', function () {
    initMap();
});

var places = {};

var markerTemp;
var type;
var map;
var service;
var infoWindow;
var riverCenter = [
    {lat: 52.260964, lng: 21.010678},
    {lat: 52.249313, lng: 21.021554},
    {lat: 52.254627, lng: 21.016011},
    {lat: 52.245088, lng: 21.027933},
    {lat: 52.241630, lng: 21.033057},
    {lat: 52.238236, lng: 21.037763},
    {lat: 52.235610, lng: 21.040168},
    {lat: 52.230166, lng: 21.045292},
    {lat: 52.225298, lng: 21.049998},
    {lat: 52.218891, lng: 21.067567},
    {lat: 52.214791, lng: 21.092143}
];

function initMap() {

    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 52.243656, lng: 21.030119},
        zoom: 16,
        styles: [{
            stylers: [{visibility: 'simplified'}]
        }, {
            elementType: 'labels',
            stylers: [{visibility: 'off'}]
        }],
        disableDefaultUI: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        minZoom: 16
    });
    service = new google.maps.places.PlacesService(map);
    infoWindow = new google.maps.InfoWindow();

    map.addListener('idle', performSearch);

    var strictBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(52.288099, 21.000600),
        new google.maps.LatLng(52.203213, 21.064822)
    );

    // Listen for the dragend event
    google.maps.event.addListener(map, 'dragend', function () {
        if (strictBounds.contains(map.getCenter())) return;

        // We're out of bounds - Move the map back within the bounds

        var c = map.getCenter(),
            x = c.lng(),
            y = c.lat(),
            minX = strictBounds.getSouthWest().lng(),
            minY = strictBounds.getSouthWest().lat(),
            maxX = strictBounds.getNorthEast().lng(),
            maxY = strictBounds.getNorthEast().lat();
        console.log(minX, maxX, minY, maxY);

        if (x < minX) x = minX;
        if (x > maxX) x = maxX;
        if (y < maxY) y = maxY;
        if (y > minY) y = minY;

        map.setCenter(new google.maps.LatLng(y, x));
    });
}

var rad = function (x) {
    return x * Math.PI / 180;
};

var getDistance = function (p1, p2) {
    var R = 6378137; // Earth’s mean radius in meter
    var dLat = rad(p2.lat() - p1.lat);
    var dLong = rad(p2.lng() - p1.lng);
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(rad(p1.lat)) * Math.cos(rad(p2.lat())) *
        Math.sin(dLong / 2) * Math.sin(dLong / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c; // returns the distance in meter
};

function performSearch() {
    var bar = {
        bounds: map.getBounds(),
        type: 'bar',
        openNow: true

    };
    var restaurant = {
        bounds: map.getBounds(),
        type: 'restaurant',
        openNow: true

    };
    var container = [bar, restaurant];
    for (con in container) {
        service.nearbySearch(container[con], callback);
    }
}

function callback(results, status) {
    if (status !== google.maps.places.PlacesServiceStatus.OK) {
        console.error(status);
        return;
    }

    for (var i = 0, result; result = results[i]; i++) {
        con = true;
        for (loc in riverCenter) {
            if (con == false) {
                con = true;
                break;
            }
            if ((getDistance(riverCenter[loc], result.geometry.location) < 600)) {
                console.log(result);
                addMarker(result);
                con = false;
            }
        }
    }
}

function addMarker(place) {
    var image;
    if (place['types'].indexOf('bar') > -1) {
        image = {
            url: "https://maxcdn.icons8.com/Color/PNG/24/Food/bar-24.png",
            anchor: new google.maps.Point(10, 10),
            scaledSize: new google.maps.Size(30, 30)
        }
    } else if (place['types'].indexOf('restaurant') > -1) {
        image = {
            url: "https://maxcdn.icons8.com/iOS7/PNG/25/City/restaurant_membership_card-25.png",
            anchor: new google.maps.Point(10, 10),
            scaledSize: new google.maps.Size(30, 30)
        }
    }
    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location,
        icon: image
    });

    google.maps.event.addListener(marker, 'click', function () {
        service.getDetails(place, function (result, status) {
            if (status !== google.maps.places.PlacesServiceStatus.OK) {
                console.error(status);
                return;
            }
            infoWindow.setContent('<p>' + result.name + '</p><p>' + result.vicinity + '</p>');
            infoWindow.open(map, marker);
        });
    });

    var longpress = false;
    google.maps.event.addListener(map, 'click', function (event) {
        if (longpress) {
            console.log('longpress');
            addCustomMarker(event.latLng)
        } else {
            console.log('shortpress');
        }
    });
    google.maps.event.addListener(map, 'mousedown', function () {

        start = new Date().getTime();
    });
    google.maps.event.addListener(map, 'mouseup', function () {
        end = new Date().getTime();
        longpress = (end - start >= 500);
    });
}

readURL = function () {

    input = $('[name=obraz]')[0];
    tekst = $('[name=text]')[0];
    console.log(markerTemp.position.toString());
    console.log(places[markerTemp.position.toString()]);
    places[markerTemp.position.toString()] = {'input': input, 'tekst': tekst};

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result)
                .css('width', '100px', 'height', 'auto')
                .removeClass('invisible')
        };
        reader.readAsDataURL(input.files[0]);
        $('#descr')
            .text(tekst.value)
            .removeClass('invisible')
    }
};


accept = function (e) {
    markerTemp.addListener('click', function () {
        input = places[markerTemp.position.toString()].input;
        tekst = places[markerTemp.position.toString()].tekst;
        var divA = document.createElement("div");
        divA.className = ('container col-md-12');
        var divI = document.createElement("div");
        var divT = document.createElement("div");

        divI.className = ('col-md-6');
        divT.className = ('col-md-6');

        var image = document.createElement("img");
        var text = document.createElement("p");

        divI.appendChild(image);
        divT.appendChild(text);

        divA.appendChild(divI);
        divA.appendChild(divT);

        var reader = new FileReader();
        reader.onload = function (e) {
            image.src = (e.target.result);
            image.className = 'thumb';

        };
        reader.readAsDataURL(input.files[0]);
        text.textContent = (tekst.value);
        text.className = 'txt';
        infoWindow.setContent(divA);
        infoWindow.open(map, markerTemp);
    });
    infoWindow.close(map, markerTemp);
    return false;
};
addCustomMarker = function (latLng) {
    var marker = new google.maps.Marker({
        map: map,
        position: latLng
    });
    markerTemp = marker;
    google.maps.event.addListener(marker, 'click', function () {
        console.log($('#plate').html());
        infoWindow.setContent($('#plate').html());
        infoWindow.open(map, marker);
    });
};

Handlebars.getTemplate = function (name) {
    if (Handlebars.templates === undefined || Handlebars.templates[name] === undefined) {
        $.ajax({
            url: 'templates/' + name + '.handlebars',
            success: function (data) {
                if (Handlebars.templates === undefined) {
                    Handlebars.templates = {};
                }
                Handlebars.templates[name] = Handlebars.compile(data);
            },
            async: false
        });
    }
    return Handlebars.templates[name];
};








