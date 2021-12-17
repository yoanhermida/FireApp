from tkinter import Tk, Label, Button, LEFT, Entry, END

from data import DatabaseClient


class UserInterface:

    client = DatabaseClient("fireapp.db")

    def __init__(self):

        # creates root window
        self.root = Tk(className="fireApp")
        self.root.geometry("500x500")
        self.root.title("FIRE App")

        # window components
        welcome = Label(self.root, text='Net Worth\n')
        welcome.pack()

        # buttons
        button_get_doc = Button(self.root, text="Get Net Worth", command=self.display_records)
        button_get_doc.pack(side=LEFT)

        button_exit = Button(self.root, text="Exit", command=self.exit_app)
        button_exit.pack(side=LEFT)

        # keep gui running
        self.root.mainloop()

    def exit_app(self):
        self.root.destroy()

    def display_records(self):
        r_set = self.client.get_record()
        i = 0
        for r in r_set:
            for j in range(len(r)):
                e = Entry(self.root, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, r[j])
            i += 1
