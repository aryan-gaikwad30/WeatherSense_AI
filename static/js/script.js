function createLineChart(canvasId, label, data) {

    const canvas = document.getElementById(canvasId);

    if (!canvas || chartLabels.length === 0) {
        return;
    }

    new Chart(canvas, {

        type: "line",

        data: {

            labels: chartLabels,

            datasets: [{
                label: label,
                data: data,
                borderWidth: 3,
                fill: false,
                tension: 0.4
            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            scales: {

                y: {

                    beginAtZero: false

                }

            }

        }

    });

}


// =========================
// Temperature Chart
// =========================

createLineChart(
    "temperatureChart",
    "Temperature (°C)",
    chartTemps
);


// =========================
// Humidity Chart
// =========================

createLineChart(
    "humidityChart",
    "Humidity (%)",
    chartHumidity
);


// =========================
// Wind Speed Chart
// =========================

createLineChart(
    "windChart",
    "Wind Speed (km/h)",
    chartWind
);
// ==========================
// Geolocation
// ==========================

const locationBtn = document.getElementById("locationBtn");

if (locationBtn) {

    locationBtn.addEventListener("click", () => {

        if (!navigator.geolocation) {

            alert("Geolocation is not supported.");

            return;

        }

        navigator.geolocation.getCurrentPosition(

            async (position) => {

                const latitude = position.coords.latitude;

                const longitude = position.coords.longitude;

                const response = await fetch("/location", {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json"

                    },

                    body: JSON.stringify({

                        latitude,

                        longitude

                    })

                });

                if (!response.ok) {

                    alert("Unable to fetch your location weather.");

                    return;

                }

                // Simplest approach for now:
                // reload the page with detected city.

                const data = await response.json();

                window.location.href = "/?city=" + encodeURIComponent(data.weather.city);

            },

            () => {

                alert("Location permission denied.");

            }

        );

    });

}
const form = document.querySelector("form");

if(form){

    form.addEventListener("submit",()=>{

        document.getElementById("loadingSpinner").style.display="block";

    });

}