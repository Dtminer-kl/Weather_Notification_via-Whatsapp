import requests
from twilio.rest import Client

# Using OpenWeather for Weather Data
# USing Twilio for sms/whatsapp api message sending

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# if you want to use it you have to make your own API key for open weather
api_key = ""

# you also have to make your own account on twilio (as well as generate a number from twilio)
account_sid = ""
auth_token = ""

# The data received from the api is in 3hr intervals. cnt represents the number of 3hr intervals from 6am.
# Change the lon and lat to your location
parameters = {
    "lon": 101.518349,
    "lat": 3.073838,
    "cnt": 4,
    "appid": api_key
}

# Getting API information about weather using the paras from above
response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_date = response.json()

will_rain = False

# parsing through json data and getting the weather code
for hour_data in weather_date["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    # Input the number from twilio in 'from_' and your verified number in 'to'
    message = client.messages.create(
        body='Bring an Umbrella!',
        from_='whatsapp:+',
        to='whatsapp:+'
    )
    print(message.status)
