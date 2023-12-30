from tkinter import *
from tkinter import messagebox
from Operation import *

#Creation of the root TopLevel widget
root = Tk()
root.iconbitmap("ryval_calculator_icon.ico")
root.title("Calculadora")
root.resizable(0,0)

#Create a menu bar
menu_bar = Menu(root)

#Create an edit view that works as a submenu of menu_bar and allows the user to
#modify the view of the UI
edit_view = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View",menu=edit_view)

#Create a theme menu that works as a submenu of edit_view
theme_menu = Menu(edit_view, tearoff=0)

#Add options to the theme_menu. Each option is a different theme for the view
theme_menu.add_command(label="Light mode", command=lambda:light_mode())
theme_menu.add_command(label="Dark mode", command=lambda:dark_mode())
theme_menu.add_command(label="Blue AMOLED mode", command=lambda:blue_amoled_mode())

#Add theme_menu to the cascade of edit_view
edit_view.add_cascade(label="Themes", menu=theme_menu)

#Functions for changing the UI's color mode
def light_mode():
    '''Sets the UI's components to lighter colors'''
    result_frame.config(bg="white", highlightbackground="black",highlightthickness=1)    
    operations_frame.config(bg="white", highlightbackground="black",highlightthickness=1)
    numbers_frame.config(bg="white", highlightbackground="black",highlightthickness=1)

    operations_label.config(bg="white", fg="black", highlightbackground="gray")
    operations_history_label.config(bg="white", fg="black", highlightbackground="gray")

    porcentage_button.config(bg="black", fg="white", highlightbackground="gray")
    sqrt_button.config(bg="black", fg="white", highlightbackground="gray")   
    power_button.config(bg="black", fg="white", highlightbackground="gray")   
    division_button.config(bg="black", fg="white", highlightbackground="gray")
    multiplication_button.config(bg="black", fg="white", highlightbackground="gray")
    substraction_button.config(bg="black", fg="white", highlightbackground="gray")
    sum_button.config(bg="black", fg="white", highlightbackground="gray")
    result_button.config(bg="black", fg="white", highlightbackground="gray")

    boton_zero.config(bg="white", fg="black", highlightbackground="gray")
    boton_double_zero.config(bg="white", fg="black", highlightbackground="gray")
    boton_one.config(bg="white", fg="black", highlightbackground="gray")
    boton_two.config(bg="white", fg="black", highlightbackground="gray")
    boton_three.config(bg="white", fg="black", highlightbackground="gray")
    boton_four.config(bg="white", fg="black", highlightbackground="gray")
    boton_five.config(bg="white", fg="black", highlightbackground="gray")
    boton_six.config(bg="white", fg="black", highlightbackground="gray")
    boton_seven.config(bg="white", fg="black", highlightbackground="gray")
    boton_eight.config(bg="white", fg="black", highlightbackground="gray")
    boton_nine.config(bg="white", fg="black", highlightbackground="gray")
    boton_clean.config(bg="white", fg="black", highlightbackground="gray")

