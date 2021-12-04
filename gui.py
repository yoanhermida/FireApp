from tkinter import Tk, Label, Button, LEFT, Entry, END

from data import MyData, DatabaseClient


class UserInterface(object):
    
    client = DatabaseClient("fireapp.db")

    # creates root window
    root = Tk(className="fireApp")
    root.geometry("500x500")
    root.title("FIRE App")

    # window components
    welcome = Label(root, text='Net Worth\n')
    welcome.pack()

    def exit_app(self):
        self.root.destroy()

    def display_records(self):
        r_set = MyData(self.client).get_record()
        i = 0
        for r in r_set:
            for j in range(len(r)):
                e = Entry(self.root, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, r[j])
            i += 1

    # buttons
    button_get_doc = Button(root, text="Get Net Worth", command=display_records)
    button_get_doc.pack(side=LEFT)

    button_exit = Button(root, text="Exit", command=exit_app)
    button_exit.pack(side=LEFT)

    # keep gui running
    root.mainloop()
