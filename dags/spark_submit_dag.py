# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
#
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }
#
# with DAG(
#     dag_id='run_word_count_job',
#     default_args=default_args,
#     description='Run Spark word count example',
#     schedule=None,
#     start_date=datetime(2025, 1, 1),
#     catchup=False,
#     tags=['spark', 'word-count'],
# ) as dag:
#
#     run_word_count_job = SparkSubmitOperator(
#         task_id='run_word_count_job',
#         application='/opt/airflow/spark-jobs/word_count_job.py',  # Path to your Python script
#         conn_id='spark_default',
#         name='word_count_job',
#         conf={
#             'spark.executor.memory': '1g',
#             'spark.executor.cores': '2',
#         },
#         verbose=True,
#     )
#
#     run_word_count_job
