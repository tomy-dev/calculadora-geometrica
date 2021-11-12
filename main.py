# Main / Menu

import continuo
import triangulo
import paralelogramo
import rectangulo
import cuadrado
import rombo

print("Calculadora Geometrica | Menu")

def menu():
    print('''
        Triángulo: 1
        Paralelogramo: 2
        Rectángulo: 3
        Cuadrado: 4
        Rombo: 5
        Romboide: 6
        Trapecio: 7
        Circulo: 8
    ''')

    figura = input("Elije una figura: ")
    figura = int(figura)

    if (figura == 1):
        triangulo.calculo()
        continuo.continuar()
    elif (figura == 2):
        paralelogramo.calculo()
        continuo.continuar()
    elif (figura == 3):
        rectangulo.calculo()
        continuo.continuar()
    elif (figura == 4):
        cuadrado.calculo()
        continuo.continuar()
    elif (figura == 5):
        rombo.calculo()
        continuo.continuar()