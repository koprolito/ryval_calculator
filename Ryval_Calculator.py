import Standard_Calculator
import Areas_Calculator
import customtkinter as ctk

# Main Window
window = ctk.CTk()
window.title('Ryval Calculator')
window.geometry('320x450')
window.iconbitmap('ryval_calculator_icon.ico')
window.minsize(320,450)

standard_calculator = Standard_Calculator.Standard_Calculator(window)
standard_calculator.window.mainloop()