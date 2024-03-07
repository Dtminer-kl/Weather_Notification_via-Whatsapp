import requests
from twilio.rest import Client

# Using OpenWeather for Weather Data
# USing Twilio for sms/whatsapp api message sending

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "9651a557459e4de044dd8b765c26bb14"
account_sid = "ACbfd713d5a0a391b1679791e5e80e5b1f"
auth_token = "d13f55ec29f22a2442d817a20b10ad7a"

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
    message = client.messages.create(
        body='Bring an Umbrella!',
        from_='whatsapp:+14155238886',
        to='whatsapp:+601111774395'
    )
    print(message.status)
