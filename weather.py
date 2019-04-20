import re, sys, os, json
import requests

API_KEY = os.environ['OWM_API_KEY']

def fetch_weather(zipcode):
	path = 'http://api.openweathermap.org/data/2.5/weather?zip={},us'.format(zipcode)
	path += '&APPID={}'.format(API_KEY)
	response = requests.get(path)

	return response.text

def parse_json(weather_result):
	data = json.loads(weather_result)

	ret = {}
	ret['weather'] = data['weather'][0]['description']
	ret['temp'] = data['main']['temp']

	return ret

def main(zipcode):
	weather_result = fetch_weather(zipcode)
	parsed_result = parse_json(weather_result)

	print("{} {} degrees Kelvin".format(parsed_result['weather'], parsed_result['temp']))

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: python3 weather.py 80301')
		sys.exit()

	zipcode = sys.argv[1]
	match = re.search(r'\d{5}', zipcode)

	if match:
		main(zipcode)
	else:
		raise ValueError("Invalid ZIP code supplied. Please provide a 5-digit ZIP.")
