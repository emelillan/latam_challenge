from typing import List, Tuple
import emoji
import json
from collections import Counter
import concurrent.futures


def process_chunk(chunk):
    emoji_counter = Counter()
    for line in chunk:
        content = json.loads(line).get("content", "")
        for value in emoji.analyze(content):
            emoji_counter[value.chars] += 1
    return emoji_counter


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path, 'r') as file_data:
        lines = file_data.readlines()

    # Dividir el trabajo en chunks
    # Ajustar según el número de cores disponibles
    chunk_size = len(lines) // 16
    chunks = [lines[i:i + chunk_size]
              for i in range(0, len(lines), chunk_size)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_chunk, chunks)

    # Combinar los contadores
    final_counter = Counter()
    for counter in results:
        final_counter.update(counter)

    # Obtener los 10 emojis más comunes
    top_10_emojis = final_counter.most_common(10)
    return top_10_emojis
