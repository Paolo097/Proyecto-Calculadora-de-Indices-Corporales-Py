#Se crea la funcion para obtener el indice de masa corporal y se pasan los parametros peso y altura
def calcular_IMC (peso, altura):
    #Se realiza la ecuacion de peso en kg y el cuadrado de la altura en metros de la persona y se guarda en la variable IMC
    IMC = peso / (altura**2)
    return IMC

##########################################################################################################################

#Se crea la funcion para obtener el porcentaje de grasa corporal de la persona, se pasan los parametros peso, altura, edad, valor genero
def calcular_porcentaje_grasa (peso, altura, edad, valor_genero):
    #Se calcula a partir del IMC, la edad y el genero de la persona y se guarda en la variable GC(grasa corporal)
    GC = 1.2 * (peso / (altura**2)) + 0.23 * edad - 5.4 - valor_genero
    return GC

##########################################################################################################################

#Se crea la funcion para obtener las calorias en reposo de la persona, se pasan los parametros peso, altura, edad, valor genero
def calcular_calorias_en_reposo (peso, altura, edad, valor_genero):
    #Se calcula a traves de la siguiente formula y se guarda en la variable TMB(tasa metabólica basal)
    TMB = (10*peso) + (6.25*altura) - (5*edad) + valor_genero
    return TMB

##########################################################################################################################

#Se crea la funcion para obtener la calorias que una persona quema en actividad, se pasan los parametros peso, altura, edad, valor genero, valor actividad
def calcular_calorias_en_actividad (peso, altura, edad, valor_genero, valor_actividad):
    #Se calcula a traves de la siguiente formula y se guarda en la variable TMB(tasa metabolica basal)
    TMB = ((10*peso) + (6.25*altura) - (5*edad) + valor_genero) * valor_actividad
    return TMB
  
  ##########################################################################################################################
 
#Se crea la funcion para obtener el consumo de calorias recomendado para adelgazar, se pasan los parametros peso, altura, edad, valor genero
def consumo_calorias_recomendado_para_adelgazar (peso, altura, edad, valor_genero):
    #Se calcula a traves de la siguiente formula
    a = round((((10*peso) + (6.25*altura) - (5*edad)) * 0.8),2)
    b = round((((10*peso) + (6.25*altura) - (5*edad)) * 0.85),2)
    c = f"Para adelgazar es recomendado que consumas entre: {a} y {b} calorías al día \n"
    return c
    