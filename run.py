import gspread
from google.oauth2.service_account import Credentials

# Define the required Google API scopes
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Load Google service account credentials 
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Authorize the Google Sheets API client
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet named 'Football_Club_TristanS'
SHEET = GSPREAD_CLIENT.open('Football_Club_TristanS')


class Player:
    """
    Add a class to represent a Player
    """
    def __init__(self, name, age, goals_scored, games_played):
        """
        Create a Player object with the corresponding attributes
        """
        self.name = name
        self.age = age
        self.goals_scored = goals_scored
        self.games_played = games_played

    def __str__(self):
        """
        Return the string containing player details
        """
        return f"{self.name}, Age: {self.age}, Goals Scored: {self.goals_scored}, Games Played: {self.games_played}\n"


class FootballClub:
    """
    Add a class to represent a Football Club
    """
    def __init__(self):
        """
        Create a FootballClub object with an Attribute list to store the players from club
        """
        self.players = []

    def add_player(self, name, age, goals_scored, games_played):
        """
        Add new players to the football club.
        Raise ValueError if conditions are not met.
        Print statements.
        """
        if not any(char.isdigit() for char in name):
            try:
                age = int(age)
                if age < 18 or age > 50:
                    raise ValueError("Age should be between 18 and 50!")
            except ValueError:
                raise ValueError("Age must be a number between 18 and 50!")
        
            try:
                games_played = int(games_played)
            except ValueError:
                raise ValueError("Games played must be a number!")

            try:
                goals_scored = int(goals_scored)
            except ValueError:
                raise ValueError("Goals scored must be a number!")

            # Check if a player with the same name and age already exists
            for player in self.players:
                if player.name == name and player.age == age:
                    raise ValueError(f"{name}, Age: {age} already exists in the club!")

            # Create a new Player object and add it to the list of players
            player = Player(name, age, goals_scored, games_played)
            self.players.append(player)
            print(f"{name} has been added to the club!\n")

            # Update Google Sheets
            try:
                worksheet = SHEET.worksheet("Players")
                row = [name, age, games_played, goals_scored]
                worksheet.append_row(row)
                print("Data added to Google Sheets successfully!")
            except Exception as e:
                print(f"Failed to update Google Sheets. Error:[{e}]")
        else:
            raise ValueError("Name should only contain letters and no digits!")

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

    def load_players_from_sheet(self):
        """
        Load player data from the Google Sheets and store data
        """
        try:
            worksheet = SHEET.worksheet("Players")
            player_data = worksheet.get_all_values()

            # Skip the header row
            player_data = player_data[1:]

            # Create Player objects from the data
            players = []
            for row in player_data:
                row = name, age, goals_scored, games_played
                age = int(age)
                goals_scored = int(goals_scored)
                games_played = int(games_played)
                player = Player(name, age, goals_scored, games_played)
                players.append(player)

            self.players.extend(player)

        except Exception as e:
            print(f"Failed to fetch players from Google Sheets! Error: {e}")
            return


def main():
    """
    Function to run the Football Club Automation System.
    Allow user to add players, delete players, list all players, 
    edit an existing player or exit the program.
    Show statements if requirements not met.
    """
    football_club = FootballClub()
    football_club.load_players_from_sheet()

    # Print the main menu 
    print("<<<<< Football Club Automation System >>>>>\n")
    print("1. Add Player")
    print("2. Delete Player")
    print("3. List All Players")
    print("4. Edit Player")
    print("5. Exit\n")

    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            while True:
                name = input("Enter player name: ")
                if not any(char.isdigit() for char in name):
                    break
                else:
                    print("Name should only contain letters and no digits!")

            while True:
                age = input("Enter player age: ")
                try:
                    age = int(age)
                    if age < 18 or age > 50:
                        raise ValueError("Age should be between 18 and 50!")
                except ValueError as e:
                    print(f"Error: {e}")
                else:
                    break

            while True:
                goals_scored = input("Enter number of goals: ")
                try:
                    goals_scored = int(goals_scored)
                except ValueError:
                    print("Goals scored must be an integer!")
                else:
                    break

            while True:
                games_played = input("Enter number of games played: ")
                try:
                    games_played = int(games_played)
                except ValueError:
                    print("Games played must be an integer!")
                else:
                    break

            football_club.add_player(name, age, goals_scored, games_played)

        elif choice == '2':
            name = input("Enter player name to delete: ")
            football_club.delete_player(name)

        elif choice == '3':
            print("List of all players: ")
            football_club.list_all_players()

        elif choice == '4':
            name = input("Enter player name to edit: ")
            for player in football_club.players:
                if player.name == name:
                    print(f"Player found:\n{player}")
                    while True:
                        try:
                            new_age = int(input("Enter new age: "))
                            if new_age < 18 or new_age > 50:
                                raise ValueError("Age should be between 18 and 50!")
                            player.age = new_age
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                        else:
                            break

                    while True:
                        try:
                            new_goals_scored = int(input("Enter updated goals:"))
                            player.goals_scored = new_goals_scored
                            break
                        except ValueError:
                            print("Goals scored must be an integer!")
                        else:
                            break

                    while True:
                        try:
                            new_games_played = int(input("Enter new games played: "))
                            player.new_games_played = new_games_played
                            break
                        except ValueError:
                            print("Games played must be an integer!")
                        else:
                            break

                    print("Player data updated successfully!\n")
                    break
            else:
                print(f"Player with name '{name}' not found in the club.\n")

        elif choice == '5':
            print("Exiting the program..")
            break
        else:
            print("Invalid choice. Please try again!")


# Check if the script runs as the main
if __name__ == "__main__":
    main()
