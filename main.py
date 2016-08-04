from twilio.rest import TwilioRestClient
from config import *
import requests
from number_list import *
import sys

def main(contacts):
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=%s' % open_weather_api_key)
	r_json = r.json()

	description = r_json['weather'][0]['description']
	temperature = r_json['main']['temp']

	for contact in contacts:
		tw_account_sid = NUMBER_LIST[contact]['tw_account_sid']
		tw_auth_token = NUMBER_LIST[contact]['tw_auth_token']

		client = TwilioRestClient(tw_account_sid, tw_auth_token)

		message = 'Good Morning %s' % contact + '!'
		message += 'London: %s degrees, %s' % (temperature, description)

		recipient = NUMBER_LIST[contact]['recipient']
		sender = NUMBER_LIST[contact]['sender']
		sms = client.messages.create(to=recipient, from_=sender, body=message)

if __name__ == '__main__':
	contacts = sys.argv[1:]
	main(contacts)