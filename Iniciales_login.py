
import time
import os
import sys
import sqlite3
import getpass
 
#declaracion de variables
 
registeredUser = ('utng')
registeredPW = ('mexico')
 
#declaracion de funciones
def login(usuario,passw):
    if usuario in registeredUser:
        if passw in registeredPW:
            return 1
        else:
            print("\n\ Las contraseñas no coinciden \n")
    else:
        return 2
 
 #inicializacion de procesos
usuario=input('Usuario: ')
passw = getpass.getpass('Contraseña: ')
 
if login(usuario,passw)==1:
    print('BIENVENIDO ',usuario)
else:
    print('ERROR! el usuario no esta registrado!.')