def dark_mode():
    '''Sets the UI's components to darker colors'''
    result_frame.config(bg="black", highlightbackground="white",highlightthickness=1)    
    operations_frame.config(bg="black", highlightbackground="white",highlightthickness=1)
    numbers_frame.config(bg="black", highlightbackground="white",highlightthickness=1)

    operations_label.config(bg="black", fg="white", highlightbackground="white")
    operations_history_label.config(bg="black", fg="white", highlightbackground="white")

    sqrt_button.config(bg="gray", fg="white", highlightbackground="white")   
    porcentage_button.config(bg="gray", fg="white", highlightbackground="white")   
    power_button.config(bg="gray", fg="white", highlightbackground="white")   
    division_button.config(bg="gray", fg="white", highlightbackground="white")
    multiplication_button.config(bg="gray", fg="white", highlightbackground="white")
    substraction_button.config(bg="gray", fg="white", highlightbackground="white")
    sum_button.config(bg="gray", fg="white", highlightbackground="white")
    result_button.config(bg="gray", fg="white", highlightbackground="white")

    boton_zero.config(bg="black", fg="white", highlightbackground="white")
    boton_double_zero.config(bg="black", fg="white", highlightbackground="white")
    boton_one.config(bg="black", fg="white", highlightbackground="white")
    boton_two.config(bg="black", fg="white", highlightbackground="white")
    boton_three.config(bg="black", fg="white", highlightbackground="white")
    boton_four.config(bg="black", fg="white", highlightbackground="white")
    boton_five.config(bg="black", fg="white", highlightbackground="white")
    boton_six.config(bg="black", fg="white", highlightbackground="white")
    boton_seven.config(bg="black", fg="white", highlightbackground="white")
    boton_eight.config(bg="black", fg="white", highlightbackground="white")
    boton_nine.config(bg="black", fg="white", highlightbackground="white")
    boton_clean.config(bg="black", fg="white", highlightbackground="white")

def blue_amoled_mode():
    '''Sets the UI's components to blue amoled based colors'''
    result_frame.config(bg="#252440", highlightbackground="white", highlightthickness=1)    
    operations_frame.config(bg="#252440", highlightbackground="white", highlightthickness=1)
    numbers_frame.config(bg="#252440", highlightbackground="white", highlightthickness=1)

    operations_label.config(bg="#252440", fg="white", highlightbackground="white")
    operations_history_label.config(bg="#252440", fg="white", highlightbackground="white")

    sqrt_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    porcentage_button.config(bg="#3CB371", fg="white", highlightbackground="white")   
    power_button.config(bg="#3CB371", fg="white", highlightbackground="white")   
    division_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    multiplication_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    substraction_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    sum_button.config(bg="#3CB371", fg="white", highlightbackground="white")
    result_button.config(bg="#3CB371", fg="white", highlightbackground="white")

    boton_zero.config(bg="#252440", fg="white", highlightbackground="white")
    boton_double_zero.config(bg="#252440", fg="white", highlightbackground="white")
    boton_one.config(bg="#252440", fg="white", highlightbackground="white")
    boton_two.config(bg="#252440", fg="white", highlightbackground="white")
    boton_three.config(bg="#252440", fg="white", highlightbackground="white")
    boton_four.config(bg="#252440", fg="white", highlightbackground="white")
    boton_five.config(bg="#252440", fg="white", highlightbackground="white")
    boton_six.config(bg="#252440", fg="white", highlightbackground="white")
    boton_seven.config(bg="#252440", fg="white", highlightbackground="white")
    boton_eight.config(bg="#252440", fg="white", highlightbackground="white")
    boton_nine.config(bg="#252440", fg="white", highlightbackground="white")
    boton_clean.config(bg="#252440", fg="white", highlightbackground="white")
    

#Global variables
main_operator = "0"
secondary_operator = ""
operations = ""
history = ""
pressed_result = 0

#Functions for updating the main_operator according to the button that is pressed
def one():
    global main_operator
    if(main_operator == "0"):
        main_operator = "1"
    elif(len(main_operator) < 17):
        main_operator += "1"
    update_main_operator()
def two():
    global main_operator
    if(main_operator == "0"):
        main_operator = "2"
    elif(len(main_operator) < 17):
        main_operator += "2"
    update_main_operator()
def three():
    global main_operator
    if(main_operator == "0"):
        main_operator = "3"
    elif(len(main_operator) < 17):
        main_operator += "3"
    update_main_operator()
def four():
    global main_operator
    if(main_operator == "0"):
        main_operator = "4"
    elif(len(main_operator) < 17):
        main_operator += "4"
    update_main_operator()
def five():
    global main_operator
    if(main_operator == "0"):
        main_operator = "5"
    elif(len(main_operator) < 17):
        main_operator += "5"
    update_main_operator()
def six():
    global main_operator
    if(main_operator == "0"):
        main_operator = "6"
    elif(len(main_operator) < 17):
        main_operator += "6"
    update_main_operator()
