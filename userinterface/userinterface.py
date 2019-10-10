from callbackmenu import *
from tkinter import *
from classes.people import *


class MainWindow:
    def __init__(self, window):
        self.window = window
        self.list_of_people = []
        self.window.title("Cost Balancing")
        self.window_width = self.window.winfo_screenwidth() - 400
        self.window_height = self.window.winfo_screenheight() - 400
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height))

        # Menu
        self.menu_bar = Menu(self.window)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.window.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.people_menu = Menu(self.menu_bar, tearoff=0)
        self.people_menu.add_command(label="Add", command=lambda: self.open_new_person_window())
        self.people_menu.add_command(label="Edit")
        self.people_menu.add_command(label="Delete")
        self.menu_bar.add_cascade(label="People", menu=self.people_menu)

        self.expense_menu = Menu(self.menu_bar, tearoff=0)
        self.expense_menu.add_command(label="Add")
        self.expense_menu.add_command(label="Delete")
        self.menu_bar.add_cascade(label="Expenses", menu=self.expense_menu)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Contribute",
                                   command=lambda: open_web_browser("https://github.com/GuillaumeDmns/cost-balancing"))
        self.help_menu.add_command(label="About")
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.window.config(menu=self.menu_bar)

        # Display of people's names
        self.people_frame = Frame(self.window)
        self.people_frame.pack(side="top", pady=10)

        # Bottom buttons
        self.bottom_frame = Frame(self.window)
        self.bottom_frame.pack(side="bottom", pady=15)
        self.add_button = Button(self.bottom_frame,
                                 text="Add a person",
                                 command=lambda: self.open_new_person_window()). \
            pack(side=LEFT, padx=5, pady=5)
        self.quit_button = Button(self.bottom_frame, text="Exit",
                                  command=self.window.destroy).pack(side=LEFT, padx=5, pady=5)

        self.update_people_list()

        # Edit window
        self.edit_window = None

        # New person window
        self.new_person_window = None

        # Mainloop
        self.window.mainloop()

    def update_people_list(self):
        for person in self.people_frame.winfo_children():
            person.destroy()
        for person in self.list_of_people:  # Display list of people with their balance and actions
            person_frame = Frame(self.people_frame)
            person_frame.pack(side="top", pady=10)
            Label(person_frame, text=person.get_name() + " : " + str(person.get_balance()) + "€ spent") \
                .pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Add an expense").pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Edit " + person.get_name(),
                   command=lambda x=person: self.open_edit_window(x)).pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Delete " + person.get_name(), fg="red").pack(side=LEFT, padx=3, pady=3)

    def open_edit_window(self, person):
        self.edit_window = Toplevel(self.window)
        EditWindow(self.edit_window, person)
        self.edit_window.transient(self.window)
        self.edit_window.grab_set()
        self.window.wait_window(self.edit_window)
        self.update_people_list()

    def open_new_person_window(self):
        self.new_person_window = Toplevel(self.window)
        NewPersonWindow(self.new_person_window, self.list_of_people)
        self.new_person_window.transient(self.window)
        self.new_person_window.grab_set()
        self.window.wait_window(self.new_person_window)
        self.update_people_list()


class PersonWindow:
    def __init__(self, window):
        # Edit window
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
        self.cancel_button = Button(self.buttons_frame, text="Cancel", command=self.window.destroy)

        self.buttons_frame.pack(side="bottom", pady=15)
        self.cancel_button.pack(side=LEFT, padx=5, pady=5)

        self.name_frame.pack(side="top", pady=10)
        self.people_caption.pack()
        self.balance_frame.pack(side="top", pady=10)
        self.balance_caption.pack()

        self.people_name.pack()
        self.balance.pack()


class EditWindow(PersonWindow):
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

