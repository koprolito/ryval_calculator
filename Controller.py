from Standard_Calculator_View import *
from Operation import *

#Global variables
ui = Standard_Calculator_View()
main_operator = "0"
secondary_operator = ""
operations = ""
history = ""
pressed_result = 0

def update_main_operator():
    '''Updates the operations_label's text with the current value of the main_operator'''
    ui.operations_label.config(text=main_operator)

def update_history():
    '''Updates the operations_history_label with the current value of the history variable.
    If the result_button has been pressed, it means the pressed_result value will be greater than 0, 
    and if that is the case the history will be set to the last number that was pressed after the result given'''
    global history, pressed_result  
    if pressed_result > 0:
        history = history[pressed_result::]
        pressed_result = 0
    ui.operations_history_label.config(text=history)

#The main_operator will be updated accordingly to the operations that are processed.
#It will be set as the text shown in the operations_label
ui.operations_label.config(text=main_operator)

#Functions for changing the UI's color mode
def light_mode():
    '''Sets the UI's components to lighter colors'''
    ui.result_frame.config(bg="white", highlightbackground="black",highlightthickness=1)    
    ui.operations_frame.config(bg="white", highlightbackground="black",highlightthickness=1)
    ui.operations_frame_advnc.config(bg="white", highlightbackground="black",highlightthickness=1)
    ui.numbers_frame.config(bg="white", highlightbackground="black",highlightthickness=1)

    ui.operations_label.config(bg="white", fg="black", highlightbackground="gray")
    ui.operations_history_label.config(bg="white", fg="black", highlightbackground="gray")

    ui.porcentage_button.config(bg="black", fg="white", highlightbackground="gray")
    ui.sqrt_button.config(bg="black", fg="white", highlightbackground="gray")   
    ui.power_button.config(bg="black", fg="white", highlightbackground="gray")   
    ui.division_button.config(bg="black", fg="white", highlightbackground="gray")
    ui.multiplication_button.config(bg="black", fg="white", highlightbackground="gray")
    ui.substraction_button.config(bg="black", fg="white", highlightbackground="gray")
    ui.sum_button.config(bg="black", fg="white", highlightbackground="gray")
    ui.result_button.config(bg="black", fg="white", highlightbackground="gray")

    ui.decimal_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.zero_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.double_zero_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.one_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.two_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.three_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.four_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.five_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.six_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.seven_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.eight_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.nine_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.pi_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.euler_button.config(bg="white", fg="black", highlightbackground="gray")
    ui.clean_button.config(bg="white", fg="black", highlightbackground="gray")

def dark_mode():
    '''Sets the UI's components to darker colors'''
    ui.result_frame.config(bg="black", highlightbackground="white",highlightthickness=1)    
    ui.operations_frame.config(bg="black", highlightbackground="white",highlightthickness=1)
    ui.operations_frame_advnc.config(bg="black", highlightbackground="white",highlightthickness=1)
    ui.numbers_frame.config(bg="black", highlightbackground="white",highlightthickness=1)

    ui.operations_label.config(bg="black", fg="white", highlightbackground="white")
    ui.operations_history_label.config(bg="black", fg="white", highlightbackground="white")

    ui.sqrt_button.config(bg="gray", fg="white", highlightbackground="white")   
    ui.porcentage_button.config(bg="gray", fg="white", highlightbackground="white")   
    ui.power_button.config(bg="gray", fg="white", highlightbackground="white")   
    ui.division_button.config(bg="gray", fg="white", highlightbackground="white")
    ui.multiplication_button.config(bg="gray", fg="white", highlightbackground="white")
    ui.substraction_button.config(bg="gray", fg="white", highlightbackground="white")
    ui.sum_button.config(bg="gray", fg="white", highlightbackground="white")
    ui.result_button.config(bg="gray", fg="white", highlightbackground="white")

    ui.decimal_button.config(bg="black", fg="white", highlightbackground="white")
    ui.zero_button.config(bg="black", fg="white", highlightbackground="white")
    ui.double_zero_button.config(bg="black", fg="white", highlightbackground="white")
    ui.one_button.config(bg="black", fg="white", highlightbackground="white")
    ui.two_button.config(bg="black", fg="white", highlightbackground="white")
    ui.three_button.config(bg="black", fg="white", highlightbackground="white")
    ui.four_button.config(bg="black", fg="white", highlightbackground="white")
    ui.five_button.config(bg="black", fg="white", highlightbackground="white")
    ui.six_button.config(bg="black", fg="white", highlightbackground="white")
    ui.seven_button.config(bg="black", fg="white", highlightbackground="white")
    ui.eight_button.config(bg="black", fg="white", highlightbackground="white")
    ui.nine_button.config(bg="black", fg="white", highlightbackground="white")
    ui.pi_button.config(bg="black", fg="white", highlightbackground="white")
    ui.euler_button.config(bg="black", fg="white", highlightbackground="white")
    ui.clean_button.config(bg="black", fg="white", highlightbackground="white")

