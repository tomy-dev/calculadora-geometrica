# Rombo

def calculo():
    d = input("Ingrese d: ")
    D = input("Ingrese D: ")
    altura = input("Ingrese la altura: ")
    
    d = float(d)
    D = float(D)
    altura = float(altura)

    perimetro : float = 4 * altura
    area : float = (d * D) / 2
    
    perimetro = str(perimetro)
    area = str(area)
    
    print("Perimetro: " + perimetro)
    print("Area: " + area)

calculo()