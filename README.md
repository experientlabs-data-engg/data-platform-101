# Spark-DP-201

### Steps to use it:

### Step 1: Clone the repository.   
   ```commandline
   git clone git@github.com:experientlabs/spark-dp-101.git
   ```

### Step 2. Generate ssh key pair.
This will be used for establishing communication between airflow and spark nodes. 
So that airflow can run ssh jobs on spark node

```shell
./mwaa-local-env generate-ssh-key
```

### Step 3. Build Image.

```shell
./de-local-env build-image
```

### Step 4. Run the setup.

```shell
./de-local-env start
```

### Step 5. Allow container to write to app directory which is used as volume mount
```shell
chmod -R 777 app/
```

> Feel free to post in the comment section if you run across any problem. 

This is a basic Apache Spark and Airflow setup using Docker Containers. 
This setup is designed for learning and evaluation of Apache spark and airflow systems.
This docker application has all basic interfaces of Apache Spark and Airflow like:
1. Jupyter Notebook http://localhost:4041
2. Spark UI http://localhost:4040
3. Spark History Server http://localhost:18080
4. Airflow UI http://localhost:8080 user: admin password: test
5. Spark Shell 
6. Pyspark Shell 

### Architecture
In current architecture, Airflow container is directly connecting to spark container via docker network bridge
or via ssh connection. However an Ideal architecture can have an intermediate node (Edge Node) that acts as bridge 
between Spark and Airflow. But as the quote goes *Simple is Beautiful*, so let's go ahead with this simple setup.  
> ![architecture.png](resources%2Farchitecture.png)



