document.getElementById("checkBtn").addEventListener("click", async () => {
    const text = document.getElementById("emailText").value.trim();

    if (text === "") {
        alert("Παρακαλώ γράψε ένα μήνυμα για έλεγχο.");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });

        const data = await response.json();

        document.getElementById("result").innerHTML = `
            <strong>Αποτέλεσμα:</strong> ${data.label.toUpperCase()} <br>
            <strong>Πιθανότητα SPAM:</strong> ${(data.probability * 100).toFixed(2)}%
        `;
    } catch (error) {
        console.error("Error:", error);
        alert("Σφάλμα σύνδεσης με το backend.");
    }
});
