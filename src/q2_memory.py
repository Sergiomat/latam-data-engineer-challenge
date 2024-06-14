from typing import List, Tuple
from collections import Counter
import json
import emoji
import pandas as pd

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que retorna las top 10 emojis más usados con su respectivo conteo.
    Optimizada para uso de memoria.
    
    :param file_path: Ubicación del archivo con los tweets a procesar.
    :return: Lista de tuplas con el emoji y su respectivo conteo.
    """
    # Cargar el DataFrame desde el archivo JSON
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error al decodificar la línea: {e}")
    df = pd.json_normalize(data)
    
    # Función para extraer emojis
    def extract_emojis(s):
        return ''.join(c for c in s if c in emoji.EMOJI_DATA)
    
    # Extraer emojis de la columna 'content' usando generador
    emoji_counter = Counter()
    for content in df['content']:
        emojis = extract_emojis(content)
        emoji_counter.update(emojis)
    
    # Obtener los top 10 emojis
    top_10_emojis = emoji_counter.most_common(10)
    
    return top_10_emojis