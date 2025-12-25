from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import os, sys
from airflow import DAG

start_date = datetime(2025, 10, 11)

default_args = {
    'owner': 'airflow',
    'start_date': start_date,
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

sqlalchemy_database_url = Variable.get("sqlalchemy_database_url")
token = Variable.get("TMDB_token")
source_file_url = Variable.get("TMDB_URL")

with DAG('HW13', default_args=default_args, schedule_interval='@once', catchup=False) as dag:
    create_tmdb_table = SQLExecuteQueryOperator(
        task_id="create_tmdb_movie_discover_table",
        conn_id="postgresql_conn",
        sql="""
        CREATE TABLE IF NOT EXISTS tmdb_movie_discover (
        adult BOOLEAN,
        backdrop_path TEXT,
        genre_ids INTEGER[],
        id BIGINT PRIMARY KEY,
        original_language TEXT,
        original_title TEXT,
        overview TEXT,
        popularity DOUBLE PRECISION,
        poster_path TEXT,
        release_date TEXT,
        title TEXT,
        video BOOLEAN,
        vote_average DOUBLE PRECISION,
        vote_count INTEGER
        );
        """
    )

    to_postgresql = SSHOperator(task_id='to_postgres', 
        command=f"""source /dataops/airflowenv/bin/activate && 
                python /dataops/load_from_github_argparse.py -sdu {sqlalchemy_database_url} -url {source_file_url} -t {token}""",
                ssh_conn_id='spark_ssh_conn'),
                    
    create_tmdb_table >> to_postgresql


 


