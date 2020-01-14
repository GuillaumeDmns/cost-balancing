from tkinter import *
from utils import *

class AboutWindow:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0, 0)

        self.license = Label(self.window, text="MIT License", fg="blue", cursor="hand2")
        self.license.pack(side="top", padx=10, pady=5)
        self.license.bind("<Button-1>", lambda e: open_web_browser("https://choosealicense.com/licenses/mit/"))

        self.frame_made_by = Frame(self.window)
        self.made_by = Label(self.frame_made_by, text="Made with ♥ by")
        self.made_by.pack(side=LEFT, padx=0, pady=0)
        self.me = Label(self.frame_made_by, text="Guillaume Damiens", fg="blue", cursor="hand2")
        self.me.pack(side=RIGHT, padx=0, pady=0)
        self.me.bind("<Button-1>", lambda e: open_web_browser("https://github.com/GuillaumeDmns"))
        self.frame_made_by.pack(padx=10, pady=10)

        self.window.title("About cost-balancing")
