#!/usr/bin/env python3
#---------------------------------------------
from gui import gui
from src import signal


signal.system_clear()
signal.system_information("Controlium")
signal.manage_args()
#-------------

gui.program()

#-------------
print("-----------------------")
print("Program \033[1;34mexit\033[0m")
