
import json
from datetime import datetime
from typing import List, Tuple
from collections import Counter
import pandas as pd


def q1_memory(file_path: str, option=1) -> List[Tuple[datetime.date, str, int]]:

    if option == 1:
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                # Parse each line as a separate JSON object
                d = json.loads(line.strip())
                data.append((datetime.fromisoformat(
                    d['date'].replace('Z', '+00:00')).date(),
                    d['user']['username'], d['id']))

        # Traer las 10 fechas con más tweets
        top_10_dates = Counter([d[0] for d in data]).most_common(10)

        # Encontrar el usuario con más tweets por fecha
        result = [(date, user) for date, user, _ in [
            (date, Counter([d[1] for d in data if d[0] == date]
                           ).most_common(1)[0][0], count)
            for date, count in top_10_dates]]

        return sorted(result, key=lambda x: x[0])

    elif option == 2:
        date_counts = Counter()
        date_user_counts = {}

        with open(file_path, 'r') as file:
            for line in file:
                tweet = json.loads(line)
                date = datetime.fromisoformat(
                    tweet['date'].replace('Z', '+00:00')).date()
                user = tweet['user']['username']

                date_counts[date] += 1

                if date not in date_user_counts:
                    date_user_counts[date] = Counter()
                date_user_counts[date][user] += 1

        # Get the top 10 dates with the most tweets
        top_10_dates = date_counts.most_common(10)

        result = []
        for date, _ in top_10_dates:
            # Find the user with the most tweets for this specific date
            top_user = date_user_counts[date].most_common(1)[0][0]
            result.append((date, top_user))

        return sorted(result, key=lambda x: x[0])

    elif option == 3:

        # Usar un generador para cargar el JSON en chunks, lo que reduce el uso de memoria
        chunk_size = 100  # Ajustar según la memoria disponible
        chunks = pd.read_json(file_path, lines=True, chunksize=chunk_size)

        # Inicializar un DataFrame vacío para acumular los resultados
        df = pd.DataFrame()

        # Procesar los chunks y filtrar columnas
        for chunk in chunks:
            chunk = chunk[['date', 'user', 'id']]
            chunk['user'] = chunk['user'].apply(lambda x: x['username'])
            chunk['date'] = pd.to_datetime(chunk['date']).dt.date
            df = pd.concat([df, chunk])

        # Encontrar las 10 fechas con más tweets y el usuario más frecuente en cada una
        top_users = (df.groupby('date')['user']
                     .value_counts()
                     .groupby(level=0)
                     .nlargest(1)
                     .reset_index(level=1, drop=True)
                     )

        # Seleccionar las 10 fechas con más tweets
        top_10_dates = top_users.groupby(level=0).sum().nlargest(10).index

        # Filtrar y obtener el resultado final como una lista de tuplas
        result = [(date, top_users[date].reset_index()['user'][0])
                  for date in top_10_dates]
        return sorted(result, key=lambda x: x[0])

    return "Invalid option"
