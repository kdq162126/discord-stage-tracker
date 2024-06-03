import gspread
import os
from dotenv import load_dotenv
load_dotenv()

class GoogleSheet:
    def __init__(self, url=None):

        self.credentials = {
            "type": "service_account",
            "private_key_id": os.getenv('GOOGLE_PRIVATE_KEY_ID'),
            "private_key": os.getenv('GOOGLE_PRIVATE_KEY'),
            "client_email": os.getenv('GOOGLE_CLIENT_EMAIL'),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "universe_domain": "googleapis.com"
        }

        self.gc = gspread.service_account_from_dict(self.credentials)
        if not url:
            url = os.getenv('SHEET_URL')

        try:
            self.url = url
            self.sh = self.gc.open_by_url(url)
            return
        except:
            print(f'ERROR === bot.py -- 43: Invalid URL')

        print('Try to create a new sheet')
        self.sh = self.gc.create('Discord Channel Tracking')
        self.url = self.sh.url
        print(f'New sheet was created successfully, link: {self.url}')


    def get_client_email(self):
        return self.credentials['client_email']

    def update_url(self, url: str):
        self.url = url
        self.sh = self.gc.open_by_url(url)

    def share_writer(self, email: str):
        self.sh.share(email, perm_type='user', role='writer')


    def get_rows(self, sheet_url: str):
        print(self.sh.worksheets())
        print(self.sh.sheet1.get('A1'))

