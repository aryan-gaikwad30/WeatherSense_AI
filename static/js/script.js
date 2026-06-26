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