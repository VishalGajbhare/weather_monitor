// This is a placeholder for fetching data from the backend
document.addEventListener('DOMContentLoaded', () => {
    // Fetch and display daily summaries
    fetch('/api/daily_summary') // Assuming you set up an API endpoint
        .then(response => response.json())
        .then(data => {
            const summaryDiv = document.getElementById('weather-summary');
            data.forEach(summary => {
                const div = document.createElement('div');
                div.textContent = `${summary.city} - Avg Temp: ${summary.avg_temp}°C, Max Temp: ${summary.max_temp}°C, Min Temp: ${summary.min_temp}°C, Condition: ${summary.dominant_condition}`;
                summaryDiv.appendChild(div);
            });
        });
});
