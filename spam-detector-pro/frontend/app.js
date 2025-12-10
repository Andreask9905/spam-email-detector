async function analyzeEmail() {
    const text = document.getElementById("emailInput").value;

    if (!text.trim()) {
        alert("Please paste an email first.");
        return;
    }

    const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    // Show result box
    document.getElementById("resultBox").classList.remove("hidden");

    // Prediction
    document.getElementById("prediction").textContent = data.prediction;
    document.getElementById("probability").textContent = data.probability.toFixed(4);

    // URLs
    const urlList = document.getElementById("urlList");
    urlList.innerHTML = "";
    data.urls.forEach(url => {
        const li = document.createElement("li");
        li.textContent = url;
        urlList.appendChild(li);
    });

    // Phishing warnings
    const warnList = document.getElementById("warningsList");
    warnList.innerHTML = "";
    data.phishing.forEach(w => {
        const li = document.createElement("li");
        li.textContent = `${w.url} → ${w.warnings.join(", ")}`;
        warnList.appendChild(li);
    });
}
