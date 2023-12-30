from tkinter import *
from tkinter import messagebox
from Operacion import *

#declaracion de la raiz de la ventana
root = Tk()
root.iconbitmap("icono_calculadora.ico")
root.title("Calculadora")
root.resizable(0,0)

#Crear una barra menú
menuBar = Menu(root)

#Crear un menú de edición del aspecto de la calculadora
edit_view = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="View",menu=edit_view)

# Crear un submenú para los temas
theme_menu = Menu(edit_view, tearoff=0)

# Agregar opciones de temas al submenú
theme_menu.add_command(label="Light mode", command=lambda:light_mode())
theme_menu.add_command(label="Dark mode", command=lambda:dark_mode())
theme_menu.add_command(label="Blue AMOLED mode", command=lambda:blue_amoled_mode())

# Agregar el submenú al menú de edición
edit_view.add_cascade(label="Themes", menu=theme_menu)

#Funciones para cambiar el tema de la calculadora
def light_mode():

    marco_resultado.config(bg="white", highlightbackground="black",highlightthickness=1)    
    marco_operaciones.config(bg="white", highlightbackground="black",highlightthickness=1)
    marco_numeros.config(bg="white", highlightbackground="black",highlightthickness=1)

    linea_de_operaciones.config(bg="white", fg="black", highlightbackground="gray")
    historial_de_operaciones.config(bg="white", fg="black", highlightbackground="gray")

    boton_porcentaje.config(bg="black", fg="white", highlightbackground="gray")
    boton_raiz_cuadrada.config(bg="black", fg="white", highlightbackground="gray")   
    boton_potencia.config(bg="black", fg="white", highlightbackground="gray")   
    boton_division.config(bg="black", fg="white", highlightbackground="gray")
    boton_multiplicacion.config(bg="black", fg="white", highlightbackground="gray")
    boton_resta.config(bg="black", fg="white", highlightbackground="gray")
    boton_suma.config(bg="black", fg="white", highlightbackground="gray")
    boton_resultado.config(bg="black", fg="white", highlightbackground="gray")

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
    marco_resultado.config(bg="black", highlightbackground="white",highlightthickness=1)    
    marco_operaciones.config(bg="black", highlightbackground="white",highlightthickness=1)
    marco_numeros.config(bg="black", highlightbackground="white",highlightthickness=1)

    linea_de_operaciones.config(bg="black", fg="white", highlightbackground="white")
    historial_de_operaciones.config(bg="black", fg="white", highlightbackground="white")

    boton_raiz_cuadrada.config(bg="gray", fg="white", highlightbackground="white")   
    boton_porcentaje.config(bg="gray", fg="white", highlightbackground="white")   
    boton_potencia.config(bg="gray", fg="white", highlightbackground="white")   
    boton_division.config(bg="gray", fg="white", highlightbackground="white")
    boton_multiplicacion.config(bg="gray", fg="white", highlightbackground="white")
    boton_resta.config(bg="gray", fg="white", highlightbackground="white")
    boton_suma.config(bg="gray", fg="white", highlightbackground="white")
    boton_resultado.config(bg="gray", fg="white", highlightbackground="white")

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
    marco_resultado.config(bg="#252440", highlightbackground="white", highlightthickness=1)    
    marco_operaciones.config(bg="#252440", highlightbackground="white", highlightthickness=1)
    marco_numeros.config(bg="#252440", highlightbackground="white", highlightthickness=1)

    linea_de_operaciones.config(bg="#252440", fg="white", highlightbackground="white")
    historial_de_operaciones.config(bg="#252440", fg="white", highlightbackground="white")

    boton_raiz_cuadrada.config(bg="#3CB371", fg="white", highlightbackground="white")
    boton_porcentaje.config(bg="#3CB371", fg="white", highlightbackground="white")   
    boton_potencia.config(bg="#3CB371", fg="white", highlightbackground="white")   
    boton_division.config(bg="#3CB371", fg="white", highlightbackground="white")
    boton_multiplicacion.config(bg="#3CB371", fg="white", highlightbackground="white")
    boton_resta.config(bg="#3CB371", fg="white", highlightbackground="white")
    boton_suma.config(bg="#3CB371", fg="white", highlightbackground="white")
    boton_resultado.config(bg="#3CB371", fg="white", highlightbackground="white")

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
    

#Variables globales
operando = "0"
n1 = ""
operaciones = ""
historial = ""
resultado_presionado = 0

