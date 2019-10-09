from classes.people import *
from userinterface.userinterface import MainWindow, Tk

list_of_people = [People("Guillaume"), People("Marcos"), People("Adrien")]
add_someone = True

# while add_someone:
#     list_of_people.append(People(input("New name : ")))
#     add_someone = input("Continue ? 1 oui / 0 non : ") == "1"


def main():
    window = Tk()
    main_win = MainWindow(window, list_of_people)
    window.mainloop()


if __name__ == '__main__':
    main()
