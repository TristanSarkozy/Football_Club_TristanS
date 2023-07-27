import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Football_Club_TristanS')


class Player:
    def __init__(self, name, age):
        """
        Create a Player object with the coresponding attributes
        """
        self.name = name
        self.age = age
        self.goals_scored = 0
        self.games_played = 0

    def __str__(self):
        """
        Return the string containing player details
        """
        return f"{self.name}, Age: {self.age}, Goals Scored: {self.goals_scored}, Games Played: {self.games_played}"

player1 = Player("Dan Suciu", 43)

print(player1)
