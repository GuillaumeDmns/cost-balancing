from callbackmenu import *
from tkinter import *


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window_width = self.window.winfo_screenwidth() - 400
        self.window_height = self.window.winfo_screenheight() - 400
        self.window.geometry(str(self.window_width) + "x" + str(self.window_height))

        # Menu
        self.menu_bar = Menu(self.window)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Save")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.window.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.people_menu = Menu(self.menu_bar, tearoff=0)
        self.people_menu.add_command(label="Add")
        self.people_menu.add_command(label="Edit")
        self.people_menu.add_command(label="Delete")
        self.menu_bar.add_cascade(label="People", menu=self.people_menu)

        self.expense_menu = Menu(self.menu_bar, tearoff=0)
        self.expense_menu.add_command(label="Add")
        self.expense_menu.add_command(label="Edit")
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
        self.add_button = Button(self.bottom_frame, text="Add a person").pack(side=LEFT, padx=5, pady=5)
        self.quit_button = Button(self.bottom_frame, text="Exit", command=self.window.quit).pack(side=LEFT, padx=5, pady=5)

        self. window.title("Cost Balancing")
        self.window.mainloop()

    def people_list(self, list_of_people):
        for person in list_of_people:  # Display list of people with their balance and actions
            person_frame = Frame(self.people_frame)
            person_frame.pack(side="top", pady=10)
            Label(person_frame, text=person.get_name() + " : " + str(person.get_balance()) + "€") \
                .pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Add an expense").pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Edit " + person.get_name()).pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Delete " + person.get_name(), fg="red").pack(side=LEFT, padx=3, pady=3)