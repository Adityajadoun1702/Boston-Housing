const values = new Map();

document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener("input", function () {
        if (this.value === "") {
            values.delete(this.id);
        } else {
            values.set(this.id, parseFloat(this.value));
        }
        updateProgress();
    });
});

document.querySelectorAll('input[type="radio"]').forEach(radio => {
    radio.addEventListener("change", function () {
        values.set(this.name, parseFloat(this.value)); // uses "chas" as key
        updateProgress();
    });
});

function updateProgress() {
    const progress = (values.size / 13) * 100;
    document.getElementById("progress-pct").innerText =Math.round(progress) + "%";
    document.getElementById("progress-fill").style.width =progress + "%";
}

async function submitRecord() {
    const data = Object.fromEntries(values);

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        document.getElementById("pred-value").innerText = result.prediction.toFixed(2);

    } catch (err) {
        document.getElementById("error-banner").innerText = "Prediction failed: " + err.message;
    }
}

function clearForm() {
    document.querySelectorAll('input[type="number"]').forEach(input => {
        input.value = "";
    });
    document.querySelectorAll('input[type="radio"]').forEach(radio => {
        radio.checked = false;
    });
    values.clear();
    document.getElementById("progress-pct").innerText = "0%";
    document.getElementById("pred-value").innerText = "--";
    document.getElementById("error-banner").innerText = "";
}