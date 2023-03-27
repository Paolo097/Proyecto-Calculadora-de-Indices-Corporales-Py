def perimetro_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return perimetro, area
    

perimetro, area = perimetro_cuadrado(5)

print(f"El Perimetro es: {perimetro} y el Area es: {area}")