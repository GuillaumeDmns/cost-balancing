from classes.people import *
from classes.expense import *
from callbackmenu import *
from tkinter import *

list_of_people = []
add_someone = True

while add_someone:
    list_of_people.append(People(input("Nouveau nom : ")))
    add_someone = input("Continuer ? 1 oui / 0 non : ") == "1"

print("Liste des personnes : ")
for people in list_of_people:
    print(people.get_name())

window = Tk()
window_width = window.winfo_screenwidth() - 400
window_height = window.winfo_screenheight() - 400
window.geometry(str(window_width) + "x" + str(window_height))

# Menu
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

people_menu = Menu(menu_bar, tearoff=0)
people_menu.add_command(label="Add")
people_menu.add_command(label="Edit")
people_menu.add_command(label="Delete")
menu_bar.add_cascade(label="People", menu=people_menu)

expense_menu = Menu(menu_bar, tearoff=0)
expense_menu.add_command(label="Add")
expense_menu.add_command(label="Edit")
expense_menu.add_command(label="Delete")
menu_bar.add_cascade(label="Expenses", menu=expense_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Contribute", command=lambda: openwebbrower("https://github.com/GuillaumeDmns/cost-balancing"))
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

for person in list_of_people:
    Label(window, text=person.get_name()).pack()

bottom_frame = Frame(window)
bottom_frame.pack(side="bottom", pady=15)
add_button = Button(bottom_frame, text="Add a person").pack(side=LEFT, padx=5, pady=5)
quit_button = Button(bottom_frame, text="Exit", command=window.quit).pack(side=LEFT, padx=5, pady=5)

window.title("Cost Balancing")
window.mainloop()