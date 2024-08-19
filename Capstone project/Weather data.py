import requests

def get_weather(latitude, longitude):
  url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"  
 

  response = requests.get(url)
  data = response.json()
  return data

# Example usage:
latitude = 12.9716
longitude = 77.6412
weather_data = get_weather(latitude, longitude)
print(f"""
Latitude: {latitude}
Longitude: {longitude}
Elevation: {weather_data["elevation"]}
Current Temperature: {weather_data["current_weather"]["temperature"]}{weather_data["current_weather_units"]["temperature"]}
Current Wind Speed: {weather_data["current_weather"]["windspeed"]}{weather_data["current_weather_units"]["windspeed"]}
Current Wind Direction: {weather_data["current_weather"]["winddirection"]}°
""")
