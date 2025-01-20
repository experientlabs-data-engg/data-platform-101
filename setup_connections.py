import json
from time import sleep

import requests as requests
from requests.auth import HTTPBasicAuth

MAX_WAIT_TIME = 900
SLEEP_TIME = 20


def setup_pools(basic_auth):
    for pool in json.loads(open("pools.json").read()):
        pool_name = pool["name"]
        print(f"Checking if pool {pool_name} exists")
        response = requests.get(f"http://localhost:8080/api/v1/pools/{pool_name}", auth=basic_auth)
        print(response)
        if response.status_code == 404:
            print(f"Pool {pool_name} does not exist, setting up..")
            requests.post("http://localhost:8080/api/v1/pools", json=pool, auth=basic_auth)
        else:
            print(f"Pool {pool_name} exists, updating.. {pool}")
            print(requests.patch(f"http://localhost:8080/api/v1/pools/{pool_name}", json=pool, auth=basic_auth))


def wait_and_setup_connection(basic_auth):
    wait_time = 0
    while True:
        try:
            print("Checking if SSH connection exists..")
            response = requests.get("http://localhost:8080/api/v1/connections/ssh_executor_local", auth=basic_auth)
            print(str(response.status_code) + ":" + response.text)
            if response.status_code == 404:
                print("SSH connection does not exist, setting up..")
                ssh_conn = {
                    "connection_id": "ssh_executor_local",
                    "conn_type": "ssh",
                    "host": "executor",
                    "login": "executor",
                    "extra": "{\"key_file\":\"/usr/local/airflow/.ssh/id_rsa\"}"
                }
                requests.post("http://localhost:8080/api/v1/connections", json=ssh_conn, auth=basic_auth)
            return
        except requests.exceptions.ConnectionError as e:
            print(e)
        sleep(SLEEP_TIME)
        wait_time += SLEEP_TIME
        if wait_time > MAX_WAIT_TIME:
            raise Exception("Could not connect to Airflow")


def wait_and_setup_spark_connection(basic_auth):
    wait_time = 0
    while True:
        try:
            print("Checking if Spark connection exists..")
            response = requests.get("http://localhost:8080/api/v1/connections/spark-connection", auth=basic_auth)
            print(str(response.status_code) + ":" + response.text)
            if response.status_code == 404:
                print("Spark connection does not exist, setting up..")
                spark_conn = {
                    "connection_id": "spark-connection",
                    "conn_type": "spark",
                    "host": "spark://spark",
                    "port": "4040",
                    "extra": json.dumps({"queue": "root.default"})
                }
                requests.post("http://localhost:8080/api/v1/connections", json=spark_conn, auth=basic_auth)
            return
        except requests.exceptions.ConnectionError as e:
            print(e)
        sleep_time = 5
        sleep(sleep_time)
        wait_time += sleep_time
        if wait_time > 30:  # Maximum wait time
            raise Exception("Could not connect to Airflow")


if __name__ == "__main__":
    basic_auth = HTTPBasicAuth('admin', 'test')
    # wait_and_setup_connection(basic_auth)
    # setup_pools(basic_auth)
    wait_and_setup_spark_connection(basic_auth)
