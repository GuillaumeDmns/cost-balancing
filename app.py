from classes.people import *
from classes.expense import *
from classes.userinterface import UserInterface

list_of_people = []
add_someone = True

while add_someone:
    list_of_people.append(People(input("New name : ")))
    add_someone = input("Continue ? 1 oui / 0 non : ") == "1"

ui = UserInterface()
