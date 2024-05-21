import requests

def fetch_weather_data(location, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Adjust units as needed (e.g., metric, imperial)
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data):
    if data and "main" in data and "weather" in data:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather in {data['name']} - Temperature: {temperature}°C, Humidity: {humidity}%, Conditions: {weather_description}")
    else:
        print("Location not found or data unavailable.")

def main():
    location = input("Enter a city or ZIP code: ")
    '''Replace the api key wiyh your own api key'''
    api_key = "[c*$~L;[kf_np39"
    weather_data = fetch_weather_data(location, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
