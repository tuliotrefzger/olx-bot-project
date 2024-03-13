import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheets:
    def __init__(self):
        self.spreadsheet_id = "1bGri5TIelYz53QnZ1o-XY4DY5Tu0EvyT7aUyQFzZh3o"
        self.api_key = "AIzaSyBd90QAyKEYYjNxHYSw5GPhQhoVLxJNPH0"
        self.sheet_name = "Sheet1"

    def authenticate_sheets(self):
        return build("sheets", "v4", developerKey=self.api_key).spreadsheets()

    def get_spreadsheet(self):
        result = (
            self.authenticate_sheets()
            .values()
            .get(spreadsheetId=self.spreadsheet_id, range=f"{self.sheet_name}!A1:C3")
            .execute()
        )
        return result.get("values", [])

    def get_sheet_range(self):
        spreadsheet = (
            self.authenticate_sheets().get(spreadsheetId=self.spreadsheet_id).execute()
        )
        sheets_metadata = spreadsheet.get("sheets", [])
        for sheet in sheets_metadata:
            if sheet["properties"]["title"] == self.sheet_name:
                return (
                    sheet["properties"]["title"],
                    sheet["properties"]["gridProperties"],
                )


if __name__ == "__main__":
    google_sheets_instance = GoogleSheets()
    print(google_sheets_instance.get_sheet_range())
    # sheets = google_sheets_instance.get_spreadsheet()
    # print(sheets)
