import pandas as pd
import numpy as np
from typing import List, Tuple
import datetime
import json
import numpy as np
from collections import Counter


def q1_time(file_path: str, option=1) -> List[Tuple[datetime.date, str]]:

    if option == 1:
        with open(file_path, 'r') as json_file:
            # Cargar archivo json linea a linea
            data = [json.loads(line.strip()) for line in json_file]
        # Usar una list comprenhension para extraer los campos
        data = [(item['date'], item['user']['username'], item['id'])
                for item in data if 'date' in item and 'user' in item and 'id' in item and 'id' in item['user']]

        # Convertir la lista de tuplas en un dataframe de pandas
        df = pd.DataFrame(data, columns=['date', 'user', 'id'])

        # Convertir campo date en formato datetime
        df['date'] = pd.to_datetime(df['date']).dt.date

        tweet_counts = df.groupby('date').size()
        top_10_dates = tweet_counts.nlargest(10).index
        df_top_10 = df[df['date'].isin(top_10_dates)]
        top_users = df_top_10.groupby('date')['user'].agg(
            lambda x: x.value_counts().index[0])

        # Convertir el resulatado en una lista de tuplas
        result = [(date, user) for date, user in zip(top_10_dates, top_users)]

        return result

    if option == 2:
        with open(file_path, 'r') as json_file:
            data = [json.loads(line.strip()) for line in json_file]

        # Filtrar datos relevantes y convertir fechas
        data = [(datetime.datetime.fromisoformat(item['date']).date(), item['user']['username'])
                for item in data if 'date' in item and 'user' in item]

        dates, users = zip(*data)

        # Contar tweets por fecha
        unique_dates, date_counts = np.unique(dates, return_counts=True)
        top_10_indices = np.argsort(date_counts)[-10:]
        top_10_dates = unique_dates[top_10_indices]

        result = []
        for date in top_10_dates:
            user_counts = Counter(
                user for d, user in zip(dates, users) if d == date)
            top_user = user_counts.most_common(1)[0][0]
            result.append(
                (date, top_user, date_counts[np.where(unique_dates == date)[0][0]]))

        return sorted(result, key=lambda x: x[0])

    if option == 3:

        df = pd.read_json(file_path, lines=True)

        # Procesamiento directo
        df['date'] = pd.to_datetime(df['date']).dt.date
        df['username'] = df['user'].apply(lambda x: x['username'])

        # Contar tweets por fecha
        tweet_counts = df.groupby('date').size()
        top_10_dates = tweet_counts.nlargest(10).index

        # Encontrar el usuario con más tweets en cada una de las 10 fechas
        top_users = df[df['date'].isin(top_10_dates)].groupby(
            'date')['username'].agg(lambda x: x.value_counts().idxmax())

        # Empaquetar resultados
        result = [(date, user, tweet_counts[date])
                  for date, user in top_users.items()]

        return sorted(result, key=lambda x: x[0])

    return "Invalid option"
