import Default_Components
import Operation
from PIL import Image, ImageTk

# Main Window
window = Default_Components.ctk.CTk()
window.title('Ryval Calculator')
window.geometry('320x450')
window.iconbitmap('ryval_calculator_icon.ico')
window.minsize(320,450)

#Global variables
side_panel_active = False #Determines if the side panel is active or not
current_operation_statement = Default_Components.ctk.StringVar() #Stores the current operation statement
current_operation_statement.set('0') #Initialize the current operation statement with '0'
operations_history_statement = Default_Components.ctk.StringVar() #Stores the operations history statement
operations_flag = False #True if the user has already pressed an operation button
#Define the font for the whole program
my_font = Default_Components.ctk.CTkFont(family='Helvetica', size=20, weight='bold')

# Functions
def manage_buttons(event) -> None:
    '''Disable or enable the buttons when the slide panel is active'''
    global side_panel_active
    if not side_panel_active:
        for button in number_buttons:
            button.configure(state='disabled')
        for button in operation_buttons:
            button.configure(state='disabled')
        side_panel_active = True
    else:
        for button in number_buttons:
            button.configure(state='normal')
        for button in operation_buttons:
            button.configure(state='normal')
        side_panel_active = False

def update_current_operation_statement(stmt: str) -> None:
    '''Updates the current operation statement label with the given statement'''
    global current_operation_statement, operations_flag

    #Validate if the user has processed a division by zero
    if (current_operation_statement.get() == 'Cannot divide by 0' 
    and stmt != 'C' and stmt != 'CE' 
    and stmt != 'del'):
        return None

    #Validate if the user is giving the very first input
    if(current_operation_statement.get() == '0' 
       and stmt != 'C' and stmt != 'CE' 
       and stmt != 'del' and stmt not in '+x÷-%'
       and stmt != 'x^2' and stmt != '1/x' and stmt != 'sqrt'
       and operations_history_statement.get() == ''):
        current_operation_statement.set(stmt)

    else:

        #Validate if the user is giving an operation input
        if(stmt not in '1234567890.' 
           and operations_history_statement.get() == '' 
           and stmt != 'C' and stmt != 'CE' and stmt != 'del'):
            update_operations_history_statement(current_operation_statement.get()+stmt)
            operations_flag = True
            
        #Validate if the user is giving an operation input after another operation input
        elif((stmt in '+-x÷=%' or stmt == 'x^2' 
              or stmt == '1/x' 
              or stmt == 'sqrt') 
              and operations_history_statement.get() != ''):
            aux = ''
            #Get the last number given by the user
            for i in reversed(operations_history_statement.get()):
                if i in '1234567890.':
                    aux = i + aux
                elif i not in '1234567890.' and aux != '':
                    break

            #Backup the values of the statements
            op_history_aux = operations_history_statement.get()
            current_statement_aux = current_operation_statement.get()
            #Validate if the user is giving an operation input after a result input
            if operations_history_statement.get().find('=') == -1:
                current_operation_statement.set(execute_operation(aux, 
                current_operation_statement.get(), op_history_aux[-1]))                
                #Validate if the user has made a division by zero
                if current_operation_statement.get() == 'Cannot divide by 0':
                    operations_history_statement.set('')
                    update_current_operation_statement('')
                    current_operation_statement.set('Cannot divide by 0')
                    current_operation_statement_label.configure(textvariable=current_operation_statement)
                    return None


            #Validate if the user is giving an operation input after another operation input
            #different to '='
            if stmt != '=':
                operations_history_statement.set('')
                update_operations_history_statement(current_operation_statement.get()+stmt)
                current_operation_statement.set(current_statement_aux)
            else:
                operations_history_statement.set('')
                update_operations_history_statement(op_history_aux+current_statement_aux+stmt)
            operations_flag = True

        #Validate if the user is giving an 'clear operations' input
        elif stmt == 'C':
            current_operation_statement.set('0')
            operations_history_statement.set('')

        #Validate if the user is giving an 'clear current operator' input
        elif stmt == 'CE':
            current_operation_statement.set('0')

        else:
            #Validate if the user is giving an numerical input and if the user has already
            #given an operation input
            if stmt in '1234567890.' and operations_flag:
                current_operation_statement.set(stmt)
                operations_flag = False
            elif stmt in '1234567890.':
                current_operation_statement.set(current_operation_statement.get()+stmt)


    #Update the current operation statement label
    current_operation_statement_label.configure(textvariable=current_operation_statement)

def update_operations_history_statement(stmt: str) -> None:
    '''Updates the operations history statement label with the given statement'''

    global operations_history_statement

    #Validate if the user is giving the very first input
    if(operations_history_statement.get() == ''):
        operations_history_statement.set(stmt)
    else:
        operations_history_statement.set(operations_history_statement.get()+stmt)
    operations_history_statement_label.configure(textvariable=operations_history_statement)

