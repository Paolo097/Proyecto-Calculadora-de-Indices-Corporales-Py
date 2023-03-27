#funcion para obtener al profesor y asistente segun la edad.
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista de compañeros
    compañeros = []
    
    #se pide con un for info de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #se agrega info a la lista
        compañeros.append(compañero)
        
    #ordena de menor a mayor segun su edad    
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente, profesor = obtener_compañeros(5)

#mostramos el resultado    
print(f"El profesor es: {profesor} y su asistente es: {asistente}")
