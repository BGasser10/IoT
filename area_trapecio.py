import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

print("Los datos deben estar entre 1 y 20")

x1=float(input("Ingrese la coordenada X (x1) de una de las esquinas superiores:  "))
y1=float(input("Ingrese la coordenada Y (y1) del punto anterior:  "))

x2=float(input("Ingrese la coordenada X (x2) de la otra esquina superior:  "))
y2=float(input("Ingrese la coordenada Y (y2) del punto anterior:  "))

A=((y1+y2)*(x1-x2))/2

plt.plot([x1,x2,x2,x1,x1],[0,0,y2,y1,0])
plt.axis([-1,20,-1,20])

if A < 0:
    A= A*-1

plt.fill_between([x1,x2,x2,x1,x1],[0,0,y2,y1,0])
print("El area es de",A)

plt.show()
