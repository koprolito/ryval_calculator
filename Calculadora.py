from Vista import *
from Operacion import *
import ctypes

# Obtener la configuración del tema del sistema
SPI_GETTHEMEACTIVE = 0x200A
theme_active = ctypes.c_bool()
ctypes.windll.user32.SystemParametersInfoW(SPI_GETTHEMEACTIVE, 0, ctypes.byref(theme_active), 0)

#Aplicar el tema correspondiente
#Nota: aunque el del sistema sea claro, el fondo de la calculadora siempre será oscuro por defecto. Se debe corregir
if theme_active.value:
    dark_mode()
else:
    light_mode()

root.config(menu=menuBar)
root.update()
root.geometry(root.geometry())
root.mainloop()