"""
This program is intended to help me download and import erg data from concept2's website
"""
import requests

cred = { 'un': 'newton145', 
'pw' : 'bvq8fvp2rza2RYQ@pep', 
'url' : 'https://log.concept2.com/login',
'dev_url': 'https://log-dev.concept2.com/login'
}

response = requests.get(cred['url'])

print(response)