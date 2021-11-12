# Paralelogramo

def calculo():
    base = input("Ingrese el tamaño de la base en cm: ")
    lado = input("Ingrese el tamaño de un lado: ")
    altura = input("Ingrese la altura: ")
    
    base = float(base)
    lado = float(lado)
    altura = float(altura)

    perimetro : float = 2 * (base + lado)
    area : float = base * altura
    
    perimetro = str(perimetro)
    area = str(area)
    
    print("Perimetro: " + perimetro)
    print("Area: " + area)