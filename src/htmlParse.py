from html.parser import HTMLParser
from bs4 import SoupStrainer as strainer
from bs4 import BeautifulSoup
import lxml
from datetime import date as dt
class HTMLParseDammit(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.startTags = list()
        self.tagAttrs = list()
        self.endTags = list()
        self.startEndTags = list()
        self.comments = list()
        self.data = list()
        # self.time = list()
        # self.meters = list()
        # self.pace = list()
        # self.watts = list()
        # self.cals = list()
        # self.spm = list()
        # self.heart = list()
        # self.panel = int
        # self.intervals = list()

   
    def handle_starttag(self, tag, attrs):
      self.startTags.append(tag)
      self.tagAttrs.append(list(attrs))
      return tag

    def handle_endtag(self, tag):
        self.endTags.append(tag)
        return tag

    def handle_data(self, data):
      self.data.append(data)

    def handle_comment(self, data):
        return 'comment: non-funct'

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        return 'dec: non-funct'
    
    def get_inputs(self):
        inputs = list()
        for i, tag in enumerate(self.startTags):
            if tag == 'input':
                attrs = self.tagAttrs[i]
                d = {}
                for val in attrs:
                    d.update({val[0] : val[1]}) 
                inputs.append(d)
        return inputs

    # def get_peice_data(self):
    #     intervals = 



def soupDammit(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup

def getDataLabels(soup):
    labels = list()
    for i in range(1, getNumIntervals(soup)+1):
        for l in lowLabels(soup):
            labels.append(l + ' ' + str(i))
    for l in lowLabels(soup):
        labels.append('AVG'+ ' '+  l)
    return labels

def lowLabels(soup):
    labels = list()
    intervals =  soup.find('div', {'class':'intervals panel-detail'})
    table = intervals.find('table')
    header = table.find('tr')
    for title in header.descendants:
        if title.name == 'th':
            labels.append(title.string)
    if labels[-1] == '':
        labels[-1] = 'HR'
    else:
        labels.append('HR')
    return labels

# gets the number of intervals recorded
def getNumIntervals(soup):
    s = soup.find_all(name = 'tr', attrs = 'js-interval')
    return len(s)

def getIntervals(soup):
    intervalInfo = [{},{},{},{},{},{},{}]
    labels = lowLabels(soup)
    interval_panel = soup.find('div', {'class':'intervals panel-detail'})
    table = interval_panel.find('table')
    averages = table.find('tr', {'class':'info'})
    i = 0

    for avg in averages.descendants:
        if avg.name == 'td':
            data = avg.string
            if str.__contains__(data, 'm'): #if data is meters
                 # remove m at the end of the data
                data = data[:-1]
            # Write data to dict element
            intervalInfo[i]['AVG'+ ' '+ labels[i]] = data
            i += 1
    
    intervals = table.find_all('tr', {'class':'js-interval'})
    # Note: there is an unknown number of intervals
    for interval in intervals:
        i = 0 # need to preserve numbering in a weird way b/c HR
        for ele in interval:
            if ele.name == 'td':
                data = ele.string
                if str.__contains__(data, 'm'): #if data is meters
                    # remove m at the end
                    data = data[:-1]
                # Write data to dict element
                intervalInfo[i][labels[i] + ' '+ interval['data-interval']] = data
                i += 1
        # If no HR listed (so there will be no column)
        if len(interval) < len(labels):
            # Add null for dict if no heartrate data
            intervalInfo[i][labels[i] + ' '+ interval['data-interval']] = ''
    return intervalInfo

def getRowers(soup):
    names = list()
    urls = list()
    partner_info = soup.find_all('div', {'class':'partner__info'})
    partner_names = partner_info.find_all('h4')
    for name in partner_names:
        names.append(name.string)
    
    partner_buttons = soup.find_all('div', {'class':'partner__actions'})
    button = partner_buttons.find_all('a', string='View Log')
    for url in button:
        urls.append(url.string)
    dictionary = dict(zip(names, urls))
    return dictionary

def getLogbookUrls(soup, multiples = 0, date=None):
    urls = list()
    # By default, date is today's date
    if date is None:
        date = dt.today().strftime('%m/%d/%Y')
    # Find the URL for today's workout
    tables = soup.find_all('table', {'id':'log-table'})
    workouts = tables.find_all('tr')
    for workout in workouts:
        if workout.find('td', string=date):
            icon = workout.find('td', {'class':'text-center'})
            tag = icon.find('a')
            urls.append(tag['href'])
    return urls

def getWorkoutDetails(soup):
    content = soup.find('section', {'class': 'content'})
    title = content.find('div', {'class', 'col-sm-12 row'})
    workout = title.find('small').string
    return workout

def cullUrls(soup, urls):
    return None
