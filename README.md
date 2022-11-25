# PatientDAG
<hr />

## Step 1:
```
$ docker compose up
```

This docker-compose.yml file was obtained from:
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#fetching-docker-compose-yaml

## Step 2:

Go to a web browser, and navigate to `http://localhost:8080/`

## Step 3:

use `airflow` as `username` and `password`
<br/>
and `Sign In`

## Step 4:
Unpause the DAGs `patient_dag` and `leading_dag`

## Step 5:
1. Wait for the leading_dag to complete it execution
2. The execution of the `patiently_waiting_task` will follow

## Step 6:
Once both the DAGs have completed, check the logs for the `patiently_waiting_task`
and we will discover the `patiently_waiting_task`
frequently  poking `mark_complete_task` to check if it `Succeeded`
