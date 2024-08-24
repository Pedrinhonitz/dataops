# from airflow.models.dag import DAG
from modules.google_sheets.google_sheet import DeParaKeyErrors
from base_dags.google_sheet_dags import GoogleSheetBaseDag


dags = [
    GoogleSheetBaseDag(module=DeParaKeyErrors, scheduler='36 4 * * *')
]

for dag in dags:
    globals()[dag.dag_name] = (dag.build())