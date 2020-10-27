# Calculamos el area del triangulo dadas su base y su area
def triangleArea(base, height):
    return (base*height)/2

# Que tipo de traingulo segun las dimensiones de sus 3 lados
def triangleType(edge1, edge2, edge3):
    typeOfTriangle = ""
    if edge1 == edge2 and edge2 == edge3:
        typeOfTriangle = "equiltero"
    elif ((edge1 == edge2) or (edge2 == edge3) or (edge1 == edge3)): 
        typeOfTriangle = "isosceles"
    else:
        typeOfTriangle = "escaleno"
    return typeOfTriangle


if __name__ == '__main__':
    # area del triangulo
    base = float(input("Ingresa la base del triagulo: "))
    height = float(input("Ingresa la altura del triangulo: "))
    area = triangleArea(base, height)

    # Tipo de traingulo
    respuesta = input("Quieres saber el tipo de triangulo? [si/no]: ")
    if respuesta == "si":
        edge1 = input("Medida del lado 1: ")
        edge2 = input("Medida del lado 2: ")
        edge3 = input("Medida del lado 3: ")
        tipo = triangleType(edge1, edge2, edge3)
        print(f"El traingulo es del tipo {tipo} y su area es {area} unidades.")
    else:
        print(f"El area del triangulo son {area} unidades.")