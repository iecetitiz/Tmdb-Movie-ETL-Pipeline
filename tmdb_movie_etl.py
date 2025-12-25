import requests
import pandas as pd
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlmodel import create_engine
import io


import io
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-sdu", "--sqlalchemy_database_url", required=True, type=str,
                    help="sqlalchemy_database_url")
ap.add_argument("-url", "--source_file_url", required=True, type=str, default='https://api.themoviedb.org/3/discover/movie',
                    help="url. Default: https://api.themoviedb.org/3/discover/movie")
ap.add_argument("-t", "--token", required=True, type=str,
                    help="TMDB token")


args = vars(ap.parse_args())

sqlalchemy_database_url = args['sqlalchemy_database_url']
source_file_url = args['source_file_url']
token = args['token']


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token}"
}

all_results = []

for page in range(1, 30):  # 1 → 30
    params = {
        "include_adult": "false",
        "include_video": "false",
        "language": "en-US",
        "page": page,
        "sort_by": "popularity.desc"
    }

    response = requests.get(source_file_url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Hata! Page {page}, status: {response.status_code}")
        break

    data = response.json()
    all_results.extend(data["results"])

# print(f"Toplam film sayısı: {len(all_results)}")

df = pd.DataFrame(all_results)

engine = create_engine(sqlalchemy_database_url, echo=True)

# Write pandas dataframe to postgresql table
df.to_sql('tmdb_movie_discover', con=engine, if_exists='replace', index=False)




