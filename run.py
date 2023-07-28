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
        return f"{self.name}, Age: {self.age}, Goals Scored: {self.goals_scored}, Games Played: {self.games_played}\n"
"""
player1 = Player("Dan Suciu", 43)

print(player1)
"""
class FootballClub:
    def __init__(self):
        """
        Create a FootballClub object with an Attribute list to store the players from club
        """
        self.players = []

    def add_player(self, name, age):
        """
        Add new players to the football club
        Raise ValueError if conditions are not met
        Print result to console
        """
        if not name:
            raise ValueError("Please provide a valid name!")

        try:
            age = int(age)
            if age < 18 or age > 50:
                raise ValueError("Age should be between 18 and 50!")
        except ValueError:
            raise ValueError("Age must be a number between 18 and 50!")

        # Check if a player with the same name and age already exists
        for player in self.players:
            if player.name == name and player.age == age:
                raise ValueError(f"{name}, Age: {age} already exists in the club!")
        player = Player(name, age)
        self.players.append(player)
        print(f"{name} has been added to the club!\n")
    """
    club = FootballClub()

    try:
        club.add_player("Dan Suciu", 43)
        club.add_player("Chuck Norris", 40)
        club.add_player("Dan Suciu", 43)
    except ValueError as e:
        print(f"Error: {e}")
    """
    def delete_player(self, name):
        """
        Delete a player from the football club
        """
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                print(f"{name} has been deleted from the club!\n")
                return
        print(f"{name} doesnt belong to this club!\n")

    def list_all_players(self):
        """
        List all players in the football club
        """
        if not self.players:
            print("No players added in the club!\n")
            return

        for player in self.players:
            print(player)