def execute_operation(float_str_1: str, float_str_2: str, operation: str) -> str:
    '''Executes the given operation with the given numbers and returns the result'''

    result = ''
    if operation == '+':
        result = str(Operation.Operation.sum(float(float_str_1), float(float_str_2)))
    elif operation == '-':
        result = str(Operation.Operation.substract(float(float_str_1), float(float_str_2)))
    elif operation == 'x':
        result = str(Operation.Operation.multiply(float(float_str_1), float(float_str_2)))
    elif operation == '÷':
        result = str(Operation.Operation.divide(float(float_str_1), float(float_str_2)))
    
    return result

#Frames
#   Operations and numbers frame
nums_and_operations_frame = Default_Components.Frame(window, 'transparent', 0.0, 0.3, 1, 0.7)

#   Results frame
results_frame = Default_Components.Frame(window, 'transparent', 0.0, 0.0, 1, 0.3)

#   Animated Slide Panel
animated_panel = Default_Components.SlidePanel(window, -0.5, 0.1, [nums_and_operations_frame, results_frame])

#Labels
#   Number statement label
current_operation_statement_label = Default_Components.Label(results_frame, 
    current_operation_statement, my_font, 0.95, 0.85, 'se')
my_font = Default_Components.ctk.CTkFont(family='Helvetica', size=14, weight='bold')
operations_history_statement_label = Default_Components.Label(results_frame,
    operations_history_statement, my_font, 0.91, 0.45, 'se')
my_font = Default_Components.ctk.CTkFont(family='Helvetica', size=20, weight='bold')


#Buttons
# Slide Panel Button
slide_panel_button = Default_Components.ctk.CTkButton(window, text = '', 
width=50,height=40,command = animated_panel.animate, 
image=Default_Components.ctk.CTkImage(Image.open('sidebar_image.png')), fg_color='#2a4993', hover_color='#233F83')
slide_panel_button.lift(animated_panel)
slide_panel_button.place(anchor = 'nw')
# Bind the disable and enable functions to the slide panel button
slide_panel_button.bind('<Button-1>', lambda event: manage_buttons(event) if animated_panel.is_active else manage_buttons(event))

# Set the weight for each row and column
for i in range(6):
    nums_and_operations_frame.grid_rowconfigure(i, weight=1)
    for j in range(4):
        nums_and_operations_frame.grid_columnconfigure(j, weight=1)


# Create the buttons
#   Create number buttons
number_buttons = []
num = 9
for i in range(10):
    button = Default_Components.ctk.CTkButton(
        nums_and_operations_frame, text = str(num-i),
        font=my_font, width=130,height=50, 
        fg_color='#7c87e7', hover_color='#6B78D3',
        command=lambda aux = num-i:update_current_operation_statement(str(aux)))
    number_buttons.append(button) # 9-0 buttons
number_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, 
    text = '+/-', font=my_font, width=130,
    height=50, fg_color='#2A2A2A', hover_color='#191919',
    command=lambda aux = '+/-':update_current_operation_statement(aux))) # +/- button
number_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, 
    text = '.',font=my_font, width=130,
    height=50, fg_color='#2A2A2A', hover_color='#191919',
    command=lambda aux = '.':update_current_operation_statement(aux))) # . button

#   Create operation buttons
operation_buttons = []
operations_symbols = ['x','-','+','=','%','CE','C','del','1/x','x^2','sqrt','÷']
for i in operations_symbols:
    if i == 'del':
        operation_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, text = '',
            image=Default_Components.ctk.CTkImage(Image.open('backspace_image.png')),
            font=my_font, width=130,height=50, fg_color='#2a4993', hover_color='#233F83'))
    else:
        operation_buttons.append(Default_Components.ctk.CTkButton(nums_and_operations_frame, 
        text = i,font=my_font, width=130,height=50, 
        fg_color='#2a4993', hover_color='#233F83'))

# Place the buttons
#   Place operations buttons
index = 4    
for i in range(0,2):
    for j in range(0,4):
        operation_buttons[index].grid(row=i,column=j, padx=1, pady=1, sticky='nsew')
        operation_buttons[index].bind('<Button-1>', lambda event, aux = operations_symbols[index]:update_current_operation_statement(aux))
        index += 1
index = 0
for i in range(2,6):
    operation_buttons[index].grid(row=i,column=3, padx=1, pady=1, sticky='nsew')
    operation_buttons[index].bind('<Button-1>', lambda event, aux = operations_symbols[index]:update_current_operation_statement(aux))
    index += 1
#   Place numbers buttons
index = 0
for i in range(2,6):
    for j in range(0,3):
        number_buttons[index].grid(row=i,column=j, padx=1, pady=1, sticky='nsew')
        index += 1