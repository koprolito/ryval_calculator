import Default_Components

# Main Window
window = Default_Components.ctk.CTk()
window.title('Ryval Calculator')
window.geometry('320x450')
window.iconbitmap('ryval_calculator_icon.ico')
window.minsize(320,450)

standard_calculator = Default_Components.BasicCalculator(window)

standard_calculator.window.mainloop()