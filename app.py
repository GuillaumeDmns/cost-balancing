from classes.people import *
from userinterface.userinterface import MainWindow, Tk

list_of_people = [People("Guillaume", 25), People("Loïc", 17.3), People("Solène", 72.05)]
add_someone = True

# while add_someone:
#     list_of_people.append(People(input("New name : ")))
#     add_someone = input("Continue ? 1 oui / 0 non : ") == "1"


def main():
    window = Tk()
    main_win = MainWindow(window)
    window.mainloop()


if __name__ == '__main__':
    main()
