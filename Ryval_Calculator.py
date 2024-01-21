import Default_Components
from PIL import Image, ImageTk

#Global variables
side_panel_active = False

# Main Window
window = Default_Components.ctk.CTk()
window.title('Ryval Calculator')
window.geometry('500x500')
window.iconbitmap('ryval_calculator_icon.ico')

# Functions
def manage_buttons(event=None):
    global side_panel_active
    if not side_panel_active:
        for button in numbers_buttons:
            button.configure(state='disabled')
        side_panel_active = True
    else:
        for button in numbers_buttons:
            button.configure(state='normal')
        side_panel_active = False


#Numbers frame
numbers_frame = Default_Components.NumbersFrame(window, 'gray', 0.0, 0.6)

# Animated Slide Panel
animated_panel = Default_Components.SlidePanel(window, -0.5, 0.1, numbers_frame)

# Slide Panel Button
slide_panel_button = Default_Components.ctk.CTkButton(window, text = '', 
width=50,height=40,command = animated_panel.animate, 
image=Default_Components.ctk.CTkImage(Image.open('sidebar_image.png')))
slide_panel_button.place(anchor = 'nw')
# Bind the disable and enable functions to the slide panel button
slide_panel_button.bind('<Button-1>', lambda event: manage_buttons(event) if animated_panel.is_active else None)

#Number's buttons
# Set the weight for each row and column
for i in range(10):
    numbers_frame.grid_rowconfigure(i, weight=5)
    numbers_frame.grid_columnconfigure(i, weight=5)
# Create and place the buttons
numbers_buttons = []
num = 9
for i in range(10):
    numbers_buttons.append(Default_Components.ctk.CTkButton(numbers_frame, text = str(num-i)))
#Place the buttons
numbers_buttons[0].grid(row = 0, column = 2, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[1].grid(row = 0, column = 1, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[2].grid(row = 0, column = 0, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[3].grid(row = 1, column = 2, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[4].grid(row = 1, column = 1, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[5].grid(row = 1, column = 0, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[6].grid(row = 2, column = 2, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[7].grid(row = 2, column = 1, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[8].grid(row = 2, column = 0, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons[9].grid(row = 3, column = 1, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons.append(Default_Components.ctk.CTkButton(numbers_frame, text = '+/-'))
numbers_buttons[10].grid(row = 3, column = 0, sticky = 'nsew', ipadx = 10, ipady = 15)
numbers_buttons.append(Default_Components.ctk.CTkButton(numbers_frame, text = '.'))
numbers_buttons[11].grid(row = 3, column = 2, sticky = 'nsew', ipadx = 10, ipady = 15)


#Operations frame
operations_frame = Default_Components.OperationsFrame(window, 'gray', 0.6, 0.6)

# Run
window.mainloop()