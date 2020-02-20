import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from rainbow import RainbowLogger
logger = RainbowLogger(__name__)


class Seos:
    def __init__(
        self,
        credentials_file,
        spreadsheet_id=None,
        token_file="./token.pickle"
    ):
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
        creds = None
        if os.path.exists(token_file):
            with open(token_file, "rb") as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file,
                    SCOPES
                )
                creds = flow.run_console()
            with open(token_file, "wb") as token:
                pickle.dump(creds, token)

        self.service = build("sheets", "v4", credentials=creds)
        self.sheet = self.service.spreadsheets()
        self.sheet_id = spreadsheet_id

        # defaults
        self._scope = ""
        self._sheet_name = ""

    @property
    def sheet_name(self):
        return self._sheet_name

    @sheet_name.setter
    def sheet_name(self, name):
        self._sheet_name = name

    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, scope):
        self._scope = scope

    def extract(self):
        if self.sheet_id is None:
            logger.error("Sheet ID is not set")
            return

        if not self.sheet_name or not self.scope:
            logger.warning("Nothing to extract")
            return

        try:
            result = self.sheet.values().get(
                spreadsheetId=self.sheet_id,
                range="{}!{}".format(self.sheet_name, self.scope)
            ).execute()
        except HttpError:
            return []

        values = result.get("values", [])

        if values:
            return values
