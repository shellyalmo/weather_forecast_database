response = {"coord": {"lon": 34.78, "lat": 32.08}, "weather": [{"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02d"}], "base": "stations", "main": {"temp": 303.85, "feels_like": 305.28, "temp_min": 302.59, "temp_max": 304.82, "pressure": 1006, "humidity": 62}, "visibility": 10000, "wind": {
    "speed": 5.1, "deg": 320}, "clouds": {"all": 20}, "dt": 1599661762, "sys": {"type": 1, "id": 6845, "country": "IL", "sunrise": 1599621680, "sunset": 1599666917}, "timezone": 10800, "id": 293397, "name": "Tel Aviv", "cod": 200}
print(response)

# should write function that gets the api every x minutes/ hours
