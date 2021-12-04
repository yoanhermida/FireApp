from tkinter import Tk, Label, Button, LEFT

from data import MyData, DatabaseClient


class UserInterface(object):

    # creates root window
    root = Tk(className="FIRE")
    root.geometry("500x500")
    root.title("FIRE Monthly Calculator")

    # window components
    welcome = Label(root, text='Net Worth\n')
    welcome.pack()

    monthly = Label(root, text='Monthly Calculations\n')
    monthly.pack()

    # functions called by buttons
    def get_doc(self):
        data = MyData()
        client = DatabaseClient(db_string=data.db_string,
                                db=data.db_name,
                                collection=data.collection_net_worth)
        collection = client.get_collection()
        doc = collection.find_one()
        return doc

    def exit_app(self):
        self.root.destroy()

    # buttons
    button_get_doc = Button(root, text="Get Document", command=get_doc)
    button_get_doc.pack(side=LEFT)

    button_exit = Button(root, text="Exit", command=exit_app)
    button_exit.pack(side=LEFT)

    # keep gui running
    root.mainloop()
