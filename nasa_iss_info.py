import json
import requests
import time

from twython import Twython
from auth import gapi_key
from ipauth import ip_key
from tw_auth import(
  random,
  random_2,
  random_3,
  random_4
)

twitter = Twython(
  random,
  random_2,
  random_3,
  random_4
)

yee = requests.get('https://api.ipify.org?format=json')
meme = yee.json()
print("\nThis is my computers ip address: " + meme['ip'])

ip = meme['ip']
ip_api_url = 'https://geo.ipify.org/api/v1?'

url_3 = ip_api_url + 'apiKey=' + ip_key + '&ipAddress=' + ip
test = requests.get(url_3)
test_2 = test.json()
print("\nYour current location: " + test_2['location']['city'] + ', ' + test_2['location']['region'] + ', ' +
      test_2['location']['country'])


url_4 = 'http://api.open-notify.org/iss-pass.json?lat=' + str(test_2['location']['lat']) + '&lon=' + str(test_2['location']['lng'])
response_4 = requests.get(url_4)
result_4 = response_4.json()
risetime_1 = result_4['response'][0]['risetime']
iss_duration = result_4['response'][0]['duration']

iss_passtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(risetime_1))
print('The next time the ISS will pass over your current location will be: ' + iss_passtime + ', and it will pass over your location for ' + str(int(iss_duration/60)) + ' minutes.')

if (int(iss_duration) <= 10):
  message = "Everyone, the ISS is going to be above me in 10 minutes or less!"
  twitter.update_status(status = message)
  print("Tweeted: %s" % message)
