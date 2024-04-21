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
import random
import time


# Definir funciones
def cls():
    """Limpia la pantalla de la consola."""
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    """Retorna el banner del juego."""
    return """
          _                             _                    
    /\   | |                           | |                   
   /  \  | |__   ___  _ __ ___ __ _  __| | ___   _ __  _   _ 
  / /\ \ | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ | '_ \| | | |
 / ____ \| | | | (_) | | | (_| (_| | (_| | (_) || |_) | |_| |
/_/    \_\_| |_|\___/|_|  \___\__,_|\__,_|\___(_) .__/ \__, |
                                                | |     __/ |
                                                |_|    |___/ 
(c) 2024 Juan Peña.
"""