def seven():
    global main_operator
    if(main_operator == "0"):
        main_operator = "7"
    elif(len(main_operator) < 17):
        main_operator += "7"
    update_main_operator()
def eight():
    global main_operator
    if(main_operator == "0"):
        main_operator = "8"
    elif(len(main_operator) < 17):
        main_operator += "8"
    update_main_operator()
def nine():
    global main_operator
    if(main_operator == "0"):
        main_operator = "9"
    elif(len(main_operator) < 17):
        main_operator += "9"
    update_main_operator()
def zero():
    global main_operator
    if(main_operator != "0" and len(main_operator) < 17):
        main_operator += "0"        
    update_main_operator()
def double_zero():
    global main_operator
    if(main_operator != "0" and len(main_operator) < 17):
        main_operator += "00"
    update_main_operator()

def update_main_operator():
    '''Updates the operations_label's text with the current value of the main_operator'''
    operations_label.config(text=main_operator)

def update_history():
    '''Updates the operations_history_label with the current value of the history variable.
    If the result_button has been pressed, it means the pressed_result value will be greater than 0, 
    and if that is the case the history will be set to the last number that was pressed after the result given'''
    global history, pressed_result  
    if pressed_result > 0:
        history = history[pressed_result::]
        pressed_result = 0
    operations_history_label.config(text=history)

def clean():
    '''Cleans all the operations and history that has been proccessed until the momment by the user'''
    global main_operator, history, operations, secondary_operator
    main_operator = "0"
    history = ""
    operations = secondary_operator = ""    
    update_main_operator()
    update_history()

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
        if operations[i] not in "+-xr/^%" and operations[i] in "1234567890." or (i == 0 and operations[i] == "-"):
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

#Declarations of the frames to be used to set the respective components
result_frame = Frame(root,relief="solid",borderwidth=2,bg="#252440", highlightbackground="white", highlightthickness=1)
result_frame.pack(side=TOP, expand=True, fill=BOTH)

operations_frame = Frame(root,relief="solid",highlightthickness=1)
operations_frame.pack(side=RIGHT,expand=True, fill=BOTH)
operations_frame.grid_rowconfigure(0, weight=1)
operations_frame.grid_columnconfigure(0, weight=1)

operations_frame_advnc = Frame(root,relief="solid",highlightthickness=1)
operations_frame_advnc.pack(side=LEFT,expand=True, fill=BOTH)
operations_frame_advnc.grid_rowconfigure(0, weight=1)
operations_frame_advnc.grid_columnconfigure(0, weight=1)

numbers_frame = Frame(root,relief="solid",bg="#252440", highlightbackground="white", highlightthickness=1)
numbers_frame.pack(side=BOTTOM,expand=True,fill=BOTH)
numbers_frame.grid_rowconfigure(0, weight=1)
numbers_frame.grid_columnconfigure(0, weight=1)

#Labels in which the operations and their history will be represented
operations_history_label = Label(result_frame, font=("Curier 10",25),bg="#252440", fg="white", highlightbackground="white")
operations_history_label.pack(anchor="e")

operations_label = Label(result_frame, text=main_operator,font=("Curier 10",30),height=2,bg="#252440", fg="white", highlightbackground="white")
operations_label.pack(anchor="e")

#Buttons for basic arithmetical operations
division_button = Button(operations_frame,text="/", font=("Curier 10", 15),height=0,width=8,command=divide,bg="#3CB371", fg="white", highlightbackground="white")
division_button.pack(anchor="e")

multiplication_button = Button(operations_frame,text="x", font=("Curier 10", 15),height=0,width=8,command=multiply,bg="#3CB371", fg="white", highlightbackground="white")
multiplication_button.pack(anchor="e")

substraction_button = Button(operations_frame,text="-", font=("Curier 10", 15),height=0,width=8,command=substract,bg="#3CB371", fg="white", highlightbackground="white")
substraction_button.pack(anchor="e")

