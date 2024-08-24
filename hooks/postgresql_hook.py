from pandas import DataFrame
from typing import List, Tuple
from airflow.hooks.postgres_hook import PostgresHook

class BasePostgresHook(PostgresHook):

    def __init__(self, conn_id) -> None:
        super().__init__(conn_id)
        self.conn = self.get_conn()


    def extract_postgres(self, sql: str) -> DataFrame:
        from pandas import read_sql

        df = read_sql(sql, self.conn)
        self.conn.close()
        
        return df


    def load_postgres(self, df: DataFrame, table_name: str, is_truncate: bool = True) -> None:
        from pandas import to_sql   

        if is_truncate:
            if_exists = 'replace'
        else:
            if_exists = 'append'

        to_sql(
            table_name, 
            self.conn, 
            if_exists=if_exists, 
            index=False
        )
        
        self.conn.close()


    def run_query_postgres(self, sql: str)  -> List[Tuple]:
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        self.conn.close()
        
        return result