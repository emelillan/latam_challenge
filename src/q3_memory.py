from typing import List, Tuple

import json
import re
from collections import Counter
from typing import List, Tuple


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Extrae los 10 usuarios más mencionados de un archivo JSON de tweets.

    Esta función lee un archivo JSON línea por línea, extrae los nombres de usuario
    mencionados en el contenido de cada tweet, y devuelve los 10 usuarios más mencionados.

    Args:
    file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
    List[Tuple[str, int]]: Lista de tuplas conteniendo los 10 usuarios más mencionados
                           y el número de menciones, ordenados de mayor a menor.

    Nota:
    - Este método está optimizado para uso de memoria, procesando el archivo línea por línea.
    - Utiliza expresiones regulares para extraer los nombres de usuario mencionados.
    """
    # Compilar la expresión regular para mejorar el rendimiento
    username_pattern = re.compile(r'@(\w+)')

    # Inicializar un contador para los nombres de usuario mencionados
    mention_counter = Counter()

    # Procesar el archivo línea por línea
    with open(file_path, 'r') as tweet_file:
        for tweet_json in tweet_file:
            # Parsear cada línea como un objeto JSON
            tweet_data = json.loads(tweet_json.strip())

            # Extraer el contenido del tweet si existe
            tweet_content = tweet_data.get('content', '')

            # Encontrar todos los nombres de usuario mencionados en el contenido
            mentioned_users = username_pattern.findall(tweet_content)

            # Actualizar el contador con los usuarios mencionados
            mention_counter.update(mentioned_users)

    # Obtener los 10 usuarios más mencionados
    top_mentioned_users = mention_counter.most_common(10)

    return top_mentioned_users
