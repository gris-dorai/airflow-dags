from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
}

def process(p1):
    print(p1)
    return 'done'

with DAG(dag_id='parallel_dag', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:

    task_4 = PythonOperator(task_id='task_4', python_callable=process, op_args=['my super parameter'])
task_4
        
