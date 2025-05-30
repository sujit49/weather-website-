import json
import requests
from flask import Flask, render_template, request
import plotly.graph_objs as go
import plotly

app = Flask(__name__)

API_KEY = "101a8012bb63aa43add3a33c93a1fa64"
CURRENT_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    unit = request.form.get('unit', 'metric')
    unit_symbol = '°C' if unit == 'metric' else '°F'

    if not city:
        return render_template('index.html', error="City name cannot be empty.")

    # Fetch current weather
    current_params = {'q': city, 'appid': API_KEY, 'units': unit}
    current_response = requests.get(CURRENT_WEATHER_URL, params=current_params)
    current_data = current_response.json()

    if current_response.status_code != 200:
        error_msg = current_data.get('message', 'Unable to fetch current weather data.')
        return render_template('index.html', error=error_msg)

    current_weather = {
        'description': current_data['weather'][0]['description'].capitalize(),
        'icon': current_data['weather'][0]['icon'],
        'temperature': current_data['main']['temp'],
        'humidity': current_data['main']['humidity'],
        'wind_speed': current_data['wind']['speed'],
    }

    # Fetch 5-day forecast
    forecast_params = {'q': city, 'appid': API_KEY, 'units': unit}
    forecast_response = requests.get(FORECAST_URL, params=forecast_params)
    forecast_data = forecast_response.json()

    if forecast_response.status_code != 200:
        error_msg = forecast_data.get('message', 'Unable to fetch forecast data.')
        return render_template('index.html', error=error_msg)

    dates = [entry['dt_txt'] for entry in forecast_data['list']]
    temps = [entry['main']['temp'] for entry in forecast_data['list']]

    # Create Plotly graph for forecast
    graph = go.Figure(data=go.Scatter(x=dates, y=temps, mode='lines+markers'))
    graph.update_layout(
        title="Temperature Trend (5 Days)",
        xaxis_title="Date & Time",
        yaxis_title=f"Temperature ({unit_symbol})",
        template="plotly_dark"
    )
    graph_json = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('weather.html',
                           city=city,
                           current_weather=current_weather,
                           graph_json=graph_json)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

