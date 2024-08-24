FROM apache/airflow:2.10.0

USER root

RUN apt-get update && \
    apt-get install -y gosu && \
    apt-get install -y nano && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /opt/airflow/requirements.txt
COPY dags /opt/airflow/dags
COPY dbt /opt/airflow/dbt
COPY operators /opt/airflow/operators
COPY hooks /opt/airflow/hooks
COPY modules /opt/airflow/modules
COPY base_dags /opt/airflow/base_dags
COPY utils /opt/airflow/utils
COPY plugins /opt/airflow/plugins
COPY logs /opt/airflow/logs
COPY secrets /opt/airflow/secrets

RUN chown -R airflow: /opt/airflow/ && \
    chmod -R 777 /opt/airflow/

    USER airflow

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow"

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
