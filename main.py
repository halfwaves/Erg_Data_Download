"""
This program is intended to help me download and import erg data from concept2's website
"""
import requests, json
from requests.exceptions import Timeout
from getpass import getpass

cred = {'client_id':'x',
'client_secret': 'x',
'grant_type':'',
'scope': 'user:read,results:read',
'un': 'newton145', 
'pw' : 'bvq8fvp2rza2RYQ@pep', 
'url' : 'https://log.concept2.com/login',
'dev_url': 'https://log-dev.concept2.com/login'
}

form_data = {'username':'newton145', 'pw':'bvq8fvp2rza2RYQ@pep'}

def user_login_c2(url):
    with requests.Session() as s:
        #session.auth('username', getpass())

        r = s.get(url)
        #read_r = r.json()
        print(r.encoding)
        print(r.headers)
        r = s.post(url, data = form_data)
        print(r.text)
        return [s,r]


[s, r] = user_login_c2(cred.get('url'))
