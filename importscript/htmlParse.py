from html.parser import HTMLParser
from bs4 import SoupStrainer as strainer
from bs4 import BeautifulSoup
import lxml
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
    for child in soup.find('div', {'class':'intervals panel-detail'}).descendants:
        if child.name == 'table':
            for el in child.descendants:
                if el.name == 'th':
                    labels.append(el.string)
    labels[-1]= 'HR'
    return labels

# gets the number of intervals recorded
def getNumIntervals(soup):
    s = soup.find_all(name = 'tr', attrs = 'js-interval')
    return len(s)

def getIntervals(soup):
    intervalInfo = [{},{},{},{},{},{},{}]
    labels = lowLabels(soup)
    papa = soup.find('div', {'class':'intervals panel-detail'})
    mama = papa.contents[1] 
    child = mama.find('tr', {'class':'info'})
    i = 0
    for bb in child.descendants:
        if bb.name == 'td':
            intervalInfo[i]['AVG'+ ' '+ labels[i]] = bb.contents
            i += 1
    
    oopsie = mama.find_all('tr', {'class':'js-interval'})
    for child in oopsie:
        i = 0
        for o in child:
            if o.name == 'td':
                intervalInfo[i][labels[i] + ' '+ child['data-interval']] = o.contents
                i += 1
    return intervalInfo

def getRowers(soup):
    names = list()
    urls = list()
    for child in soup.find_all('div', {'class':'partner__info'}).descendants:
        if child.name == 'h4':
            names.append(child.string)
    
    for child in soup.find('div', {'class':'partner__actions'}).descendants:
        if child.name == 'a':
            for l in child.descendants:
                if l.strin == 'View Log':
                    urls.append(l.string)
    dictionary = dict(zip(names, urls))
    return dictionary
