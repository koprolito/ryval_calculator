from Controller import *
import ctypes
import pygame
from pygame import mixer
    
#Get the configuration of the OS
SPI_GETTHEMEACTIVE = 0x200A
theme_active = ctypes.c_bool()
ctypes.windll.user32.SystemParametersInfoW(SPI_GETTHEMEACTIVE, 0, ctypes.byref(theme_active), 0)

#Apply the correspondant mode
#Note: it still does not detect the exact configuration of the OS. It always
#sets dark mode by default
if theme_active.value:
    ui.change_mode("black","white",1,"black","white", "gray", "white", "black", "white", "white")
else:
    ui.change_mode("white","black",1,"white","black", "black", "white", "white", "black", "gray")

ui.root.config(menu=ui.menu_bar)
ui.root.update()
ui.root.geometry(ui.root.geometry())
ui.root.mainloop()