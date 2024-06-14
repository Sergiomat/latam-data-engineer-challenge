from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Función que retorna las top 10 fechas con más tweets y el usuario con más publicaciones por cada día.
    Optimizada para tiempo de ejecución.
    
    :param file_path: Ubicación del archivo con los tweets a procesar.
    :return: Lista de tuplas con la fecha y el usuario con más publicaciones en esa fecha.
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
    
    # Procesamiento
    df['date'] = pd.to_datetime(df['date'])
    top_dates = df['date'].dt.date.value_counts().head(10)
    
    result = []
    for date, count in top_dates.items():
        daily_tweets = df[df['date'].dt.date == date]
        top_user = daily_tweets['user.username'].value_counts().idxmax()
        result.append((date, top_user))
    
    return result