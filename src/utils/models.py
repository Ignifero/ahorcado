"""Módulo con los modelos de la base de datos."""

# Importar módulos

# Clases

class Jugador:
    """Modelo para los datos de un jugador.
    """

    def __init__(self, id: int, nick: str, email: str, puntaje_max: int = 0):
        """Inicializa un objeto de la clase Jugador.

        Args:
            id (int): El identificador del jugador.
            nick (str): El apodo o nombre de usuario del jugador. Tiene que ser único.
            email (str): El correo electrónico del jugador. Tiene que ser único.
            puntaje (int): El puntaje del jugador.
        """
        self.id = id
        self.nick = nick
        self.email = email
        self.puntaje_max = puntaje_max
        

    def __str__(self):
        return f"{self.nick} ({self.email}): {self.puntaje} puntos"
    

class Categoria:
    """Modelo para los datos de una categoría.
    """

    def __init__(self, id: int, nombre: str):
            """Inicializa un objeto de la clase Categoria.

            Args:
                id (int): El identificador de la categoría.
                nombre (str): El nombre de la categoría. Tiene que ser único.
            """
            self.id = id
            self.nombre = nombre

    def __str__(self):
        return self.nombre


class Palabra:
    """Modelo para los datos de una palabra.
    """

    def __init__(self, id: int, palabra_: str, categoria: Categoria):
        """Inicializa un objeto de la clase Palabra.

        Args:
            id (int): El identificador de la palabra.
            palabra_ (str): La palabra a adivinar. Tiene que ser única.
            categoria (Categoria): La categoría de la palabra.
        """
        self.id = id
        self.palabra_ = palabra_
        self.categoria_id = categoria.id

    def __str__(self):
        return self.palabra_
    
