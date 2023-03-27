import calculadora_indices as calc

def calculo_porcentaje_grasa():
    print("En esta función se va calcular el porcentaje de grasa de una persona. \n")
    peso = float(input("Ingrese el peso de la persona (en kilogramos):"))
    altura = float(input("Ingrese la altura de la persona (en metros):"))
    edad = int(input("Ingrese la edad de la persona (en años):"))
    valor_genero = float(input("Ingrese el valor (10.8) en caso de hombre y (0) en caso de ser mujer:"))
    GC = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print("El porcentaje de grasa que tiene el cuerpo de la persona es:",round(GC, 2), "%")

calculo_porcentaje_grasa()

##########################################################################################################################