import json
from collections import Counter
from typing import List, Tuple
import re

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que retorna los top 10 usuarios más influyentes en función del conteo de las menciones (@) que registra.
    Optimizada para tiempo de ejecución.
    
    :param file_path: Ubicación del archivo con los tweets a procesar.
    :return: Lista de tuplas con el usuario y su respectivo conteo.
    """
    try:
        mention_pattern = re.compile(r'@\w+')
        mentions = []

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    tweet = json.loads(line)
                    content = tweet.get('content', '')
                    mentions.extend(mention_pattern.findall(content))
                except json.JSONDecodeError as e:
                    print(f"Error al decodificar la línea: {e}")
        
        if not mentions:
            raise ValueError("No se encontraron menciones en los datos proporcionados.")
        
        mention_counts = Counter(mentions)
        top_mentions = mention_counts.most_common(10)
        
        return [(mention[1:], count) for mention, count in top_mentions]  # Remove '@' from username

    except FileNotFoundError:
        print(f"El archivo '{file_path}' no se encontró.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    return []
