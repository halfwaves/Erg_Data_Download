"""
This program is intended to help me download and import erg data from concept2's website
"""
from getpass import getpass
import webHandling as wh
from tkinter import Tk
from tkinter.filedialog import askdirectory
# except ImportError:
#     print("Python Import Error")
# except:
#     print("Something went wrong when loading the file. Talk to Newton")


form_data = {'username':'newton145', 'pw':'bvq8fvp2rza2RYQ@pep'}


t = Tk.TopLevel
path = askdirectory(title='Please Select a destination Folder') # shows dialog box and return the path
print(path)  