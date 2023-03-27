import calculadora_indices as calc

def calculo_calorias_en_actividad():
    print("En esta función se va calcular la cantidad de calorías que una persona quema al realizar algún tipo de actividad física. \n")
    peso = float(input("Ingrese el peso de la persona (en kilogramos):"))
    altura = float(input("Ingrese la altura de la persona (en centímetros):"))
    edad = int(input("Ingrese la edad de la persona (en años):"))
    valor_genero = (float(input("Ingrese el valor (5) en caso de ser hombre y (-161) en caso de ser mujer:")))
    valor_actividad = (float(input("Ingrese el valor de actividad fisica semanal:\n"
                                   "1.2: -> Poco o Ningún ejercicio.\n"
                                   "1.375: -> Ejercicio Lígero (1 a 3 días a la semana).\n"
                                   "1.55: -> Ejercicio Moderado (3 a 5 días de la semana).\n"
                                   "1.725: -> Deportista (6-7 días a la semana).\n"
                                   "1.9: -> Atleta (entrenamientos mañana y tarde):")))
    TMB = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print("La cantidad de calorías que una persona quema, al realizar algún tipo de actividad física semanalmente es:", round(TMB, 2), "cal")

calculo_calorias_en_actividad()

##########################################################################################################################