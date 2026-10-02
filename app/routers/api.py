<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>PocketSmart AI Dashboard</title>
    <link rel="stylesheet" href="/static/styles.css" />
  </head>

  <body>
    <main class="card dashboard">
      <h1>{{ welcome_message }}</h1>

      <div class="stats">
        <div class="stat-box">
          <span class="label">Budget</span>
          <strong>$4,200</strong>
        </div>

        <div class="stat-box">
          <span class="label">Saved</span>
          <strong>$1,150</strong>
        </div>

        <div class="stat-box">
          <span class="label">Ideas</span>
          <strong>12</strong>
        </div>
      </div>

      <hr />

      <h2>Smart Recommendation</h2>

      <form id="recommendForm" class="stacked-form">

        <label>
          Category
          <select id="category" required>
            <option value="home_interior">Home Interior</option>
            <option value="party">Party</option>
            <option value="jewelry">Jewelry</option>
          </select>
        </label>

        <label>
          Budget
          <input
            type="number"
            id="budget"
            value="1000"
            min="1"
            required
          />
        </label>

        <label>
          Style
          <input
            type="text"
            id="style"
            value="modern"
            required
          />
        </label>

        <label>
          Notes
          <textarea
            id="notes"
            placeholder="Tell PocketSmart AI what you need..."
          ></textarea>
        </label>

        <button type="submit">
          Get AI Recommendation
        </button>
      </form>

      <div id="result" class="muted"></div>

      <div class="actions">
        <a href="/">Home</a>
        <a href="/login">Login</a>
      </div>
    </main>

    <script>
      document
        .getElementById("recommendForm")
        .addEventListener("submit", async function (event) {
          event.preventDefault();

          const result = document.getElementById("result");

          result.textContent = "Generating recommendation...";

          const payload = {
            category: document.getElementById("category").value,
            budget: Number(document.getElementById("budget").value),
            style: document.getElementById("style").value,
            notes: document.getElementById("notes").value
          };

          try {
            const response = await fetch("/api/recommend", {
              method: "POST",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (response.ok) {
              result.innerHTML = `
                <h3>AI Recommendation</h3>
                <p>${data.recommendation}</p>
                <p><strong>Estimated Cost:</strong> $${data.estimated_cost}</p>
              `;
            } else {
              result.textContent =
                data.detail || "Unable to generate recommendation.";
            }
          } catch (error) {
            result.textContent =
              "Unable to connect to the recommendation service.";
          }
        });
    </script>
  </body>
</html>