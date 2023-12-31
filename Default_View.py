from tkinter import *
from tkinter import messagebox

class Default_View:

    def __init__(self):
        #Creation of the root TopLevel widget
        self.root = Tk()
        self.root.iconbitmap("ryval_calculator_icon.ico")
        self.root.title("Ryval Calculator")        

        #Create a menu bar
        self.menu_bar = Menu(self.root)

        #Create an edit view that works as a submenu of menu_bar and allows the user to
        #modify the view of the UI
        self.edit_view = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="View",menu=self.edit_view)

        #Create a theme menu that works as a submenu of edit_view
        self.theme_menu = Menu(self.edit_view, tearoff=0)

        #Add theme_menu to the cascade of edit_view
        self.edit_view.add_cascade(label="Themes", menu=self.theme_menu)       