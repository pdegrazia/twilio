from twilio.rest import TwilioRestClient
from config import *
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=%s' % open_weather_api_key)
r_json = r.json()

description = r_json['weather'][0]['description']
temperature = r_json['main']['temp']

client = TwilioRestClient(tw_account_sid, tw_auth_token)
message = 'London: %s degrees, %s' % (temperature, description)
message = client.messages.create(to='+447513472349', from_='+441745472066', body=message)