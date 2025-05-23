# -*- coding: utf-8 -*-
"""dag

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tHib4-LLLOfPIL3FpbjwthdPTCA_JkuD
"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='dwh_project_update',
    default_args=default_args,
    schedule_interval=None,
    tags=['example', 'bash', 'python_script']
) as dag:

    run_script = BashOperator(
        task_id='dwh_project_update_task',
        bash_command='python3 -u /home/shahmeerkm/airflow/dags/script18.py'
    )

run_script