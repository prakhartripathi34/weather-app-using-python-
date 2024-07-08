import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = "cc17a8bd4c8b458655be76e107fd7aed"

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + API_KEY + "&q=" + city

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        if data['cod'] != 200:
            raise KeyError

        main = data['main']
        weather = data['weather'][0]

        temperature_celsius = main['temp'] - 273.15
        temperature_fahrenheit = (main['temp'] - 273.15) * 9/5 + 32
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = weather['description']

        result = (f"Temperature: {temperature_celsius:.2f}°C / {temperature_fahrenheit:.2f}°F\n"
                  f"Pressure: {pressure} hPa\n"
                  f"Humidity: {humidity}%\n"
                  f"Weather Description: {weather_description.capitalize()}")

        return result, weather_description
    except requests.exceptions.HTTPError as err:
        if response.status_code == 401:
            return "Unauthorized: Check your API key", ""
        else:
            return f"HTTP Error: {err}", ""
    except KeyError:
        return "Invalid city name. Please try again.", ""
    except Exception as err:
        return f"An error occurred: {err}", ""