def blue_amoled_mode():
    '''Sets the UI's components to blue amoled based colors'''
    ui.result_frame.config(bg="#252440", highlightbackground="white", highlightthickness=1)    
    ui.operations_frame.config(bg="#252440", highlightbackground="white", highlightthickness=1)
    ui.operations_frame_advnc.config(bg="#252440", highlightbackground="white", highlightthickness=1)
    ui.numbers_frame.config(bg="#252440", highlightbackground="white", highlightthickness=1)

    ui.operations_label.config(bg="#252440", fg="white", highlightbackground="white")
    ui.operations_history_label.config(bg="#252440", fg="white", highlightbackground="white")

    ui.sqrt_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    ui.porcentage_button.config(bg="#3CB371", fg="white", highlightbackground="white")   
    ui.power_button.config(bg="#3CB371", fg="white", highlightbackground="white")   
    ui.division_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    ui.multiplication_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    ui.substraction_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    ui.sum_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    ui.result_button.config(bg="#3CB371", fg="white", highlightbackground="white")

    ui.decimal_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.zero_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.double_zero_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.one_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.two_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.three_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.four_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.five_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.six_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.seven_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.eight_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.nine_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.pi_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.euler_button.config(bg="#252440", fg="white", highlightbackground="white")
    ui.clean_button.config(bg="#252440", fg="white", highlightbackground="white")

#Add options to the theme_menu. Each option is a different theme for the view
ui.theme_menu.add_command(label="Light mode", command=lambda:light_mode())
ui.theme_menu.add_command(label="Dark mode", command=lambda:dark_mode())
ui.theme_menu.add_command(label="Blue AMOLED mode", command=lambda:blue_amoled_mode())

#Validations for border cases
def validate_indetermination() -> bool:
    '''Validates if the divisor of a division is zero, which causes indetermination.
    Returns True if the operation's divisor is zero and shows a messagebox as a warning for the user.
    Returns False if the operation's divisor is not zero'''    

    global operations
    global main_operator
    if(main_operator == "0"):
        mb = messagebox.showinfo("Error","No se puede divide entre zero")
        clean()
        return True
    else:
        return False
    
def is_int(num: str) -> bool:
    '''Validates if a float parameter num (as an string value) has no decimal different to zero.
    If the parameter num has a decimal number different to zero the function will return False.
    If the parameter num has no decimal number different to zero the function will return True'''
    for i in range(num.find(".")+1, len(num)):
            if num[i] != "0":
                return False
    return True

#Functions for operating numbers (each corresponds to their respective Button component)
def sum():
    '''Sums the numbers given by the user in the UI'''
    global secondary_operator, main_operator, operations, history
    history += main_operator+"+"

    if(secondary_operator == ""):
        secondary_operator = main_operator
        operations += secondary_operator+"+"
    elif(secondary_operator != "" and main_operator != ""): 
        secondary_operator = result(False)
        operations = secondary_operator+"+" 
    main_operator = "0"
    update_history()
    update_main_operator()

def substract():
    '''Substracts the numbers given by the user in the UI'''
    global secondary_operator, main_operator, operations, history
    history += main_operator+"-"

    if(secondary_operator == ""):
        secondary_operator = main_operator
        operations += secondary_operator+"-"
    elif(secondary_operator != "" and main_operator != ""): 
        secondary_operator = result(False)
        operations = secondary_operator+"-" 
    main_operator = "0"
    update_history()
    update_main_operator()

def multiply():
    '''Multiplies the numbers given by the user in the UI'''
    global secondary_operator, main_operator, operations, history
    history += main_operator+"x"

    if(secondary_operator == ""):
        secondary_operator = main_operator
        operations += secondary_operator+"x"
    elif(secondary_operator != "" and main_operator != ""): 
        secondary_operator = result(False)
        operations = secondary_operator+"x" 
    main_operator = "0"
    update_history()
    update_main_operator()

