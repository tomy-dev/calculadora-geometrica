# Continuar

import main

def continuar():
    continuar = input("¿Deseas continuar? | 1: Sí | 2: No")
    continuar = int(continuar)
    
    if (continuar == 1):
        main.menu
    else:
        exit(0)