#actualizaciones del operando según el boton al que se le haga click
def one():
    global operando
    if(operando == "0"):
        operando = "1"
    elif(len(operando) < 17):
        operando += "1"
    actualizar_operando()
def two():
    global operando
    if(operando == "0"):
        operando = "2"
    elif(len(operando) < 17):
        operando += "2"
    actualizar_operando()
def three():
    global operando
    if(operando == "0"):
        operando = "3"
    elif(len(operando) < 17):
        operando += "3"
    actualizar_operando()
def four():
    global operando
    if(operando == "0"):
        operando = "4"
    elif(len(operando) < 17):
        operando += "4"
    actualizar_operando()
def five():
    global operando
    if(operando == "0"):
        operando = "5"
    elif(len(operando) < 17):
        operando += "5"
    actualizar_operando()
def six():
    global operando
    if(operando == "0"):
        operando = "6"
    elif(len(operando) < 17):
        operando += "6"
    actualizar_operando()
def seven():
    global operando
    if(operando == "0"):
        operando = "7"
    elif(len(operando) < 17):
        operando += "7"
    actualizar_operando()
def eight():
    global operando
    if(operando == "0"):
        operando = "8"
    elif(len(operando) < 17):
        operando += "8"
    actualizar_operando()
def nine():
    global operando
    if(operando == "0"):
        operando = "9"
    elif(len(operando) < 17):
        operando += "9"
    actualizar_operando()
def zero():
    global operando
    if(operando != "0" and len(operando) < 17):
        operando += "0"        
    actualizar_operando()
def double_zero():
    global operando
    if(operando != "0" and len(operando) < 17):
        operando += "00"
    actualizar_operando()

def actualizar_operando():
    linea_de_operaciones.config(text=operando)

def actualizar_historial():
    global historial, resultado_presionado  
    if resultado_presionado > 0:
        historial = historial[resultado_presionado::]
        resultado_presionado = 0
    historial_de_operaciones.config(text=historial)

def clean():
    global operando
    global operaciones
    global n1
    operando = "0"
    operaciones = n1 = ""
    actualizar_operando()

def validar_indeterminacion():
    global operaciones
    global operando
    if(operando == "0"):
        mb = messagebox.showinfo("Error","No se puede dividir entre zero")
        clean()
        return True
    else:
        return False
    
def is_int(num):
    for i in range(num.find(".")+1, len(num)):
            if num[i] != "0":
                return False
    return True

def resultado(update):
    cad_num = ""
    res = ""
    sqrt = False
    global operaciones,operando, n1, historial, resultado_presionado
    
    for i in range(len(operaciones)):
        if operaciones[i] not in "+-xr/^%" and operaciones[i] in "1234567890." or (i == 0 and operaciones[i] == "-"):
            cad_num += operaciones[i]
        elif operaciones[i:len(operaciones)] == "sqrt":
            sqrt = True
            break
        else:
            break

    if sqrt == True:
        res = str(Operacion.raiz_cuadrada(float(cad_num)).real)

    if '%' in operaciones:
        porcentage = str(Operacion.porcentaje(float(cad_num),float(operando)))
        if '+' in operaciones:
            res = str(Operacion.sumar(float(cad_num),float(porcentage)))
        elif '-' in operaciones:
            res = str(Operacion.restar(float(cad_num),float(porcentage)))
        elif 'x' in operaciones:
            res = porcentage
        elif '/' in operaciones:
            if(validar_indeterminacion() == False):
                res = str(Operacion.dividir(float(cad_num),float(operando)/100))
            else:
                return ""
        elif '^' in operaciones:
            res = str(Operacion.potencia(float(cad_num),float(porcentage)))
    else:
        if '+' in operaciones:
            res = str(Operacion.sumar(float(cad_num),float(operando)))
        elif '-' in operaciones:
            res = str(Operacion.restar(float(cad_num),float(operando)))
        elif 'x' in operaciones:
            res = str(Operacion.multiplicar(float(cad_num),float(operando)))
        elif '/' in operaciones:
            if(validar_indeterminacion() == False):
                res = str(Operacion.dividir(float(cad_num),float(operando)))
            else:
                return ""
        elif '^' in operaciones:
            res = str(Operacion.potencia(float(cad_num),float(operando)))
        elif sqrt == False:
            res = cad_num
        
    if update == True:
        historial += operando
        if(is_int(res) == False):
            operando = res
        else:
            operando = res[:res.find(".")]
        actualizar_historial()
        resultado_presionado += len(historial)
        actualizar_operando()

        n1 = operaciones = ""   
    return res

