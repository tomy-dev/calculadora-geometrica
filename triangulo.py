# Triangulo

def calculo():
    base = input("Ingrese el tamaño de la base en cm: ")
    lado_izq = input("Ingrese el tamaño del lado izquierdo: ")
    lado_der = input("Ingrese el tamaño del lado derecho: ")
    altura = input("Ingrese la altura: ")
    
    base = float(base)
    lado_izq = float(lado_izq)
    lado_der = float(lado_der)
    altura = float(altura)
    
    perimetro : float = base + lado_izq + lado_der
    area : float = (base * altura) / 2
    
    perimetro = str(perimetro)
    area = str(area)
    
    print("Perimetro: " + perimetro)
    print("Area: " + area)