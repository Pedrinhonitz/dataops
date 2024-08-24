from utils.tratament import transform
from airflow.exceptions import AirflowException
from hooks.google_sheets_hook import GoogleSheetHook
from modules.base.base_extract_module import BaseExtractModule


class GoogleSheetBase(BaseExtractModule):
    sql=None
    page_name=None
    is_clear=False
    spreadsheet_id=None
    range_sheet='A2:Z1000000'

    def __init__(self) -> None:    
        self.google_sheet_hook = GoogleSheetHook()
        super().__init__()

    def extract(self) -> None:
        if self.sql:
            df = self.extract_postgres(
                self.sql
            )
        else:
            df = self.google_sheet_hook.get_google_sheet(
                self.spreadsheet_id, 
                f"{self.page_name}!{self.range_sheet}"
            )
        
        if df.empty:
            raise AirflowException(f"DataFrame Empty: {df.shape}")

        df = transform(df, self.fields)
        df.to_parquet(self.file_path)


    def load(self) -> None:
        from pandas import read_parquet

        df = read_parquet(self.file_path)

        if self.sql:
            self.load_postgres(
                df,
                self.table_name,
                self.is_truncate
            )
        else:
            self.google_sheet_hook.push_google_sheet(
                df, 
                self.spreadsheet_id, 
                self.page_name, 
                self.range_sheet, 
                self.is_clear
        )

    def delete_temp_file(self) -> None:
        from os import remove
        from os.path import exists

        if exists(self.file_path):
            remove(self.file_path)
        else:
            raise FileNotFoundError(self.file_path)
