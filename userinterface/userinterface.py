from userinterface.people import *
from userinterface.about import *
from userinterface.expense import *


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
        self.file_menu.add_command(label="Exit", command=lambda: close_window(self.window))
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.people_menu = Menu(self.menu_bar, tearoff=0)
        self.people_menu.add_command(label="Add", command=lambda: self.open_new_person_window())
        self.menu_bar.add_cascade(label="People", menu=self.people_menu)

        self.expense_menu = Menu(self.menu_bar, tearoff=0)
        self.expense_menu.add_command(label="Add")
        self.menu_bar.add_cascade(label="Expenses", menu=self.expense_menu)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Contribute",
                                   command=lambda: open_web_browser("https://github.com/GuillaumeDmns/cost-balancing"))
        self.help_menu.add_command(label="About", command=self.open_about_window)
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
                                  command=lambda: close_window(self.window)).pack(side=LEFT, padx=5, pady=5)

        self.update_people_list()

        # Edit window
        self.edit_window = None

        # New person window
        self.new_person_window = None

        # New expense window
        self.expense_window = None

        # About window
        self.about_window = None

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
            Button(person_frame, text="Delete " + person.get_name(), fg="red",
                   command=lambda x=person: self.delete_person(x)).pack(side=LEFT, padx=3, pady=3)

    def open_edit_window(self, person):
        self.edit_window = Toplevel(self.window)
        EditPersonWindow(self.edit_window, person)
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

    def delete_person(self, person):
        if askokcancel("Delete person", "Do you really want to delete " + person.get_name() + "?"):
            self.list_of_people.remove(person)
            self.update_people_list()

    def open_about_window(self):
        self.about_window = Toplevel(self.window)
        AboutWindow(self.about_window)
        self.about_window.transient(self.window)
        self.about_window.grab_set()
        self.window.wait_window(self.about_window)

    def open_expense_window(self, person):
        self.expense_window = Toplevel(self.window)
        NewExpenseWindow(self.expense_window)
        self.expense_window.transient(self.window)
        self.expense_window.grab_set()
        self.window.wait_window(self.expense_window)
