from tkinter import *
from classes.people import *


class PersonWindow:
    def __init__(self, window):
        self.window = window
        self.window.geometry("300x300")
        self.window.resizable(0, 0)

        self.name_frame = Frame(self.window)
        self.people_caption = Label(self.name_frame, text="Name")
        self.new_name = StringVar()
        self.people_name = Entry(self.name_frame, textvariable=self.new_name)

        self.balance_frame = Frame(self.window)
        self.balance_caption = Label(self.balance_frame, text="Expenses")
        self.new_balance = DoubleVar()
        self.balance = Label(self.balance_frame, text=str(self.new_balance.get()) + "€")

        self.buttons_frame = Frame(self.window)
        self.cancel_button = Button(self.buttons_frame, text="Cancel", command=lambda: self.window.destroy())

        self.buttons_frame.pack(side="bottom", pady=15)
        self.cancel_button.pack(side=LEFT, padx=5, pady=5)

        self.name_frame.pack(side="top", pady=10)
        self.people_caption.pack()
        self.balance_frame.pack(side="top", pady=10)
        self.balance_caption.pack()

        self.people_name.pack()
        self.balance.pack()


class EditPersonWindow(PersonWindow):
    def __init__(self, edit_window, person):
        super().__init__(edit_window)
        self.person = person

        self.validate_button = Button(self.buttons_frame, text="Validate", command=self.validate_edit_person)
        self.validate_button.pack(side=LEFT, padx=5, pady=5)

        self.people_name.delete(0, END)
        self.people_name.insert(0, person.get_name())
        self.people_name.pack()

        self.balance["text"] = person.get_balance()
        self.balance.pack()

        self.window.title("Edit " + person.get_name() + " profile")

    def validate_edit_person(self):
        self.person.set_name(self.new_name.get())
        self.window.destroy()


class NewPersonWindow(PersonWindow):
    def __init__(self, new_person_window, list_of_people):
        super().__init__(new_person_window)
        self.list_of_people = list_of_people

        self.validate_button = Button(self.buttons_frame, text="Validate", command=self.validate_new_person)
        self.validate_button.pack(side=LEFT, padx=5, pady=5)

        self.window.title("Create a new profile")

    def validate_new_person(self):
        self.list_of_people.append(People(self.new_name.get(), self.new_balance.get()))
        self.window.destroy()
