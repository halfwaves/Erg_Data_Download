import pandas as pd
import csv
from pathlib import Path



int_header = ['login url', 'home url', 'username', 'password', 'csv path']
user_header = ['name', 'logboook url']
cred_path = Path.home().joinpath('Documents').joinpath('C2Logbook Downloader').joinpath('CSV').joinpath('internal.csv')
default_home = Path.home().joinpath('Documents').joinpath('C2Logbook Downloader').joinpath('CSV')

def openFormatting():
    path = cred_path.parent
    if not Path.exists(path):
        path.mkdir(parents=True)
    csvfile = open(cred_path, mode='w')
    writer = csv.DictWriter(csvfile, fieldnames=int_header)
    writer.writeheader()
    return writer



def rewriteCredentials(un, pw, login_url = 'https://log.concept2.com/login', home_url = 'https://log.concept2.com/log',
csv_path = ''):
    w = openFormatting()
    cred = {
    'username': un, 
    'password' : pw, 
    'login url' : login_url,
    'home url': home_url,
    'csv path': csv_path
    }
    w.writerow(cred)

"""
Seeks the credentials from the file path
IF file doesn't exist, it returns False
"""
def getCred(filepath = cred_path):
    try:
       with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return row
    except:
        print('No credentials loaded')
        return False

"""
Creates the csv file and sets the proper headers
"""
def createFile(name, intervals, path):
    #Format headers 
    fieldnames = [name, ]
    inters = numberIntervals(intervals)
    for i in inters:
        fieldnames.append(i)
    csvfile = open(path.join(name).join('.csv'), 'w', newline='')
    #Formats in excel tab format
    w = csv.DictWriter(csvfile, dialect='excel_tab')
    w.writeheader(fieldnames)
    return w

"""
Writes rower data as a row
@param intervals: raw intervals 
"""
def writeRower(name, data, intervals, filename):
    datalist = list()
    datalist.append(name)
    for d in data:
        datalist.append(d)
    #TODO: figure out where I need to label the numbers of the intervals
    inters = numberIntervals(intervals)
    rowerdata = dict(zip(inters, datalist))
    filename.writerow(rowerdata)


    