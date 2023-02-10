function loadPage() {
    console.log("Loaded info");
    var url = 'http://127.0.0.1:5000/get-locations';
    $.get(
        url, function(data, status) {
            console.log("recieved response");
            if(data) {
                var locations = data.locations;
                var theLocations = document.getElementById("theLocations");
                $('#theLocations').empty();
                for(var i in locations) {
                    var opt = new Option(locations[i]);
                    $('#theLocations').append(opt);
                }
            }
        }
    );
}

function approximatePrice() {
    console.log("estimatimating price");
    var sft = document.getElementById("sqft");
    var bathroom = document.getElementById("bathroom");
    var bedrooms = document.getElementById("bedrooms");
    var loc = document.getElementById("theLocations");
    var approxPrice = document.getElementById("ApproxPrice");

    var webUrl = "http://127.0.0.1:5000/predict-price";

    $.post(
        webUrl, {
            // sft: parseFloat(sft.value),
            // bath: parseInt(bathroom),
            // bedrooms: parseInt(bedrooms),
            // loc: loc.value,

            sft: parseFloat(sft.value),
            bath: 3,
            bedrooms: 3,
            loc: loc.value,
        },
        function(data, status) {
            console.log(data.approximate_price);
            approxPrice.innerHTML =+ data.approximate_price.toString();
            console.log(status);
        }
    );
}

window.onload = loadPage;