document.querySelectorAll("input").forEach(input => {
    input.addEventListener("input", updateProgress);
});


document.querySelectorAll('input[type="radio"]').forEach(radio => {
    radio.addEventListener("change", updateProgress);
});
let progress=0
const values=new Map();
function updateProgress(event) {
    const id = event.target.id;
    const value = event.target.value;

    if (value === "") {
        values.delete(id);
    } else {
        values.set(id, value);
    }

    progress = (values.size / 13) * 100;

    document.getElementById("progress-pct").innerText =
        Math.round(progress) + "%";
}
async function submitRecord(){
    const data=Object.fromEntries(values)

    const response=await fetch("/predict",{
        method:"Post",
        headers:{"Content-type":"application/json"},
        body:JSON.stringify(data)
    })

    const result = await response.json(); 
    console.log(result);
}
function clearForm() {
    document.querySelectorAll('input[type="number"]').forEach(input => {
        input.value = "";
    });
    document.querySelectorAll('input[type="radio"]').forEach(radio => {
        radio.checked = false;
    });
    values.clear();
    progress = 0;
    document.getElementById("progress-pct").innerText = "0%";
    console.log("Form Cleared");
}