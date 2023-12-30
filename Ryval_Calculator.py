from View import *
from Operation import *
import ctypes

#Get the configuration of the OS
SPI_GETTHEMEACTIVE = 0x200A
theme_active = ctypes.c_bool()
ctypes.windll.user32.SystemParametersInfoW(SPI_GETTHEMEACTIVE, 0, ctypes.byref(theme_active), 0)

#Apply the correspondant mode
#Note: it still does not detect the exact configuration of the OS. It always
#sets dark mode by default
if theme_active.value:
    dark_mode()
else:
    light_mode()

root.config(menu=menu_bar)
root.update()
root.geometry(root.geometry())
root.mainloop()