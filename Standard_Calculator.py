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
def has_decimals(number: str) -> bool:
    '''Returns True if the given number has decimals different to 0'''
    if number.find('.') != -1:
        for i in range(number.find('.')+1, len(number)):
            if number[i] != '0':
                return True
    return False

def to_int(number: str) -> int:
    '''Returns the given number as an integer
    \nIf the number has decimals different to 0, returns the number as a float'''
    if has_decimals(number):
        return float(number)
    else:
        number = number[0:number.find('.')]
        return int(number)

def get_last_numerical_input() -> str:
    '''Returns the last numerical input given by the user'''
    global operations_history_statement
    aux = ''
    #Get the last number given by the user
    for i in reversed(operations_history_statement.get()):
        if(i in '1234567890.' 
           or i == "-" and aux not in "-" and aux != ''):
            aux = i + aux
        elif i not in '1234567890.' and aux != '':
            break
    return aux

def validate_division_by_zero() -> bool:
    '''Returns True if the user has made a division by zero'''
    global current_operation_statement, operations_history_statement
    if current_operation_statement.get() == 'Cannot divide by 0':
        operations_history_statement.set('')
        update_operations_history_statement('')
        current_operation_statement.set('Cannot divide by 0')
        current_operation_statement_label.configure(textvariable=current_operation_statement)
        return True
    return False

def manage_porcentage_operation() -> None:
    '''Manages the porcentage operation'''
    global current_operation_statement, operations_history_statement
     #Validate if the user has already given a number input
    aux_current = current_operation_statement.get() #Bakcup the current operation statement
    if operations_history_statement.get() == "":
        current_operation_statement.set(execute_basic_operation("1", current_operation_statement.get(), '%'))
        operations_history_statement.set(aux_current+"%=")
    else:
        last_numerical_input = get_last_numerical_input()
        porcentage = execute_basic_operation(
            last_numerical_input, current_operation_statement.get(), '%')
        current_operation_statement.set(execute_basic_operation(last_numerical_input, 
            porcentage, operations_history_statement.get()[-1]))
        operations_history_statement.set(operations_history_statement.get()
            +porcentage+"%=")
    update_operations_history_statement("")

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

def manage_brother_panels() -> None:
    '''Manages the brother panels of the main slide panel'''
    global slide_panel, settings_panel
    slide_panel.animate()
    if not slide_panel.is_active():
        settings_panel.animate_backwards()

def update_current_operation_statement(stmt: str) -> None:
    '''Updates the current operation statement label with the given statement
    \nIt operates with the given statement and the current operation statement'''
    global current_operation_statement, operations_flag

    #Validate if the user has exceeded the maximum number of digits (12)
    if(len(current_operation_statement.get()) == 12 and stmt != 'C' and stmt != 'CE' and stmt != 'del'
       and stmt not in '+x÷-=%' and stmt != 'x^2' and stmt != '1/x' and stmt != '√(x)'
       and not operations_flag):
        return None

    #Validate if the user is giving an negation input
    if stmt == '+/-':
        aux_current = current_operation_statement.get() #Bakcup the current operation statement
        current_operation_statement.set(execute_basic_operation('-1', current_operation_statement.get(), 'x'))
        return None

    #Validate if the user has processed a division by zero
    if (validate_division_by_zero() == True
    and stmt != 'C' and stmt != 'CE' 
    and stmt != 'del'):
        return None

    #Validate if the user is giving the very first input
    if(current_operation_statement.get() == '0' 
       and stmt != 'C' and stmt != 'CE' 
       and stmt != 'del' and stmt not in '+x÷-%'
       and stmt != 'x^2' and stmt != '1/x' and stmt != '√(x)'
       and operations_history_statement.get() == ''
       and not operations_flag):
        if(stmt == '.'):
            current_operation_statement.set('0.')
        else:
            current_operation_statement.set(stmt)

    else:

        #Validate if the user is giving an operation input
        if(stmt not in '1234567890.' 
           and operations_history_statement.get() == '' 
           and stmt != 'C' and stmt != 'CE' and stmt != 'del'):
            
            #Validate if the user is giving a % input
            if stmt == "%":
                manage_porcentage_operation()
            
            #Validate if the user is giving a power, squared root or 1-divided-by operation input
            elif(stmt == 'x^2' or stmt == '1/x' or stmt == '√(x)'):
                aux_current = current_operation_statement.get() #Bakcup the current operation statement
                if(stmt == '1/x'):
                    stmt = "1÷x"
                    current_operation_statement.set(execute_basic_operation('1', current_operation_statement.get(), '÷'))
                else:
                    current_operation_statement.set(execute_advanced_operation(current_operation_statement.get(), stmt))
                    
                #Validate if the user has made a division by zero
                if validate_division_by_zero() == True:
                    return None
                
                operations_history_statement.set(stmt.replace('x', aux_current)+"=")
                update_operations_history_statement("")
            else:
                if(operations_history_statement.get() not in '^√'
                and operations_history_statement.get().find("1÷") == -1):
                    operations_history_statement.set(current_operation_statement.get()+stmt)
                else:
                    operations_history_statement.set(current_operation_statement.get())
                    update_operations_history_statement(stmt)
            operations_flag = True
            
        #Validate if the user is giving an operation input after another operation input
        elif (stmt in '+-x÷=%' or stmt == 'x^2' or stmt == '1/x' or stmt == '√(x)'
              and operations_history_statement.get() != ''):
            
            #Validate if the user is giving a % input
            if stmt == "%":
                manage_porcentage_operation()

            #Validate if the user is giving a power, squared root or 1-divided-by operation input
            elif stmt == 'x^2' or stmt == '1/x' or stmt == '√(x)':
                aux_current = current_operation_statement.get() #Bakcup the current operation statement
                if(stmt == '1/x'):
                    stmt = "1÷x"
                    current_operation_statement.set(execute_basic_operation('1', current_operation_statement.get(), '÷'))
                else:
                    current_operation_statement.set(execute_advanced_operation(current_operation_statement.get(), stmt))
                    
                #Validate if the user has made a division by zero
                if validate_division_by_zero() == True:
                    return None
                
                operations_history_statement.set(stmt.replace('x', aux_current)+"=")
                update_operations_history_statement("")
            else:
                aux = get_last_numerical_input()

                #Backup the values of the statements
                op_history_aux = operations_history_statement.get()
                current_statement_aux = current_operation_statement.get()
                #Validate if the user is giving an operation input after a result input
                if operations_history_statement.get().find('=') == -1:
                    current_operation_statement.set(execute_basic_operation(aux, 
                    current_operation_statement.get(), op_history_aux[-1]))                
                    #Validate if the user has made a division by zero
                    if validate_division_by_zero() == True:
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

        elif stmt == 'del':
            current_operation_statement.set(current_operation_statement.get()[0:-1])
            if current_operation_statement.get() == '':
                current_operation_statement.set('0')

        else:
            #Validate if the user is giving an numerical input and if the user has already
            #given an operation input
            if stmt in '1234567890.' and operations_flag:
                if current_operation_statement.get().find('.') == -1 and stmt == '.':
                    current_operation_statement.set(current_operation_statement.get()+stmt)
                elif current_operation_statement.get().find('.') != -1 and stmt == '.':
                    return None
                else:
                    current_operation_statement.set(stmt)
                operations_flag = False
            elif stmt in '1234567890.':
                if current_operation_statement.get().find('.') != -1 and stmt == '.':
                    return None
                else:
                    if current_operation_statement.get() == '0':
                        current_operation_statement.set(stmt)
                    else:
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

