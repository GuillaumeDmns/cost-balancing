from tkinter import *
from classes.expense import *


class ExpenseWindow:
    def __init__(self, window, person):
        self.window = window
        self.window.geometry("300x300")
        self.window.resizable(0, 0)

        self.person = person

        self.name_frame = Frame(self.window)
        self.name_caption = Label(self.name_frame, text="Name")
        self.new_name = StringVar()
        self.expense_name = Entry(self.name_frame, textvariable=self.new_name)

        self.amount_frame = Frame(self.window)
        self.amount_caption = Label(self.amount_frame, text="Amount")
        self.new_amount = DoubleVar()
        self.amount = Entry(self.amount_frame, textvariable=self.new_amount)

        self.buttons_frame = Frame(self.window)
        self.cancel_button = Button(self.buttons_frame, text="Cancel", command=lambda: self.window.destroy())

        self.buttons_frame.pack(side="bottom", pady=15)
        self.cancel_button.pack(side=LEFT, padx=5, pady=5)

        self.name_frame.pack(side="top", pady=10)
        self.name_caption.pack()
        self.amount_frame.pack(side="top", pady=10)
        self.amount_caption.pack()

        self.expense_name.pack()
        self.amount.pack()


# class EditExpenseWindow(ExpenseWindow):
#     def __init__(self, edit_window, person):
#         super().__init__(edit_window)
#         self.person = person
#
#         self.validate_button = Button(self.buttons_frame, text="Validate", command=self.validate_edit_person)
#         self.validate_button.pack(side=LEFT, padx=5, pady=5)
#
#         self.people_name.delete(0, END)
#         self.people_name.insert(0, person.get_name())
#         self.people_name.pack()
#
#         self.balance["text"] = person.get_balance()
#         self.balance.pack()
#
#         self.window.title("Edit " + person.get_name() + " profile")
#
#     def validate_edit_person(self):
#         self.person.set_name(self.new_name.get())
#         self.window.destroy()


class NewExpenseWindow(ExpenseWindow):
    def __init__(self, new_expense_window, person):
        super().__init__(new_expense_window, person)

        self.validate_button = Button(self.buttons_frame, text="Validate", command=self.validate_new_expense)
        self.validate_button.pack(side=LEFT, padx=5, pady=5)

        self.window.title("Add an expense for " + str(self.person.get_name()))

    def validate_new_expense(self):
        if self.new_amount.get() > 0:
            self.person.add_expense(Expense(self.new_name.get(), self.new_amount.get()))
            self.window.destroy()
