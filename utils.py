import webbrowser
from tkinter.messagebox import *


def open_web_browser(url):
    webbrowser.open_new_tab(url)


def close_app(window):
    if askokcancel("Exit", "Do you really want to exit ?"):
        window.destroy()
