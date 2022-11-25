from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

from random import uniform
from datetime import datetime

default_args = {
    'start_date': datetime(2022, 11, 24, 17, 50, 0)
}


with DAG('leading_dag', schedule_interval='*/5 * * * *', default_args=default_args, catchup=False) as dag:
    download_data_task = BashOperator(
        task_id='download_data_task',
        bash_command='sleep 100'
    )

    run_model_task = BashOperator(
        task_id='run_model_task',
        bash_command='sleep 50'
    )

    mark_complete_task = DummyOperator(
        task_id='mark_complete_task'
    )

    download_data_task >> run_model_task >> mark_complete_task
