import calculadora_indices as calc

def calculo_calorias_adelgazar():
    print("En esta función se va calcular el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar. \n")
    peso = float(input("Ingrese el peso de la persona (en kilogramos):"))
    altura = float(input("Ingrese la altura de la persona (en centímtros):"))
    edad = int(input("Ingrese la edad de la persona (en años):"))
    valor_genero = int(input("Ingrese el valor (5) en caso de ser hombre y (-161) en caso de ser mujer:"))
    c = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(c)

calculo_calorias_adelgazar()

##########################################################################################################################
