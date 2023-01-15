from html.parser import HTMLParser

class HTMLParseDammit(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.startTags = list()
        self.tagAttrs = list()
        self.endTags = list()
        self.startEndTags = list()
        self.comments = list()
        self.data = list()
   
    def handle_starttag(self, tag, attrs):
      self.startTags.append(tag)
      self.tagAttrs.append(list(attrs))
      return tag

    def handle_endtag(self, tag):
        self.endTags.extend(tag)
        return tag

    def handle_data(self, data):
      # print('not functional')
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


