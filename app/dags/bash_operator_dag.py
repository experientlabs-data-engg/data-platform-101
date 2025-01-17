from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id='bash_operator_dag',
    default_args=default_args,
    schedule_interval=None,  # Run on demand
    catchup=False,
) as dag:

    # Task 1: Print Python version
    print_python_version = BashOperator(
        task_id='print_python_version',
        bash_command='python --version',
    )

    # Task 2: Get system info
    get_system_info = BashOperator(
        task_id='get_system_info',
        bash_command='uname -a',
    )

    # Set task dependencies
    print_python_version >> get_system_info