def sumar():
    global n1, operando, operaciones, historial
    historial += operando+"+"

    if(n1 == ""):
        n1 = operando
        operaciones += n1+"+"
    elif(n1 != "" and operando != ""): 
        n1 = resultado(False)
        operaciones = n1+"+" 
    operando = "0"
    actualizar_historial()
    actualizar_operando()

def restar():
    global n1, operando, operaciones, historial
    historial += operando+"-"

    if(n1 == ""):
        n1 = operando
        operaciones += n1+"-"
    elif(n1 != "" and operando != ""): 
        n1 = resultado(False)
        operaciones = n1+"-" 
    operando = "0"
    actualizar_historial()
    actualizar_operando()

def multiplicar():
    global n1, operando, operaciones, historial
    historial += operando+"x"

    if(n1 == ""):
        n1 = operando
        operaciones += n1+"x"
    elif(n1 != "" and operando != ""): 
        n1 = resultado(False)
        operaciones = n1+"x" 
    operando = "0"
    actualizar_historial()
    actualizar_operando()

def dividir():
    global n1, operando, operaciones, historial
    historial += operando+"/"

    if(n1 == ""):
        n1 = operando
        operaciones += n1+"/"
        operando = "0"
    elif(n1 != "" and operando != ""):
        n1 = resultado(False) 
        operaciones = n1+"/" 
    operando = "0"
    actualizar_historial()
    actualizar_operando()

def potencia():
    global n1, operando, operaciones, historial
    historial += operando+"^"

    if(n1 == ""):
        n1 = operando
        operaciones += n1+"^"
        operando = "0"
    elif(n1 != "" and operando != ""):
        operaciones += "^" 
        n1 = resultado(False)
        operaciones = n1
    operando = "0"  
    actualizar_historial()      
    actualizar_operando()

def porcentaje():
    global n1, operando, operaciones, historial
    historial += operando+"%"

    if(n1 == ""):
        n1 = operando
        operaciones += n1+"%"
        operando = "0"
    elif(n1 != "" and operando != ""):
        operaciones += "%" 
        n1 = resultado(False)
        operaciones = n1
    operando = "0"
    actualizar_historial()
    actualizar_operando()

def raiz_cuadrada():
    global n1, operando, operaciones, historial
    historial += f"sqrt({operando})"

    if(n1 == ""):
        n1 = operando
        operaciones += n1+"sqrt"
        operando = "0"
    elif(n1 != "" and operando != ""):
        operaciones += "sqrt" 
        n1 = resultado(False)
        operaciones = n1
    operando = "0" 
    actualizar_historial()
    actualizar_operando()

#declaracion de frames para colocar los botones y los labels
marco_resultado = Frame(root,relief="solid",borderwidth=2,bg="#252440", highlightbackground="white", highlightthickness=1)
marco_resultado.pack(side=TOP, expand=True, fill=BOTH)

marco_operaciones = Frame(root,relief="solid",highlightthickness=1)
marco_operaciones.pack(side=RIGHT,expand=True, fill=BOTH)
marco_operaciones.grid_rowconfigure(0, weight=1)
marco_operaciones.grid_columnconfigure(0, weight=1)

marco_operaciones_advnc = Frame(root,relief="solid",highlightthickness=1)
marco_operaciones_advnc.pack(side=LEFT,expand=True, fill=BOTH)
marco_operaciones_advnc.grid_rowconfigure(0, weight=1)
marco_operaciones_advnc.grid_columnconfigure(0, weight=1)

marco_numeros = Frame(root,relief="solid",bg="#252440", highlightbackground="white", highlightthickness=1)
marco_numeros.pack(side=BOTTOM,expand=True,fill=BOTH)
marco_numeros.grid_rowconfigure(0, weight=1)
marco_numeros.grid_columnconfigure(0, weight=1)

#Label de linea_de_operaciones, donde se colocaran totwo los botones de operaciones aritméticas básicas
historial_de_operaciones = Label(marco_resultado, font=("Curier 10",25),bg="#252440", fg="white", highlightbackground="white")
historial_de_operaciones.pack(anchor="e")

linea_de_operaciones = Label(marco_resultado, text=operando,font=("Curier 10",30),height=2,bg="#252440", fg="white", highlightbackground="white")
linea_de_operaciones.pack(anchor="e")

#botones de operaciones aritméticas básicas

boton_potencia = Button(marco_operaciones,text="^", font=("Curier 10", 15),height=0,width=8,command=potencia,bg="#3CB371", fg="white", highlightbackground="white")
boton_potencia.pack(anchor="e")

