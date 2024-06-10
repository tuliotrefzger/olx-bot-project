import os.path
import pprint
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheetAPI:
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    def __init__(
        self,
        spreadsheet_id,
        creds_path="credentials.json",
        token_path="token.json",
    ):
        self.spreadsheet_id = spreadsheet_id
        self.creds_path = creds_path
        self.token_path = token_path
        self.creds = self._get_credentials()
        self.service = build("sheets", "v4", credentials=self.creds)

    def _get_credentials(self):
        creds = None
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.creds_path, self.SCOPES
                )
                creds = flow.run_local_server(port=0)
            with open(self.token_path, "w") as token:
                token.write(creds.to_json())
        return creds

    def append_values(self, range_name, values):
        try:
            sheet = self.service.spreadsheets()
            body = {"values": values}
            result = (
                sheet.values()
                .append(
                    spreadsheetId=self.spreadsheet_id,
                    range=range_name,
                    valueInputOption="USER_ENTERED",
                    body=body,
                )
                .execute()
            )
            print(f"Appended values: {result}")
        except HttpError as err:
            print(f"An error occurred: {err}")

    def get_recent_urls(self, sheet_name, date_column="J", url_column="K", days=21):
        try:
            sheet = self.service.spreadsheets()
            range_name = f"{sheet_name}!A1:Z"  # Adjust as needed to cover all columns
            result = (
                sheet.values()
                .get(spreadsheetId=self.spreadsheet_id, range=range_name)
                .execute()
            )
            rows = result.get("values", [])

            recent_urls = []
            cutoff_date = datetime.now() - timedelta(days=days)
            date_format = "%Y-%m-%d %H:%M:%S"

            for row in rows[1:]:
                if len(row) > ord(date_column) - ord("A"):
                    date_str = row[ord(date_column) - ord("A")]
                    row_date = datetime.strptime(date_str, date_format)
                    try:
                        row_date = datetime.strptime(date_str, date_format)
                        if row_date >= cutoff_date:
                            recent_urls.append(row[ord(url_column) - ord("A")])
                    except ValueError:
                        continue  # Skip rows with invalid date format

            pprint.pprint(recent_urls)
            return recent_urls

        except HttpError as err:
            print(f"An error occurred: {err}")
            return []


if __name__ == "__main__":
    SAMPLE_SPREADSHEET_ID = "1bGri5TIelYz53QnZ1o-XY4DY5Tu0EvyT7aUyQFzZh3o"

    # # Add a row to the spreadsheet
    # SAMPLE_RANGE_NAME = "Sheet1!A1"
    # current_date_time = datetime.now()
    # current_date_time_str = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    # VALUE_DATA = [
    #     [
    #         "FIAT DOBLO EX 1.3 FIRE 16V 80CV 4/5P",
    #         "FIAT",
    #         2005,
    #         "Cinza",
    #         50000,
    #         20000,
    #         20000,
    #         21825,
    #         current_date_time_str,
    #         "https://df.olx.com.br/distrito-federal-e-regiao/autos-e-pecas/carros-vans-e-utilitarios/carro-doblo-2005-1304488542?lis=listing_2020",
    #     ]
    # ]
    # sheet_api = GoogleSheetAPI(spreadsheet_id=SAMPLE_SPREADSHEET_ID)
    # sheet_api.append_values(SAMPLE_RANGE_NAME, VALUE_DATA)

    # -----------------------------------------------

    # Find most recent URLs.
    sheet_api = GoogleSheetAPI(spreadsheet_id=SAMPLE_SPREADSHEET_ID)
    # recent_urls = sheet_api.get_recent_urls("Sheet1")
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(recent_urls)
