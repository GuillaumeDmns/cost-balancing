from classes.people import *
from userinterface.userinterface import MainWindow, Tk


def main():
    window = Tk()
    main_win = MainWindow(window)
    window.mainloop()


if __name__ == '__main__':
    main()
