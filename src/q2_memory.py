from typing import List, Tuple
import json
import emoji
from collections import Counter


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que recibe la ruta de un archivo y retorna una lista con las 10
    emojis más usados en los mensajes del archivo.

    :param file_path: str
    :return: List[Tuple[str, int]]
    """

    emoji_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            if 'content' in data:
                content = data['content']
                emoji_counter.update(
                    [value.chars for value in emoji.analyze(content)])

    top_10_emojis = emoji_counter.most_common(10)

    return top_10_emojis
