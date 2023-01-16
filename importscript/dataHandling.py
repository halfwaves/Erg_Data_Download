import pandas as pd
import csv
from os import mkdir
from pathlib import Path



int_header = ['login url', 'home url', 'username', 'password']
user_header = ['name', 'logboook url']
cred_path = Path('./importscript').joinpath('CSV').joinpath('internal.csv')

def openFormatting():
    path = cred_path.parent
    if not Path.exists(path):
        path.mkdir(parents=True)
    csvfile = open(cred_path, mode='w')
    writer = csv.DictWriter(csvfile, fieldnames=int_header)
    writer.writeheader()
    return writer



def rewriteCredentials(un, pw, login_url = 'https://log.concept2.com/login', home_url = 'https://log.concept2.com/log'):
    w = openFormatting()
    cred = {
    'username': un, 
    'password' : pw, 
    'login url' : login_url,
    'home url': home_url
    }
    w.writerow(cred)

def getCred(filepath = cred_path):
    try:
       with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return row
    except:
        print('No credentials loaded')

