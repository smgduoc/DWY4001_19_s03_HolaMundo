#!/usr/bin/python3

from Persona import Persona

# ahora el "main" , que está fuera de la clase
perrin = Persona("Juan Eduardo", "1237745-3")
perrin.imprimir()

#en python los atributos son publicos
#y se pueden modificcar directamnte

perrin.rut= "1237745-3"
perrin.imprimir()

#crear una persona leyendo desde la consola
nombre = input("Ingresar nombre: ")
rut = input("Ingresar RUT: ")
personaIngresada = Persona(nombre, rut)
personaIngresada.imprimir()