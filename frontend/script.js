async function searchFlights() {
    const origin = document.getElementById("origin").value.trim();
    const destination = document.getElementById("destination").value.trim();
    const date = document.getElementById("date").value; // YYYY-MM-DD automatically

    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "<p>Loading flights...</p>";

    // 🔴 IMPORTANT: build ONE correct URL
    let url = `http://127.0.0.1:8000/flights/search?`;

    if (origin) url += `origin=${encodeURIComponent(origin)}&`;
    if (destination) url += `destination=${encodeURIComponent(destination)}&`;
    if (date) url += `date=${date}&`;   // backend expects YYYY-MM-DD

    try {
        const response = await fetch(url);

        if (!response.ok) {
            const errorText = await response.text();
            resultsDiv.innerHTML = `<p>${errorText}</p>`;
            return;
        }

        const flights = await response.json();

        if (!Array.isArray(flights) || flights.length === 0) {
            resultsDiv.innerHTML = "<p>No flights found.</p>";
            return;
        }

        resultsDiv.innerHTML = "";

        flights.forEach(flight => {
            const card = document.createElement("div");
            card.className = "flight-card";

            card.innerHTML = `
                <div class="flight-info">
                    <strong>${flight.airline_name}</strong><br>
                    ${flight.origin} → ${flight.destination}<br>
                    Departure: ${new Date(flight.departure).toLocaleString()}
                </div>
                <div>
                    <div class="price">₹${flight.base_fare}</div>
                    <button class="book-btn">Book Now</button>
                </div>
            `;

            resultsDiv.appendChild(card);
        });

    } catch (error) {
        console.error(error);
        resultsDiv.innerHTML = "<p>Error fetching flights.</p>";
    }
}
