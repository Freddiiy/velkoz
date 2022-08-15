import os


class Api_key:
    api_key: str

    def __init__(self):
        self.api_key = os.getenv("LEAGUE_APIKEY")

    def get_api_key(self):
        return self.api_key

    def set_api_key(self, key: str):
        self.api_key = key
