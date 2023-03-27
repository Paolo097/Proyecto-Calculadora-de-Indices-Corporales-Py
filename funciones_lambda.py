#creando funcion lambda para multiplicar
multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5))

#creando funcion lambda para numeros pares
numeros = [1,35,3,58,23,34,40,99]
numeros_pares = filter(lambda numero : numero%2 == 0, numeros)

print(list(numeros_pares))