def divide():
    '''Divides the numbers given by the user in the UI'''
    global secondary_operator, main_operator, operations, history
    history += main_operator+"/"

    if(secondary_operator == ""):
        secondary_operator = main_operator
        operations += secondary_operator+"/"
        main_operator = "0"
    elif(secondary_operator != "" and main_operator != ""):
        secondary_operator = result(False) 
        operations = secondary_operator+"/" 
    main_operator = "0"
    update_history()
    update_main_operator()

def power():
    '''Powers the numbers given by the user in the UI'''
    global secondary_operator, main_operator, operations, history
    history += main_operator+"^"

    if(secondary_operator == ""):
        secondary_operator = main_operator
        operations += secondary_operator+"^"
        main_operator = "0"
    elif(secondary_operator != "" and main_operator != ""):
        operations += "^" 
        secondary_operator = result(False)
        operations = secondary_operator
    main_operator = "0"  
    update_history()      
    update_main_operator()

def porcentage():
    '''Determines the porcentage of the numbers given by the user in the UI'''
    global secondary_operator, main_operator, operations, history

    if(secondary_operator == ""):
        history = "0"
        main_operator = "0"
        update_history()
        update_main_operator()
    elif(secondary_operator != "" and main_operator != ""):
        operations += "%" 
        secondary_operator = result(True)
        operations = secondary_operator

def squared_root():
    '''Determines the squared root of the numbers given by the user in the UI'''
    global secondary_operator, main_operator, operations, history
    history += f"sqrt({main_operator})"

    if(secondary_operator == ""):
        secondary_operator = main_operator
        operations += secondary_operator+"sqrt"
        secondary_operator = result(True)
    elif(secondary_operator != "" and main_operator != ""):
        operations += "sqrt" 
        secondary_operator = result(True)
    operations = secondary_operator 

def result(update: bool) -> str:
    '''Determines the result of a series of operations.
    The boolean parameter update determines if the function should modify the main_operator's value, and 
    returns the result of the operations that were processed.
    If the boolean parameter update is set to True the function will modify the main_operator's value 
    and show it in the UI.
    If the boolean parameter update is set to False the function will not modify the main_operator's value.
    '''
    cad_num = ""
    res = ""
    sqrt = False
    global operations,main_operator, secondary_operator, history, pressed_result
    
    for i in range(len(operations)):
        if(operations[i] not in "+-xr/^%" and 
           operations[i] in "1234567890." or 
           (i == 0 and operations[i] == "-")):
            cad_num += operations[i]
        elif operations[i:len(operations)] == "sqrt":
            sqrt = True
            break
        else:
            break

    if sqrt == True:
        res = str(Operation.squared_root(float(cad_num)).real)

    if '%' in operations:
        porcentage = str(Operation.porcentage(float(cad_num),float(main_operator)))
        if '+' in operations:
            res = str(Operation.sum(float(cad_num),float(porcentage)))
        elif '-' in operations:
            res = str(Operation.substract(float(cad_num),float(porcentage)))
        elif 'x' in operations:
            res = porcentage
        elif '/' in operations:
            if(validate_indetermination() == False):
                res = str(Operation.divide(float(cad_num),float(main_operator)/100))
            else:
                return ""
        elif '^' in operations:
            res = str(Operation.power(float(cad_num),float(porcentage)))
        if(is_int(porcentage) == False):
            history += porcentage
        else:
            history += porcentage[:porcentage.find(".")]
    else:
        if '+' in operations:
            res = str(Operation.sum(float(cad_num),float(main_operator)))
        elif 'x' in operations:
            res = str(Operation.multiply(float(cad_num),float(main_operator)))
        elif '/' in operations:
            if(validate_indetermination() == False):
                res = str(Operation.divide(float(cad_num),float(main_operator)))
            else:
                return ""
        elif '^' in operations:
            res = str(Operation.power(float(cad_num),float(main_operator)))
        elif '-' in operations and operations:
            res = str(Operation.substract(float(cad_num),float(main_operator)))
        elif sqrt == False and '-' not in cad_num:
            res = cad_num
        
    if update == True:
        if sqrt != True and '%' not in operations:
            history += main_operator
        if(is_int(res) == False):
            main_operator = res
        else:
            main_operator = res[:res.find(".")]
        update_history()
        pressed_result += len(history)
        update_main_operator()

        secondary_operator = operations = ""   
    return res

