from tkinter import Tk, Label, Button, LEFT, Entry, END, ttk

from data import DatabaseClient


class UserInterface:

    client = DatabaseClient("fireapp.db")

    def __init__(self):

        # creates root window
        self.root = Tk(className="FireApp")
        self.root.geometry("500x500")
        self.root.title("FireApp")

        # window components
        main = ttk.Frame(self.root, padding=10)
        main.grid()
        # ttk.Label(main, text="FireApp").grid(column=0, row=0)

        # buttons
        ttk.Button(main, text="Net Worth", command=self.display_records).grid(column=0, row=1)
        ttk.Button(main, text="Exit", command=self.exit_app).grid(column=1, row=1)

        # keep gui running
        self.root.mainloop()

    def exit_app(self):
        self.root.destroy()

    def display_records(self):
        r_set = self.client.get_record()
        i = 1
        for r in r_set:
            for j in range(len(r)):
                e = Entry(self.root, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, r[j])
            i += 1
