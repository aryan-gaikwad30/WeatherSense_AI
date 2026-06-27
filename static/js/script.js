let chatHistory = [];
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
const sendBtn=document.getElementById("sendBtn");

const chat=document.getElementById("chatMessages");

const input=document.getElementById("chatInput");

if(sendBtn){

sendBtn.addEventListener("click",async()=>{

const question=input.value.trim();

if(question==="") return;

chatHistory.push({
    role: "user",
    message: question
});

chat.innerHTML+=`
<div class="user-message">

${question}

</div>
`;

input.value="";

chat.innerHTML+=`
<div class="ai-message typing" id="typing">

    <span></span>

    <span></span>

    <span></span>

</div>
`;

chat.scrollTo({

    top: chat.scrollHeight,

    behavior: "smooth"

});
// Disable chat while AI is responding
input.disabled = true;
sendBtn.disabled = true;
const response=await fetch("/chat",{

    method:"POST",

    headers:{
        "Content-Type":"application/json"
    },

    body: JSON.stringify({

        weather: weatherData,

        forecast: forecastData,

        air_quality: airQualityData,

        risk: riskData,

        comfort: comfortData,

        health: healthData,

        history: chatHistory,

        question: question

    })

});

const data=await response.json();
// Re-enable chat after AI replies
input.disabled = false;
sendBtn.disabled = false;
input.focus();

chatHistory.push({
    role: "assistant",
    message: data.answer
});

document.getElementById("typing").remove();

chat.innerHTML += `
<div class="ai-message">

<div class="message-text">

${data.answer}

</div>

<button class="copy-btn">

📋

</button>

</div>`;

chat.scrollTo({
    top: chat.scrollHeight,
    behavior: "smooth"
});

});

}
document.querySelectorAll(".suggestion").forEach(button => {

    button.addEventListener("click", () => {

        const input = document.getElementById("chatInput");

        input.value = button.textContent.trim();

        document.getElementById("sendBtn").click();

    });

});
// Press Enter to send message

const chatInput = document.getElementById("chatInput");

if (chatInput) {

    chatInput.addEventListener("keydown", function (event) {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            document.getElementById("sendBtn").click();

        }

    });

}
document.addEventListener("click",(e)=>{

if(e.target.classList.contains("copy-btn")){

const text=e.target.previousElementSibling.innerText;

navigator.clipboard.writeText(text);

e.target.innerHTML="✅";

setTimeout(()=>{

e.target.innerHTML="📋";

},1500);

}

});