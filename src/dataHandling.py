import pandas as pd
from pathlib import Path




int_header = ['login url', 'home url', 'username', 'password', 'csv path']
user_header = ['name', 'logboook url']
cred_path = Path.home().joinpath('Documents').joinpath('C2Logbook Downloader').joinpath('CSV').joinpath('internal.csv')
rower_path = Path.home().joinpath('Documents').joinpath('C2Logbook Downloader').joinpath('CSV').joinpath('rowers.csv')
default_home = Path.home().joinpath('Documents').joinpath('C2Logbook Downloader').joinpath('CSV')

def rewriteCredentials(un, pw, login_url = 'https://log.concept2.com/login', home_url = 'https://log.concept2.com/log',
file_path = ''):
    path = cred_path.parent
    if not Path.exists(path):
        path.mkdir(parents=True)
    cred = {
    'username': un, 
    'password' : pw, 
    'login url' : login_url,
    'home url': home_url,
    'file path': file_path
    }
    df = pd.DataFrame(cred)
    df.to_csv(path)


"""
Seeks the credentials from the file path
IF file doesn't exist, it returns False
"""
def getCred(filepath = cred_path):
    try:
       df = pd.read_csv(filepath)
       return df
    except:
        print('No credentials loaded')
        return False


"""
Writes rower data as a row
@param name: [str] name of rower
@param data: [dict]
@param df: pandas dataframe
returns dataframe + rower as row

"""
def writeRower(name, data, df):
    output = pd.DataFrame()
    d = {'Name': name}
    data = d.update(data)
    output = pd.concat([df, data], sort=False)
    return output

def createDataFrame(labels, names):
    df = pd.DataFrame(columns=labels, index=names)
    return df

def nullNaN(df):
    return df.fillna(0, inplace=True)

def doesFileExist(filename):
    return Path.exists(filename)

def writeFile(filename, df, sheet_name='No Name', startrow=None,
                       truncate_sheet=False, 
                       **to_excel_kwargs):
    # If file doesn't exist
    if not doesFileExist(filename):
         df.to_excel(filename, sheet_name=sheet_name, 
            startrow=startrow if startrow is not None else 0)
    
    else:
        with pd.ExcelWriter(filename, mode='a', if_sheet_exists='new') as writer:
            df.to_excel(writer, sheet_name=sheet_name, 
                startrow=startrow if startrow is not None else 0)
    
    writer.save()

def getRowers(filepath = rower_path):
    try:
       df = pd.read_csv(filepath)
       return df
    except:
        return False

def removeData(df, to_remove, repeats):
    labels = list()
    for l in to_remove:
        for i in range(repeats+1):
            labels.append(l + ' ' + str(i))
    labels.append('AVG'+ ' '+  l)
    df.drop(labels, axis = 1)
    return df
    