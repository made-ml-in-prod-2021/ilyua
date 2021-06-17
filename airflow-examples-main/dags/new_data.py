from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "email": ["old.flanigan@gmail.com"],

    'email_on_failure': True,
    'email_on_retry': True,
    'retry_exponential_backoff': True,
    'retry_delay' : timedelta(seconds=300),
    'retries': 3,

}

with DAG(
        "new_data",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    download = DockerOperator(
        image="airflow-download",
        command="/data/raw/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-download",
        do_xcom_push=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        volumes=["/Users/i.chumak/data:/data"]
    )
    download
