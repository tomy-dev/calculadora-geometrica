# Rectángulo

def calculo():
    base = input("Ingrese el tamaño de la base en cm: ")
    lado = input("Ingrese el tamaño de un lado: ")
    
    base = float(base)
    lado = float(lado)

    perimetro : float = 2 * (base + lado)
    area : float = base * lado
    
    perimetro = str(perimetro)
    area = str(area)
    
    print("Perimetro: " + perimetro)
    print("Area: " + area)