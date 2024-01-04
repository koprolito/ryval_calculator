from Standard_Calculator_View import *
from Operation import *

#Global variables
ui = Standard_Calculator_View()
main_operator = StringVar()
main_operator.set("0")

secondary_operator = StringVar()
secondary_operator.set("")

operations = StringVar()
operations.set("")

history = StringVar()
history.set("")

pressed_result = 0

def update_main_operator():
    '''Updates the operations_label's text with the current value of the main_operator'''
    ui.operations_label.config(text=main_operator.get())

def update_history():
    '''Updates the operations_history_label with the current value of the history variable.
    If the result_button has been pressed, it means the pressed_result value will be greater than 0, 
    and if that is the case the history will be set to the last number that was pressed after the result given'''
    global history, pressed_result  
    if pressed_result > 0:
        history.set(history.get()[pressed_result::])
        pressed_result = 0
    ui.operations_history_label.config(text=history.get())

#The main_operator will be updated accordingly to the operations that are processed.
#It will be set as the text shown in the operations_label
ui.operations_label.config(text=main_operator.get())

#Add options to the theme_menu. Each option is a different theme for the view
ui.theme_menu.add_command(label="Light mode", command=lambda:ui.light_mode())
ui.theme_menu.add_command(label="Dark mode", command=lambda:ui.dark_mode())
ui.theme_menu.add_command(label="Blue AMOLED mode", command=lambda:ui.blue_amoled_mode())

#Validations for border cases
def validate_indetermination() -> bool:
    '''Validates if the divisor of a division is zero, which causes indetermination.
    Returns True if the operation's divisor is zero and shows a messagebox as a warning for the user.
    Returns False if the operation's divisor is not zero'''    

    global operations
    global main_operator
    if(main_operator.get() == "0"):
        messagebox.showinfo("Error","No se puede divide entre zero")
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
def basic_aritmethical_operations(operation: str) -> None:
    global secondary_operator, main_operator, operations, history
    history.set(history.get()+main_operator.get()+operation)

    if(secondary_operator.get() == ""):
        secondary_operator.set(main_operator.get())
        operations.set(operations.get()+secondary_operator.get()+operation)
    elif(secondary_operator.get() != "" and main_operator.get() != ""): 
        secondary_operator.set(result(False))
        operations.set(secondary_operator.get()+operation)
    main_operator.set("0")
    update_history()
    update_main_operator()

