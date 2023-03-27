import calculadora_indices as calc

def calculo_imc():
    print("En esta función se va calcular el índice de masa corporal de una persona. \n")
    peso = float(input("Ingrese el peso de la persona (en kilogramos):"))
    altura = float(input("Ingrese la altura de la persona (en metros):"))
    IMC = calc.calcular_IMC(peso, altura)
    print("El índice de masa corporal de la persona es:",round(IMC,2),"\n")

#########################################################################################

def calculo_porcentaje_grasa():
    print("En esta función se va calcular el porcentaje de grasa de una persona. \n")
    peso = float(input("Ingrese el peso de la persona (en kilogramos):"))
    altura = float(input("Ingrese la altura de la persona (en metros):"))
    edad = int(input("Ingrese la edad de la persona (en años):"))
    valor_genero = float(input("Ingrese el valor (10.8) en caso de hombre y (0) en caso de ser mujer:"))
    GC = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print("El porcentaje de grasa que tiene el cuerpo de la persona es:",round(GC,2),"% \n")

########################################################################################

def calculo_calorias_reposo():
    print("En esta función se va calcular la cantidad de calorías que una persona quema estando en reposo (esto es, su tasa metabólica basal). \n")
    peso = float(input("Ingrese el peso de la persona (en kilogramos):"))
    altura = float(input("Ingrese la altura de la persona (en centímetros):"))
    edad = int(input("Ingrese la edad de la persona (en años):"))
    valor_genero = int(input("Ingrese el valor (5) en caso de ser hombre y (-161) en caso de ser mujer:"))
    TMB = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    print("La cantidad de calorias que la persona quema en reposo es:",TMB,"cal \n")

########################################################################################

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
    print("La cantidad de calorías que una persona quema, al realizar algún tipo de actividad física semanalmente es:",round(TMB,2),"cal \n")

########################################################################################

def calculo_calorias_adelgazar():
    print("En esta función se va calcular el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar. \n")
    peso = float(input("Ingrese el peso de la persona (en kilogramos):"))
    altura = float(input("Ingrese la altura de la persona (en centímtros):"))
    edad = int(input("Ingrese la edad de la persona (en años):"))
    valor_genero = int(input("Ingrese el valor (5) en caso de ser hombre y (-161) en caso de ser mujer:"))
    c = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(c)
    
########################################################################################

def mostrar_menu():
    print("Bienvenidos a la Calculadora de Indices Corporales!!!")
    print("Seleccione una opción:")
    print("1. Calculadora de Masa Corporal.")
    print("2. Calculadora de Porcentaje de Grasa en Cuerpo.")
    print("3. Calculadora de Quemar Calorias en Reposo.")
    print("4. Calculadora de Quemar Calorias en Actividad.")
    print("5. Calculadora de Quemar Calorias para Adelgazar. ")
    print("6. Salir.")
    opcion = input("Opción seleccionada:")
    return opcion

########################################################################################

def iniciar_aplicacion():
    continuar = True
    while continuar:
        opcion = mostrar_menu()
        if opcion == "1":
            calculo_imc()
        elif opcion == "2":
            calculo_porcentaje_grasa()
        elif opcion == "3":
            calculo_calorias_reposo()
        elif opcion == "4":
            calculo_calorias_en_actividad()
        elif opcion == "5":
            calculo_calorias_adelgazar()
        elif opcion == "6":
            continuar = False
        else:
            print("La opción seleccionada no es válida.")

iniciar_aplicacion()
