"""
This program is intended to help me download and import erg data from concept2's website
"""
try:
    import webHandling as wh 
    import htmlParse as parse
    import dataHandling as dh
except ImportError:
    print('Import error in __main__')
#This just handles the gui
try:
    import tkinter as tk
    from tkinter.filedialog import askdirectory
    from tkcalendar import Calendar, DateEntry
except ImportError:
    print('Import Error for GUI')

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    #Create initial widget
    def createWidgets(self):
        self.quitButton = tk.Button(self, text = 'Don\'t press me',
        command=self.quit)
        self.quitButton.grid(column=4)
        
        self.un_label = tk.Label(self, text = 'Gimme your Username')
        self.un_label.grid(column=0)
        self.unVar = tk.StringVar()
        self.un_entry = tk.Entry(self, textvariable=self.unVar)
        self.un_entry.grid(column=0)
        
        self.pw_label = tk.Label(self, text = 'Gimme your Password')
        self.pw_label.grid(column=0)
        self.pwVar = tk.StringVar()
        self.pw_entry = tk.Entry(self, textvariable=self.pwVar)
        self.pw_entry.grid(column=0)

        self.rememberVar = tk.BooleanVar(self)
        self.rememberCB  = tk.Checkbutton(self, text='Remember me',
        variable=self.rememberVar, onvalue='yes', offvalue='no')
        self.rememberCB.grid(row = 5, column=1)

        self.rememberPathB  = tk.Button(self, text='Remember Last Session Parameters',
        command=rememberLast)
        self.rememberPathCB.grid(row = 6, column=1)
        
        def submit(self=self):
            #Triggers submit event outside of the GUI
            return submitB(self)
        
        def rememberLast(self=self):
            #Triggers submit event outside of GUI that pulls old data
            return rememberLastB(self)
        
        self.submitButton = tk.Button(self, text = 'Run da program',
        command= submit)
        self.submitButton.grid(column=4)

        # self.date = Calendar(master=None)
        # cal = DateEntry(self, variable=self.date,width=30,bg="darkblue",fg="white",year=2010)
        # cal.grid()
    
    # Handles when the user asks to use old path that DNE
    def noCredPath(self):
        #TODO: finish this
        print('no credential path exists')

'''
Event handler for when user wants to remember the last session
'''
def rememberLastB(self):
    if not (dh.cred_path()):
        return noCredPath
    path = dh.getCred()['csv path']
    if(path == ''):
        path = askdirectory(title='Please Select a destination Folder') # shows dialog box and return the path
        dh.rewriteCredentials(dh.getCred['username'],dh.getCred['password'],csv_path = path)
        
def submitB(self):
    #Solicit user for input path if not already recorded
    #if user doesn't want credentials to be recorded
    if not (app.rememberPath):
        path = askdirectory(title='Please Select a destination Folder') # shows dialog box and retu

       
    #Writes credentials to permanent file
    else:
        path = askdirectory(title='Please Select a destination Folder') # shows dialog box and return the path
        if(app.rememberVar):
            dh.rewriteCredentials (app.un_entry, app.pw_entry,csvpath=path)
    return 

temp_url = 'https://log.concept2.com/profile/1180585/log/71532822'


# s = wh.startSession()
# p = wh.createParser()
# cred = dh.getCred()
# r = wh.userLoginC2(s, p, cred)
# temp = wh.getReq(s, temp_url)
rParser = wh.createParser()
with open('example-workout.txt', 'r') as f:
    x = f.read()
    rParser.feed(x)
    p = rParser.pullIntervals()
    print(p)





# app = App()                       
# app.master.title('C2 Downloader')
# app.mainloop()

