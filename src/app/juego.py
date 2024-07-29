"""Módulo con la clase Juego. Esta clase controla la partida del juego,
por lo cual se encarga de manejar la lógica del juego y la interacción
con el usuario. La clase recibirá como parámetros un objeto de la clase
Jugador y un objeto de la clase Categoria."""

# Importar módulos

import random
import time
import sys
import os

from utils.models import Categoria, Jugador, Palabra

# Clases

class Juego:
    """Clase para el control de la partida del juego.
    """

    def __init__(self, id: int, jugador: Jugador, categoria: Categoria):
        """Inicializa un objeto de la clase Juego.

        Args:
            id (int): El identificador del juego.
            jugador (Jugador): El jugador que participa en el juego.
            categoria (Categoria): La categoría de las palabras del juego.
        """
        self.id = id
        self.jugador_id = jugador.id
        self.categoria = categoria.id
        self.palabras = []
        self.palabra = None
        self.palabra_oculta = []
        self.intentos = 0
        self.letras_usadas = []
        self.puntaje = 0

# Funciones

