from base_dags.base_dag import BaseDAG
from modules.google_sheets.google_sheet import *
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from modules.google_sheets.base import GoogleSheetBase

class GoogleSheetBaseDag(BaseDAG):


    def __init__(self, module:GoogleSheetBase, scheduler:str = '@once', tags:list = []):

        self.module = module()

        self.dag_name = self.module.dag_name
        self.limit=self.module.dag_name
        self.scheduler = scheduler
        self.tags = ['google-sheet'] + tags
        
        super().__init__(
            dag_name= self.dag_name,
            limit = self.limit,
            scheduler = self.scheduler,
            tags = self.tags
        )


    def build(self):
        with self:
            start_task = DummyOperator(
                task_id='start_task'
            )

            extract_task = PythonOperator(
                task_id='extract_task',
                python_callable=self.module.extract
            )

            load_task = PythonOperator(
                task_id='load_task',
                python_callable=self.module.load
            )

            delete_temp_file_task = PythonOperator(
                task_id='delete_temp_file_task',
                python_callable=self.module.delete_temp_file    
            )

            end_task = DummyOperator(
                task_id='end_task'
            )

            start_task >> extract_task >> load_task >> delete_temp_file_task >> end_task
        
        return self