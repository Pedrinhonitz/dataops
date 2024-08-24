from pandas import DataFrame
from airflow.exceptions import AirflowException
from airflow.providers.google.suite.hooks.sheets import GSheetsHook


class GoogleSheetHook(GSheetsHook):
    connection_id = "google-sheet"

    def __init__(self):
        self.conn = GSheetsHook(self.connection_id)


    def get_google_sheet(self, spreadsheet_id: str, page_sheets: str, header_row=0) -> DataFrame:
        from pandas import DataFrame
        
        try:
            data = self.conn.get_values(
                spreadsheet_id, 
                page_sheets
            )

            df = DataFrame(data)
            df.columns = df.iloc[header_row]
            df = df.drop(header_row)
            df = df.reset_index(drop=True)
            for col in df.columns:
                for ever in ['\r', '\n', '\t', '\f', '\b', '\v', '\0']:
                    df[col] = df[col].apply(lambda x: x.replace(ever, '') if str(x) != 'None' else None)

            return df
        except Exception as error:
            raise AirflowException(f'Failed to Get Spreadsheet: {error} /n spreadsheet_id: {spreadsheet_id} | page_sheets: {page_sheets}')


    def push_google_sheet(self, df, spreadsheet_id: str, page_sheets: str, range_sheets='A2:Z1000000', clear=True) -> bool:
        try:
            if clear:
                _ = self.conn.clear(
                    spreadsheet_id, 
                    range_sheets
                )

                _ = self.conn.append_values(
                    spreadsheet_id, 
                    f'{page_sheets}!{range_sheets}', 
                    df.values.tolist()
                )
            else:
                _ = self.conn.append_values(
                    spreadsheet_id, 
                    f'{page_sheets}!{range_sheets}', 
                    df.values.tolist()
                )
            return True
        except Exception as error:
            raise AirflowException(f'Failed to Push Spreadsheet: {error} /n spreadsheet_id: {spreadsheet_id} | page_sheets: {page_sheets}| range_sheets: {range_sheets}')
        