def advanced_arithmetical_operations(operation: str) -> None:
    global main_operator, secondary_operator, operations, history
    #global secondary_operator

    if operation != '%' and operation != 'sqrt':
        history.set(history.get()+main_operator.get()+operation)
    elif operation == 'sqrt':
        history.set(history.get()+f"sqrt({main_operator.get()})")

    if operation == '%':
        if secondary_operator.get() == "":
            history.set("0")
            main_operator.set("0")
            update_history()
            update_main_operator()
        elif secondary_operator.get() != "" and main_operator.get() != "":
            operations.set(operations.get()+"%") 
            secondary_operator.set(result(True))
            operations.set(secondary_operator.get())
    elif operation == '^':
        if operation == '^' and secondary_operator.get() == "":
            secondary_operator.set(main_operator.get())
            operations.set(operations.get()+secondary_operator.get()+"^")
            main_operator.set("0")
        elif operation == '^' and secondary_operator.get() != "" and main_operator.get() != "":
            operations.set(operations.get()+"^")
            secondary_operator.set(result(False))
            operations.set(secondary_operator.get())
        main_operator.set("0") 
        update_history()      
        update_main_operator()
    elif operation == 'sqrt':
        if secondary_operator.get() == "":
            secondary_operator.set(main_operator.get())
            operations.set(operations.get()+secondary_operator.get()+"sqrt")
            secondary_operator.set(result(True))
        elif secondary_operator.get() != "" and main_operator.get() != "":
            operations.set(operations.get()+"sqrt")
            secondary_operator.set(result(True))
        operations.set(secondary_operator.get())

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
    
    for i in range(len(operations.get())):
        if(operations.get()[i] not in "+-xr/^%" and 
           operations.get()[i] in "1234567890." or 
           (i == 0 and operations.get()[i] == "-")):
            cad_num += operations.get()[i]
        elif operations.get()[i:len(operations.get())] == "sqrt":
            sqrt = True
            break
        else:
            break

    if sqrt == True:
        res = str(Operation.squared_root(float(cad_num)).real)

    if '%' in operations.get():
        porcentage = str(Operation.porcentage(float(cad_num),float(main_operator.get())))
        if '+' in operations.get():
            res = str(Operation.sum(float(cad_num),float(porcentage)))
        elif '-' in operations.get():
            res = str(Operation.substract(float(cad_num),float(porcentage)))
        elif 'x' in operations.get():
            res = porcentage
        elif '/' in operations.get():
            if(validate_indetermination() == False):
                res = str(Operation.divide(float(cad_num),float(main_operator.get())/100))
            else:
                return ""
        elif '^' in operations.get():
            res = str(Operation.power(float(cad_num),float(porcentage)))
        if(is_int(porcentage) == False):
            history.set(history.get()+porcentage)
        else:
            history.set(history.get()+porcentage[:porcentage.find(".")])
    else:
        if '+' in operations.get():
            res = str(Operation.sum(float(cad_num),float(main_operator.get())))
        elif 'x' in operations.get():
            res = str(Operation.multiply(float(cad_num),float(main_operator.get())))
        elif '/' in operations.get():
            if(validate_indetermination() == False):
                res = str(Operation.divide(float(cad_num),float(main_operator.get())))
            else:
                return ""
        elif '^' in operations.get():
            res = str(Operation.power(float(cad_num),float(main_operator.get())))
        elif '-' in operations.get():
            res = str(Operation.substract(float(cad_num),float(main_operator.get())))
        elif sqrt == False and '-' not in cad_num:
            res = cad_num
        
    if update == True:
        if sqrt != True and '%' not in operations.get():
            history.set(history.get()+main_operator.get())
        if(is_int(res) == False):
            main_operator.set(res)
        else:
            main_operator.set(res[:res.find(".")])
        update_history()
        pressed_result += len(history.get())
        update_main_operator()

        secondary_operator.set("")
        operations.set("")
    return res

