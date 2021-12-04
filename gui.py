from tkinter import Tk, Label, Button, LEFT

from data import MyData, DatabaseClient


class UserInterface(object):

    client = DatabaseClient("fireapp.db")

    # creates root window
    root = Tk(className="FIRE")
    root.geometry("500x500")
    root.title("FIRE Monthly Calculator")

    # window components
    welcome = Label(root, text='Net Worth\n')
    welcome.pack()

    def exit_app(self):
        self.root.destroy()

    # buttons
    button_get_doc = Button(root, text="Get Net Worth", command=MyData(client).get_record())
    button_get_doc.pack(side=LEFT)

    button_exit = Button(root, text="Exit", command=exit_app)
    button_exit.pack(side=LEFT)

    # keep gui running
    root.mainloop()
