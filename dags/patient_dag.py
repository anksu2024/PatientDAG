from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.state import State
from datetime import datetime


default_args = {
    'start_date': datetime(2022, 11, 24, 17, 50, 0)
}


with DAG('patient_dag', schedule_interval='*/5 * * * *', default_args=default_args, catchup=False) as dag:
    def _print_message():
        print("Hello World!!")


    patiently_waiting_task = ExternalTaskSensor(
        task_id='patiently_waiting_task',
        poke_interval=5,
        external_dag_id='leading_dag',
        external_task_id='mark_complete_task',
        allowed_states=[State.SUCCESS]
    )

    display_message_task = PythonOperator(
        task_id='print_message_task',
        python_callable=_print_message
    )

    end_patient_dag = DummyOperator(
        task_id='end_patient_dag'
    )

    patiently_waiting_task >> display_message_task >> end_patient_dag
