#creando parametros args

def suma(nombre,*numeros):
    return f"{nombre}, la suma de los valores es: {sum(numeros)}"

resultado = suma("Paisa",9,3,4,5,6,3)
print(resultado)