def execute_basic_operation(float_str_1: str, float_str_2: str, operation: str) -> str:
    '''Executes the given basic arithmetical operation with the given numbers and returns the result'''

    result = ''
    if operation == '+':
        result = str(to_int(str(Operation.Operation.sum(float(float_str_1), float(float_str_2)))))
    elif operation == '-':
        result = str(to_int(str(Operation.Operation.substract(float(float_str_1), float(float_str_2)))))
    elif operation == 'x':
        result = str(to_int(str(Operation.Operation.multiply(float(float_str_1), float(float_str_2)))))
    elif operation == '÷':
        result = str(to_int(str(Operation.Operation.divide(float(float_str_1), float(float_str_2)))))
    elif operation == '%':
        result = str(to_int(str(Operation.Operation.porcentage(float(float_str_1), float(float_str_2)))))
    
    return result

def execute_advanced_operation(float_str_1: str, operation: str) -> str:
    '''Executes the given basic arithmetical operation with the given numbers and returns the result'''

    result = ''
    if operation == '√(x)':
        result = str(str(Operation.Operation.squared_root(float(float_str_1))))
    elif operation == 'x^2':
        result = str(str(Operation.Operation.power(float(float_str_1),2)))

    #Validate if the result contains parenthesis
    if result[0] == "(":
        result = result.replace('(', '')
        result = result.replace(')', '')

    #Validate if the result contains a comlpex number
    if result.find('j') != -1:
         result = result[0:result.find('+')]

    #Validate if the result is an integer
    result = str(to_int(result))
         
    return result

#Frames
#   Operations and numbers frame
nums_and_operations_frame = Default_Components.Frame(window, 'transparent', 0.0, 0.3, 1, 0.7)

#   Results frame
results_frame = Default_Components.Frame(window, 'transparent', 0.0, 0.0, 1, 0.3)

#   Animated Slide Panels
#       Settings Panel
settings_panel = Default_Components.SettingsPanel(window, -0.5, 0.46, [nums_and_operations_frame, results_frame])
#       Main Slide Panel
slide_panel = Default_Components.SlidePanel(window, -0.5, 0.1, [nums_and_operations_frame, results_frame], settings_panel.animate)

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
width=50,height=40,command = manage_brother_panels, 
image=Default_Components.ctk.CTkImage(Image.open('sidebar_image.png')), fg_color='#2a4993', hover_color='#233F83')
slide_panel_button.lift(slide_panel)
slide_panel_button.place(anchor = 'nw')
# Bind the disable and enable functions to the slide panel button
slide_panel_button.bind('<Button-1>', lambda event: manage_buttons(event) if slide_panel.is_active else manage_buttons(event))

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
operations_symbols = ['x','-','+','=','%','CE','C','del','1/x','x^2','√(x)','÷']
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