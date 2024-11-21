
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Weatherstack API key (Replace with your actual key)
WEATHERSTACK_API_KEY = 4f51b776013a560fafe4e17dd4e677f7

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming request from Dialogflow
    req = request.get_json()
    
    # Get the intent name
    intent_name = req.get('queryResult').get('intent').get('displayName')

    # Example: If the intent is 'GetWeather', fetch weather data
    if intent_name == 'GetWeather':
        # Get the city parameter from the request
        city = req.get('queryResult').get('parameters').get('geo-city')

        # Build the API request URL for Weatherstack
        weather_api_url = f'http://api.weatherstack.com/current?access_key={WEATHERSTACK_API_KEY}&query={city}'
        
        # Make the GET request to Weatherstack API
        response = requests.get(weather_api_url)
        data = response.json()
        
        # Check if we got valid data from the API
        if 'current' in data:
            temperature = data['current']['temperature']  # Temperature in Celsius
            weather_description = data['current']['weather_descriptions'][0]  # Weather description (e.g., 'Clear')
            message = f"The temperature in {city} is {temperature}°C with {weather_description}."
        else:
            message = "Sorry, I couldn't retrieve the weather data for that location."
        
        # Return the message to Dialogflow
        return jsonify({
            'fulfillmentText': message
        })
    
    # Default response if the intent is not recognized
    return jsonify({'fulfillmentText': 'No matching intent found.'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
