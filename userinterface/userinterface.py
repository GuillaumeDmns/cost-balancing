from callbackmenu import *
from tkinter import *


class MainWindow:
    def __init__(self, window, list_of_people):
        self.window = window
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
        self.add_button = Button(self.bottom_frame,
                                 text="Add a person",
                                 command=lambda: self.update_people_list(list_of_people)). \
            pack(side=LEFT, padx=5, pady=5)
        self.quit_button = Button(self.bottom_frame, text="Exit",
                                  command=self.window.destroy).pack(side=LEFT, padx=5, pady=5)

        self.update_people_list(list_of_people)

        # Edit window
        self.edit_window = None

        # Mainloop
        self.window.mainloop()

    def update_people_list(self, list_of_people):
        for person in self.people_frame.winfo_children():
            person.destroy()
        for person in list_of_people:  # Display list of people with their balance and actions
            person_frame = Frame(self.people_frame)
            person_frame.pack(side="top", pady=10)
            Label(person_frame, text=person.get_name() + " : " + str(person.get_balance()) + "€") \
                .pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Add an expense").pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Edit " + person.get_name(),
                   command=lambda x=person: self.open_edit_window(x)).pack(side=LEFT, padx=3, pady=3)
            Button(person_frame, text="Delete " + person.get_name(), fg="red").pack(side=LEFT, padx=3, pady=3)

    def open_edit_window(self, person):
        self.edit_window = Toplevel(self.window)
        EditWindow(self.edit_window, person)


class EditWindow:
    def __init__(self, edit_window, person):
        # Edit window
        self.edit_window = edit_window
        self.edit_name_frame = Frame(self.edit_window)
        self.edit_people_caption = Label(self.edit_name_frame, text="Name")
        self.edit_modified_name = StringVar()
        self.edit_people_name = Entry(self.edit_name_frame, textvariable=self.edit_modified_name)
        self.edit_buttons_frame = Frame(self.edit_window)
        self.edit_cancel_button = Button(self.edit_buttons_frame, text="Cancel",
                                         command=self.edit_window.destroy)
        self.edit_validate_button = Button(self.edit_buttons_frame, text="Validate",
                                           command=self.validate_edit_person)

        self.edit_window.title("Edit " + person.get_name() + " profile")

        self.edit_name_frame.pack(side="top", pady=10)
        self.edit_people_caption.pack()
        self.edit_people_name.insert(0, person.get_name())
        self.edit_people_name.pack()

        self.edit_buttons_frame.pack(side="bottom", pady=15)
        self.edit_cancel_button.pack(side=LEFT, padx=5, pady=5)
        self.edit_validate_button.pack(side=LEFT, padx=5, pady=5)

        # self.edit_window.transient(self.window)
        # self.edit_window.grab_set()
        # self.window.wait_window(self.edit_window)

    def validate_edit_person(self):
        # set_name(self.edit_modified_name)
        self.edit_window.destroy()
