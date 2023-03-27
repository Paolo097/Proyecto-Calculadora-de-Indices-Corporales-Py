import calculadora_indices as calc

def calculo_calorias_reposo():
    print("En esta función se va calcular la cantidad de calorías que una persona quema estando en reposo (esto es, su tasa metabólica basal). \n")
    peso = float(input("Ingrese el peso de la persona (en kilogramos):"))
    altura = float(input("Ingrese la altura de la persona (en centímetros):"))
    edad = int(input("Ingrese la edad de la persona (en años):"))
    valor_genero = int(input(
        "Ingrese el valor (5) en caso de ser hombre y (-161) en caso de ser mujer:"))
    TMB = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("La cantidad de calorias que la persona quema en reposo es:", TMB, "cal")

calculo_calorias_reposo()

##########################################################################################################################