boton_division = Button(marco_operaciones,text="/", font=("Curier 10", 15),height=0,width=8,command=dividir,bg="#3CB371", fg="white", highlightbackground="white")
boton_division.pack(anchor="e")

boton_multiplicacion = Button(marco_operaciones,text="x", font=("Curier 10", 15),height=0,width=8,command=multiplicar,bg="#3CB371", fg="white", highlightbackground="white")
boton_multiplicacion.pack(anchor="e")

boton_resta = Button(marco_operaciones,text="-", font=("Curier 10", 15),height=0,width=8,command=restar,bg="#3CB371", fg="white", highlightbackground="white")
boton_resta.pack(anchor="e")

boton_suma = Button(marco_operaciones,text="+", font=("Curier 10", 15),height=3,width=8,command=sumar,bg="#3CB371", fg="white", highlightbackground="white")
boton_suma.pack(anchor="e")

boton_resultado = Button(marco_operaciones,text="=", font=("Curier 10",15),height=2,width=8, command=lambda:resultado(True),bg="#3CB371", fg="white", highlightbackground="white")
boton_resultado.pack(anchor="e")

boton_porcentaje = Button(marco_operaciones_advnc, text="%", font=("Curier 10", 15),height=2,width=8,command=porcentaje,bg="#3CB371", fg="white", highlightbackground="white")
boton_porcentaje.pack(anchor="w")

boton_raiz_cuadrada = Button(marco_operaciones_advnc, text="Sqrt", font=("Curier 10", 15),height=2,width=8,command=raiz_cuadrada,bg="#3CB371", fg="white", highlightbackground="white")
boton_raiz_cuadrada.pack(anchor="w")

#botones de números

boton_zero = Button(marco_numeros, text="0", font=("Curier 10", 15),height=2,width=8,command=zero,bg="#252440", fg="white", highlightbackground="white")
boton_zero.grid(row=4, column=0, sticky='nsew')

boton_double_zero = Button(marco_numeros, text="00", font=("Curier 10", 15),height=2,width=8,command=double_zero, bg="#252440", fg="white", highlightbackground="white")
boton_double_zero.grid(row=4, column=1, sticky='nsew')

boton_one = Button(marco_numeros, text="1", font=("Curier 10", 15),height=2,width=8,command=one,bg="#252440", fg="white", highlightbackground="white")
boton_one.grid(row=3, column=0, sticky='nsew')

boton_two = Button(marco_numeros, text="2", font=("Curier 10", 15),height=2,width=8,command=two,bg="#252440", fg="white", highlightbackground="white")
boton_two.grid(row=3, column=1, sticky='nsew')

boton_three = Button(marco_numeros, text="3", font=("Curier 10", 15),height=2,width=8,command=three,bg="#252440", fg="white", highlightbackground="white")
boton_three.grid(row=3, column=2, sticky='nsew')

boton_four = Button(marco_numeros, text="4", font=("Curier 10", 15),height=2,width=8,command=four,bg="#252440", fg="white", highlightbackground="white")
boton_four.grid(row=2, column=0, sticky='nsew')

boton_five = Button(marco_numeros, text="5", font=("Curier 10", 15),height=2,width=8,command=five,bg="#252440", fg="white", highlightbackground="white")
boton_five.grid(row=2, column=1, sticky='nsew')

boton_six = Button(marco_numeros, text="6", font=("Curier 10", 15),height=2,width=8,command=six,bg="#252440", fg="white", highlightbackground="white")
boton_six.grid(row=2, column=2, sticky='nsew')

boton_seven = Button(marco_numeros, text="7", font=("Curier 10", 15),height=2,width=8,command=seven,bg="#252440", fg="white", highlightbackground="white")
boton_seven.grid(row=1, column=0, sticky='nsew')

boton_eight = Button(marco_numeros, text="8", font=("Curier 10", 15),height=2,width=8,command=eight,bg="#252440", fg="white", highlightbackground="white")
boton_eight.grid(row=1, column=1, sticky='nsew')

boton_nine = Button(marco_numeros, text="9", font=("Curier 10", 15),height=2,width=8,command=nine,bg="#252440", fg="white", highlightbackground="white")
boton_nine.grid(row=1, column=2, sticky='nsew')

#boton c/ce
boton_clean = Button(marco_numeros, text="C", font=("Curier 10", 15),height=2,width=8,command=clean,bg="#252440", fg="white", highlightbackground="white")
boton_clean.grid(row=4,column=2, sticky='nsew')