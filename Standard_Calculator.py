import Default_Components
from PIL import Image, ImageTk

# Main Window
window = Default_Components.ctk.CTk()
window.title('Ryval Calculator')
window.geometry('320x450')
window.iconbitmap('ryval_calculator_icon.ico')
window.minsize(320,450)

#Global variables
side_panel_active = False

# Functions
def manage_buttons(event):
    global side_panel_active
    if not side_panel_active:
        for button in numbers_buttons:
            button.configure(state='disabled')
        for button in operations_buttons:
            button.configure(state='disabled')
        side_panel_active = True
    else:
        for button in numbers_buttons:
            button.configure(state='normal')
        for button in operations_buttons:
            button.configure(state='normal')
        side_panel_active = False


#Operations and numbers frame
nums_and_operations_frame = Default_Components.Frame(window, 'transparent', 0.0, 0.3, 1, 0.7)

#Results frame
results_frame = Default_Components.Frame(window, 'transparent', 0.0, 0.0, 1, 0.3)

# Animated Slide Panel
animated_panel = Default_Components.SlidePanel(window, -0.5, 0.1, [nums_and_operations_frame, results_frame])

# Slide Panel Button
slide_panel_button = Default_Components.ctk.CTkButton(window, text = '', 
width=50,height=40,command = animated_panel.animate, 
image=Default_Components.ctk.CTkImage(Image.open('sidebar_image.png')), fg_color='#2a4993')
slide_panel_button.lift(animated_panel)
slide_panel_button.place(anchor = 'nw')
# Bind the disable and enable functions to the slide panel button
slide_panel_button.bind('<Button-1>', lambda event: manage_buttons(event) if animated_panel.is_active else manage_buttons(event))

#Buttons
# Set the weight for each row and column
for i in range(6):
    nums_and_operations_frame.grid_rowconfigure(i, weight=1)
    for j in range(4):
        nums_and_operations_frame.grid_columnconfigure(j, weight=1)

# Set the font for the buttons
#   Define the font
my_font = Default_Components.ctk.CTkFont(family='Helvetica', size=20, weight='bold')


# Create the buttons
numbers_buttons = []
num = 9
for i in range(10):
    numbers_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, text = str(num-i),font=my_font, width=130,height=50, fg_color='#7c87e7'))
numbers_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, text = '+/-', font=my_font, width=130,height=50, fg_color='#191919')) # +/- button
numbers_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, text = '.',font=my_font, width=130,height=50, fg_color='#191919')) # . button
operations_buttons = []
operations_symbols = ['x','-','+','=','%','CE','C','del','1/x','x^2','sqrt','÷']
for i in operations_symbols:
    if i == 'del':
        operations_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, text = '',image=Default_Components.ctk.CTkImage(Image.open('backspace_image.png')),font=my_font, width=130,height=50, fg_color='#2a4993'))
    operations_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, text = i,font=my_font, width=130,height=50, fg_color='#2a4993'))

# Place the buttons
#   Place operations buttons
index = 4    
for i in range(0,2):
    for j in range(0,4):
        operations_buttons[index].grid(row=i,column=j, padx=1, pady=1, sticky='nsew')
        index += 1
index = 0
for i in range(2,6):
    operations_buttons[index].grid(row=i,column=3, padx=1, pady=1, sticky='nsew')
    index += 1
#   Place numbers buttons
index = 0
for i in range(2,6):
    for j in range(0,3):
        numbers_buttons[index].grid(row=i,column=j, padx=1, pady=1, sticky='nsew')
        index += 1