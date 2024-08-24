from utils.system import create_if_not_exists
from hooks.postgresql_hook import BasePostgresHook
from airflow.utils.log.logging_mixin import LoggingMixin

class BaseExtractModule(BasePostgresHook, LoggingMixin):
    table_name:str = None
    fields:dict = {}
    is_truncate:bool = True
    limit=10_000

    def __init__(self) -> None:
        self.dag_name = f"{self.table_name.replace('.', '_')}_dag"
        self.dir_path = f"/opt/airflow/"
        create_if_not_exists(self.dir_path)
        self.file_path = f"{self.dir_path}{self.table_name.replace('.', '_')}/data.parquet"
        
        super().__init__('lake-postgres')


    def extract(self) -> None:
        raise NotImplementedError()


    def load(self) -> None:
        raise NotImplementedError()


    def delete_tmp_file(self) -> None:
        raise NotImplementedError()