sum_button = Button(operations_frame,text="+", font=("Curier 10", 15),height=3,width=8,command=sum,bg="#3CB371", fg="white", highlightbackground="white")
sum_button.pack(anchor="e")

result_button = Button(operations_frame,text="=", font=("Curier 10",15),height=2,width=8, command=lambda:result(True),bg="#3CB371", fg="white", highlightbackground="white")
result_button.pack(anchor="e")

porcentage_button = Button(operations_frame_advnc, text="%", font=("Curier 10", 15),height=2,width=8,command=porcentage,bg="#3CB371", fg="white", highlightbackground="white")
porcentage_button.pack(anchor="w")

power_button = Button(operations_frame_advnc,text="x^n", font=("Curier 10", 15),height=0,width=8,command=power,bg="#3CB371", fg="white", highlightbackground="white")
power_button.pack(anchor="w")

sqrt_button = Button(operations_frame_advnc, text="Sqrt", font=("Curier 10", 15),height=2,width=8,command=squared_root,bg="#3CB371", fg="white", highlightbackground="white")
sqrt_button.pack(anchor="w")

#Number buttons
boton_zero = Button(numbers_frame, text="0", font=("Curier 10", 15),height=2,width=8,command=zero,bg="#252440", fg="white", highlightbackground="white")
boton_zero.grid(row=4, column=0, sticky='nsew')

boton_double_zero = Button(numbers_frame, text="00", font=("Curier 10", 15),height=2,width=8,command=double_zero, bg="#252440", fg="white", highlightbackground="white")
boton_double_zero.grid(row=4, column=1, sticky='nsew')

boton_one = Button(numbers_frame, text="1", font=("Curier 10", 15),height=2,width=8,command=one,bg="#252440", fg="white", highlightbackground="white")
boton_one.grid(row=3, column=0, sticky='nsew')

boton_two = Button(numbers_frame, text="2", font=("Curier 10", 15),height=2,width=8,command=two,bg="#252440", fg="white", highlightbackground="white")
boton_two.grid(row=3, column=1, sticky='nsew')

boton_three = Button(numbers_frame, text="3", font=("Curier 10", 15),height=2,width=8,command=three,bg="#252440", fg="white", highlightbackground="white")
boton_three.grid(row=3, column=2, sticky='nsew')

boton_four = Button(numbers_frame, text="4", font=("Curier 10", 15),height=2,width=8,command=four,bg="#252440", fg="white", highlightbackground="white")
boton_four.grid(row=2, column=0, sticky='nsew')

boton_five = Button(numbers_frame, text="5", font=("Curier 10", 15),height=2,width=8,command=five,bg="#252440", fg="white", highlightbackground="white")
boton_five.grid(row=2, column=1, sticky='nsew')

boton_six = Button(numbers_frame, text="6", font=("Curier 10", 15),height=2,width=8,command=six,bg="#252440", fg="white", highlightbackground="white")
boton_six.grid(row=2, column=2, sticky='nsew')

boton_seven = Button(numbers_frame, text="7", font=("Curier 10", 15),height=2,width=8,command=seven,bg="#252440", fg="white", highlightbackground="white")
boton_seven.grid(row=1, column=0, sticky='nsew')

boton_eight = Button(numbers_frame, text="8", font=("Curier 10", 15),height=2,width=8,command=eight,bg="#252440", fg="white", highlightbackground="white")
boton_eight.grid(row=1, column=1, sticky='nsew')

boton_nine = Button(numbers_frame, text="9", font=("Curier 10", 15),height=2,width=8,command=nine,bg="#252440", fg="white", highlightbackground="white")
boton_nine.grid(row=1, column=2, sticky='nsew')

#boton c/ce (clear)
boton_clean = Button(numbers_frame, text="C", font=("Curier 10", 15),height=2,width=8,command=clean,bg="#252440", fg="white", highlightbackground="white")
boton_clean.grid(row=4,column=2, sticky='nsew')