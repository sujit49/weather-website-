# ☁️ Weather Dashboard

A simple web application built with Flask that allows users to get current weather conditions and a 5-day temperature forecast for any city worldwide. The forecast data is visualized using an interactive Plotly graph.

---

## 🧩 Features

-   **Current Weather:** Displays real-time temperature, description, humidity, and wind speed for a specified city.
-   **5-Day Forecast:** Provides a detailed 5-day temperature trend.
-   **Interactive Graph:** Visualizes the temperature forecast using Plotly, allowing for easy understanding of future weather patterns.
-   **Unit Selection:** Choose between Metric (°C) and Imperial (°F) units for temperature.
-   **Responsive Design:** Utilizes Bootstrap for a clean and responsive user interface.

---

## 📸 Preview

> (Optional) Add a screenshot of the app interface here

---

## 📁 File Structure

.
├── main.py             # Flask application backend logic
├── templates/
│   ├── index.html      # Main page with city input form
│   └── weather.html    # Page to display weather results and forecast graph
└── README.md           # Project documentation


---

## 🛠️ How to Run

To run this application, you'll need Python 3 installed on your system.

### Prerequisites

-   Python 3.x
-   `pip` (Python package installer)

### Installation

1.  **Clone or download** this repository to your local machine.
2.  **Navigate** into the project directory:
    ```bash
    cd your_project_folder
    ```
3.  **Install the required Python libraries** using pip:
    ```bash
    pip install Flask requests plotly
    ```
4.  **OpenWeatherMap API Key:**
    The `main.py` file uses a placeholder API key (`101a8012bb63aa43add3a33c93a1fa64`). For production use or if you encounter API limits, it's highly recommended to:
    * Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api).
    * Replace `API_KEY = "101a8012bb63aa43add3a33c93a1fa64"` in `main.py` with your own key.

### Running the Application

1.  From the project directory, run the Flask application:
    ```bash
    python main.py
    ```
2.  Open your web browser and go to the address displayed in your terminal (usually `http://127.0.0.1:5000/`).

---

## 🎮 Usage

1.  On the homepage, enter the name of a city in the input field.
2.  Select your preferred temperature unit (Metric or Imperial).
3.  Click the "Get Weather" button.
4.  The application will display the current weather details and an interactive 5-day temperature forecast graph for the entered city.
5.  If there's an error (e.g., city not found, API issue), an error message will be displayed.

---

## 🚀 Ideas for Improvement

-   Implement a search suggestion/autocomplete for city names.
-   Add more weather details (e.g., pressure, visibility).
-   Allow users to save favorite cities.
-   Improve error handling and user feedback.
-   Add a dark mode toggle.
-   Integrate with other weather APIs for comparison or redundancy.

---

## 📜 License

This project is for educational purposes. Feel free to modify and improve it!
