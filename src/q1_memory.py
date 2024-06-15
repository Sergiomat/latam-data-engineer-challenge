from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json
import pandas as pd

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Función que retorna las top 10 fechas con más tweets y el usuario con más publicaciones por cada día.
    Optimizada para uso de memoria.
    
    :param file_path: Ubicación del archivo con los tweets a procesar.
    :return: Lista de tuplas con la fecha y el usuario con más publicaciones en esa fecha.
    """
    try:
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Error al decodificar la línea: {e}")
        
        if not data:
            raise ValueError("El archivo está vacío o no contiene datos válidos.")
        
        df = pd.json_normalize(data)
        
        if 'date' not in df.columns or 'user.username' not in df.columns:
            raise KeyError("El DataFrame no contiene las columnas 'date' o 'user.username'.")
        
        # Procesamiento
        date_counts = Counter()
        user_counts_by_date = defaultdict(Counter)
        
        for _, row in df.iterrows():
            try:
                tweet_date = pd.to_datetime(row['date']).date()
                username = row['user.username']
                date_counts[tweet_date] += 1
                user_counts_by_date[tweet_date][username] += 1
            except Exception as e:
                print(f"Error al procesar la fila: {e}")
        
        top_dates = date_counts.most_common(10)
        
        result = []
        for date, count in top_dates:
            top_user = user_counts_by_date[date].most_common(1)[0][0]
            result.append((date, top_user))
        
        return result
    
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no se encontró.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    return []
