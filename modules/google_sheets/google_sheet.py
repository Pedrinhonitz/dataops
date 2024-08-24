from modules.google_sheets.base import GoogleSheetBase

class DeParaKeyErrors(GoogleSheetBase):
    table_name = "airflow.depara_http_key_error"
    page_name = "HTTP Errors"
    spreadsheet_id = '1h6NiQHGS6gUJlthe0cw6r-_VJz4nqVmLrJetQEaxXz8'
    fields = {
        "Error Code": "error_code",
        "Error Description": "error_description"
    }