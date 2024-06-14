import json
from collections import Counter
from typing import List, Tuple
import re

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que retorna las top 10 usuarios más influyentes en función del conteo de las menciones (@) que registra.
    Optimizada para tiempo de ejecución.
    
    :param file_path: Ubicación del archivo con los tweets a procesar.
    :return: Lista de tuplas con el usuario y su respectivo conteo.
    """
    mention_pattern = re.compile(r'@\w+')
    mentions = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            content = tweet.get('content', '')
            mentions.extend(mention_pattern.findall(content))
    
    mention_counts = Counter(mentions)
    top_mentions = mention_counts.most_common(10)
    return [(mention[1:], count) for mention, count in top_mentions]  # Remove '@' from username
