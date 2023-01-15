import requests as req
import dataHandling as dataHand
from requests.exceptions import Timeout
from htmlParse import HTMLParseDammit 


def startSession():
    s = req.Session()
    return s

def createParser():
    p = HTMLParseDammit()
    return p

"""
Logs the User in to Concept 2 account
@param: s = user session
@param: p = parser object
@param: url = login url
"""
def userLoginC2(s, p, url = 'https://log.concept2.com/login'):
    #session.auth('username', getpass())
    r = s.get(url)
    r.encoding = r.headers['content-type']
    temp = r.headers
    # print(r.text)
    p.feed(r.text)
    output = p.get_inputs()

    for d in output:
        if 'name' in d:
            if d['name'] == 'username':
                un_id = d['id']
            if d['name'] == 'password':
                pw_id = d['id']
            if d['name'] == '_token':
                token = d['value']
        elif 'type' in d:
            if d['type'] == 'submit':
                submit_in = (d['class'],d['value'])
        else:
            print(d)
        
    # parsed = r.text.dataParse(['username', 'password', '_token'])
    payload = { }

    s.post(url, payload)
    return [s,r]

def getReq(s, url):
    return s.get(url)

def postReq(s, url):
    return s.post(url)



def loadLoginInfo(un_id, pw_id, input_name):
    cred = dataHand.getCred()
    data = {
    un_id : cred['username'],
    pw_id : cred['password'],
    'action' : 'login'
    }    
    return data

