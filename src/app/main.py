"""
PROYECTO: Ahorcado
FECHA DE INICIO: 07-04-2024
OBJETIVO: Implementar el juego del ahorcado
INTEGRANTES:
    - Nombre: Juan Peña
      Email: ju.penag@duocuc.cl

Este es el archivo principal del proyecto, donde se encuentra la lógica del juego.
"""

# Importar módulos

import os
import sys
import time


# Definir funciones

def cls():
    """Limpia la pantalla de la consola."""
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    """Imprime el banner del juego."""
    print( """
          _                             _                    
    /\\   | |                           | |                   
   /  \\  | |__   ___  _ __ ___ __ _  __| | ___   _ __  _   _ 
  / /\\ \\ | '_ \\ / _ \\| '__/ __/ _` |/ _` |/ _ \\ | '_ \\| | | |
 / ____ \\| | | | (_) | | | (_| (_| | (_| | (_) || |_) | |_| |
/_/    \\_\\_| |_|\\___/|_|  \\___\\__,_|\\__,_|\\___(_) .__/ \\__, |
                                                | |     __/ |
                                                |_|    |___/ 
(c) 2024 Juan Peña.
""")
    

def animacion_tres_puntos(texto: str, vueltas: int = 1):
    """Imprime un texto con una animación de tres puntos al final.

    Args:
        texto (str): Texto a imprimir.
        vueltas (int, optional): Son la veces que se repetirá la animación. Defaults to 1.
    """
    for _ in range(vueltas):
        for i in range(4):
            print(f"\r{texto}", flush=True, end="")
            print("." * i, flush=True, end="")
            time.sleep(0.5)


def menu_principal():
    """Despliega el menú principal del juego.
    """
    cls()
    banner()
    print("Menú principal:")
    print("1. Jugar")
    print("2. Puntajes")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        jugar()
    elif opcion == "2":
        puntajes()
    elif opcion == "3":
        print("¡Hasta luego!")
        sys.exit(0)        
    else:
        print("Opción no válida.")
        menu_principal()


def jugar():
    """Inicia una partida del juego.
    """
    palabras_prueba = ["hola", "mundo", "python", "programacion", "juego", "ahorcado"]

    cls()
    banner()
    time.sleep(1)
    print("¡Bienvenido al juego del ahorcado!\n\n")
    time.sleep(1)
    animacion_tres_puntos("Estoy pensando en una palabra", 3)
    time.sleep(2)
    print("\n\n¡Listo! Adivina la palabra.")
    print(palabras_prueba)


def puntajes():
    """Muestra los 5 mejores puntajes del juego."""
    pass

# ----------------------------------------------------------




if __name__ == "__main__":
    print(menu_principal())