#Logic for the interaction of the buttons with the interface
def button_clicked(c: str):
    global main_operator, pressed_result, n1
    #Make sure the button clicked is a number
    if c.isdigit() or c == '.' or c == 'pi' or c == 'e':
        #If the result button has been already pressed and the button pressed recently is
        #not an aritmetical operation
        if pressed_result > 0:
            main_operator = '0'
            n1 = ''
            update_history()
        if(main_operator == '0' and c != '0' and c != '00' and c != '.'):
            if c == 'pi':
                main_operator = str(pi)
            elif c == 'e':
                main_operator = str(e)
            else:
                main_operator = c
        elif ((main_operator != '0') 
              or (c == '.' and '.' not in main_operator)):
            if c == 'pi':
                main_operator = str(pi)
            elif c == 'e':
                main_operator = str(e)
            else:
                if str(pi) not in main_operator and str(e) not in main_operator:
                    if((c == '.' and '.' not in main_operator) or (c != '.')):
                        main_operator += c                        
                elif(str(pi) in main_operator or str(e) in main_operator 
                and c != 'pi' and c!= 'e'):
                        if c == '.':
                            main_operator = '0'+c
                        else:
                            main_operator = c
        else:
            main_operator = main_operator
        update_main_operator()
    else:
        #If the button clicked is not a number it has to be an operation
        if c == '+':
            sum()
        elif c == '-':
            substract()
        elif c == 'x':
            multiply()
        elif c == '/':
            divide()
        elif c == '^':
            power()
        elif c == 'sqrt':
            squared_root()
        elif c == '%':
            porcentage()
        elif c == '=':
            result(True)

ui.decimal_button.config(command=lambda:button_clicked('.'))
ui.zero_button.config(command=lambda:button_clicked('0'))
ui.double_zero_button.config(command=lambda:button_clicked('00'))
ui.one_button.config(command=lambda:button_clicked('1'))
ui.two_button.config(command=lambda:button_clicked('2'))
ui.three_button.config(command=lambda:button_clicked('3'))
ui.four_button.config(command=lambda:button_clicked('4'))
ui.five_button.config(command=lambda:button_clicked('5'))
ui.six_button.config(command=lambda:button_clicked('6'))
ui.seven_button.config(command=lambda:button_clicked('7'))
ui.eight_button.config(command=lambda:button_clicked('8'))
ui.nine_button.config(command=lambda:button_clicked('9'))
ui.pi_button.config(command=lambda:button_clicked('pi'))
ui.euler_button.config(command=lambda:button_clicked('e'))

ui.sum_button.config(command=lambda:button_clicked('+'))
ui.substraction_button.config(command=lambda:button_clicked('-'))
ui.multiplication_button.config(command=lambda:button_clicked('x'))
ui.division_button.config(command=lambda:button_clicked('/'))
ui.porcentage_button.config(command=lambda:button_clicked('%'))
ui.power_button.config(command=lambda:button_clicked('^'))
ui.sqrt_button.config(command=lambda:button_clicked('sqrt'))
ui.result_button.config(command=lambda:button_clicked('='))

def clean():
    '''Cleans all the operations and history that has been proccessed until the momment by the user'''
    global main_operator, history, operations, secondary_operator
    main_operator = "0"
    history = ""
    operations = secondary_operator = ""    
    update_main_operator()
    update_history()

ui.clean_button.config(command=clean)

#Logic for the interaction of the keyboard and the UI
def key_pressed(event):
    global main_operator, pressed_result, n1
    #Make sure the key pressed is not the Shift key
    if event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
        return
    #Make sure the key pressed is a number
    if event.char.isdigit() or event.char == '.' and '.' not in main_operator:
        #If the result key has been already pressed and the key pressed recently is
        #not an aritmetical operation
        if pressed_result > 0:
            main_operator = '0'
            n1 = ''
            update_history()
        #Add a number to the UI's operator
        if main_operator == '0':
            if event.char == '.' and '.' not in main_operator:
                main_operator = main_operator+event.char
            else:
                main_operator = event.char
        else:
            main_operator += event.char
        #Update the UI
        update_main_operator()
    else:
        #If the button clicked is not a number it has to be an operation
        if event.char == '+':
            sum()
        elif event.char == '-':
            substract()
        elif event.char == 'x':
            multiply()
        elif event.char == '/':
            divide()
        elif event.char == '^':
            power()
        elif event.char == 'r':
            squared_root()
        elif event.char == '%':
            porcentage()
        elif event.char == '=':
            result(True)

#Bind the keyboard event to the function key_pressed
ui.root.bind('<Key>', key_pressed)
