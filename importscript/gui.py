#This just handles the gui
try:
    from tkinter import Tk
    from tkinter.filedialog import askdirectory
except ImportError:
    print('Import Error for GUI')