#Logic for the interaction of the buttons with the interface
def button_clicked(c: str):
    global main_operator, pressed_result
    global secondary_operator, history, operations
    #Make sure the button clicked is a number
    if c.isdigit() or c == '.' or c == 'pi' or c == 'e':
        #If the result button has been already pressed and the button pressed recently is
        #not an aritmetical operation
        if pressed_result > 0:
            main_operator.set("0")
            secondary_operator.set('')
            update_history()            
        if(main_operator.get() == '0' and c != '0' and c != '00' and c != '.'):
            if c == 'pi':
                main_operator.set(str(pi))
            elif c == 'e':
                main_operator.set(str(e))
            else:
                main_operator.set(c)
        elif ((main_operator.get() != '0') 
              or (c == '.' and '.' not in main_operator.get())):
            if c == 'pi':
                main_operator.set(str(pi))
            elif c == 'e':
                main_operator.set(str(e))
            else:
                if str(pi) not in main_operator.get() and str(e) not in main_operator.get():
                    if((c == '.' and '.' not in main_operator.get()) or (c != '.')):
                        main_operator.set(main_operator.get()+c)                    
                elif(str(pi) in main_operator.get() or str(e) in main_operator.get() 
                and c != 'pi' and c!= 'e'):
                        if c == '.':
                            main_operator.set('0'+c)
                        else:
                            main_operator.set(c)
        else:
            main_operator.set(main_operator.get())
        update_main_operator()
    else:
        #If the button clicked is not a number it has to be an operation
        if c == '+':
            basic_aritmethical_operations('+')
        elif c == '-':
            basic_aritmethical_operations('-')
        elif c == 'x':
            basic_aritmethical_operations('x')
        elif c == '/':
            basic_aritmethical_operations('/')
        elif c == '^':
            advanced_arithmetical_operations('^')
        elif c == 'sqrt':
            advanced_arithmetical_operations('sqrt')
        elif c == '%':
            advanced_arithmetical_operations('%')
        elif c == '=':
            result(True)
        elif c == 'negate':
            if(main_operator.get() != '0' and main_operator.get() != ''):
                if(main_operator.get()[0] == '-'):
                    main_operator.set(main_operator.get()[1::])
                else:
                    main_operator.set('-'+main_operator.get())
                update_main_operator()
        elif c == 'sqrd':
            if operations.get() != "":
                main_operator.set(result(False))
                if(is_int(main_operator.get()) != False):                
                    main_operator.set(main_operator.get()[:main_operator.get().find(".")])
            operations.set(main_operator.get()+'^')            
            history.set(main_operator.get()+'^')
            main_operator.set('2')
            result(True)
        elif c == '1/x':
            aux = operations.get()
            operations.set('1/')
            history.set(history.get()+'1/'+main_operator.get())
            history_aux = history.get()
            main_operator.set(result(False))
            if(is_int(main_operator.get()) != False):                
                    main_operator.set(main_operator.get()[:main_operator.get().find(".")])
            operations.set(aux)
            aux = main_operator.get()            
            result(True)
            history.set(history_aux)
            pressed_result = 0
            main_operator.set(aux)
            update_main_operator()
            update_history()
            history.set('')


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
ui.one_divided_by_button.config(command=lambda:button_clicked('1/x'))
ui.negative_button.config(command=lambda:button_clicked('negate'))
ui.squared_button.config(command=lambda:button_clicked('sqrd'))
ui.result_button.config(command=lambda:button_clicked('='))

def clean():
    '''Cleans all the operations and history that has been proccessed until the momment by the user'''
    global main_operator, history, operations, secondary_operator
    main_operator.set("0")
    history.set("")
    operations.set("")
    secondary_operator.set("")
    update_main_operator()
    update_history()

ui.clean_button.config(command=clean)

#Logic for the interaction of the keyboard and the UI
def key_pressed(event):
    global main_operator, pressed_result, secondary_operator
    #Make sure the key pressed is not the Shift key
    if event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
        return
    #Make sure the key pressed is a number
    if event.char.isdigit() or event.char == '.' and '.' not in main_operator.get():
        #If the result key has been already pressed and the key pressed recently is
        #not an aritmetical operation
        if pressed_result > 0:
            main_operator.set("0")
            secondary_operator.set("")
            update_history()
        #Add a number to the UI's operator
        if main_operator.get() == '0':
            if event.char == '.' and '.' not in main_operator.get():
                main_operator.set(main_operator.get()+event.char)
            else:
                main_operator.set(event.char)
        else:
            main_operator.set(main_operator.get()+event.char)
        #Update the UI
        update_main_operator()
    else:
        #If the button clicked is not a number it has to be an operation
        if event.char == '+':
            basic_aritmethical_operations('+')
        elif event.char == '-':
            basic_aritmethical_operations('-')
        elif event.char == 'x':
            basic_aritmethical_operations('x')
        elif event.char == '/':
            basic_aritmethical_operations('/')
        elif event.char == '^':
            advanced_arithmetical_operations('^')
        elif event.char == 'r':
            advanced_arithmetical_operations('sqrt')
        elif event.char == '%':
            advanced_arithmetical_operations('%')
        elif event.char == '='or event.keysym == 'Return':
            result(True)

#Bind the keyboard event to the function key_pressed
ui.root.bind('<Key>', key_pressed)
