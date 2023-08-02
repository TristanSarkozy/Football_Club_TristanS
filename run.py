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
        return (
            f"{self.name}, Age: {self.age}, Goals Scored: {self.goals_scored},"
            f" Games Played: {self.games_played}\n"
        )
                                                               

class FootballClub:
    """
    Add a class to represent a Football Club
    """
    def __init__(self):
        """
        Create a FootballClub object with an Attribute list
        to store the players from the club.
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
                    raise ValueError("Age between 18 and 50!!!")
            except ValueError:
                raise ValueError("Type a number between 18 and 50!!!")

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
                if player.name == name:
                    print(f"\n{name} already exists in the club!")
                    return

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
            for row in player_data:
                name, age, goals_scored, games_played = row
                age = int(age)
                goals_scored = int(goals_scored)
                games_played = int(games_played)
                player = Player(name, age, goals_scored, games_played)
                self.players.append(player)

        except Exception as e:
            print(f"Failed to fetch players from Google Sheets! Error: {e}")
            return

    def up_sheet(self, name, age, goals_scored, games_played):
        """
        Update player data in the Google Sheets with the new values.
        """
        try:
            worksheet = SHEET.worksheet("Players")
            cell = worksheet.find(name)

            # Get the row number of the player's data
            row_number = cell.row

            # Update age, games played, goals scored in Google Sheets
            worksheet.update_cell(row_number, 2, age)
            worksheet.update_cell(row_number, 3, games_played)
            worksheet.update_cell(row_number, 4, goals_scored)

            print(f"Player data for '{name}' updated in the Google Sheets!")

        except gspread.exceptions.CellNotFound:
            print(f"Player with name '{name}' not found in the Google Sheets.")
        except Exception as e:
            print(f"Failed to update player data in Google Sheets. Error: {e}")


def main():
    """
    Function to run the Football Club Automation System.
    Allow users to add players, delete players, list all players,
    edit an existing player or exit the program.
    Show statements if requirements are not met.
    """
    football_club = FootballClub()
    football_club.load_players_from_sheet()

    # Print the main menu
    print("<<<<< Football Club Automation System >>>>>\n")
    print("1. Add Player")
    print("2. List All Players")
    print("3. Edit Player")
    print("4. Exit\n")

    while True:
        choice = input("Enter your choice (1/2/3/4): \n")

        if choice == '1':
            while True:
                name = input("Enter player name: \n")
                if not any(char.isdigit() for char in name):
                    break
                else:
                    print("\nName should only contain letters and no digits!")

            while True:
                age = input("Enter player age: \n")
                try:
                    age = int(age)
                    if age < 18 or age > 50:
                        raise ValueError("\nAge between 18 and 50!!!")
                except ValueError as e:
                    print(f"\nType a number between 18 and 50!!! {e}")
                else:
                    break

            while True:
                goals_scored = input("Enter number of goals: \n")
                try:
                    goals_scored = int(goals_scored)
                except ValueError:
                    print("\nGoals scored must be a number!")
                else:
                    break

            while True:
                games_played = input("Enter number of games played: \n")
                try:
                    games_played = int(games_played)
                except ValueError:
                    print("\nGames played must be a number!")
                else:
                    break

            football_club.add_player(name, age, goals_scored, games_played)

        elif choice == '2':
            print("List of all players: ")
            football_club.list_all_players()

        elif choice == '3':
            name = input("Enter player name to edit: \n")
            for player in football_club.players:
                if player.name == name:
                    print(f"\nPlayer found:\n{player}")
                    while True:
                        try:
                            new_age = int(input("Enter new age: \n"))
                            if new_age < 18 or new_age > 50:
                                raise ValueError("\nAge between 18 and 50!!!")
                            break
                        except ValueError as e:
                            print(f"\nType a number between 18 and 50!!! {e}")

                    while True:
                        try:
                            new_goals = int(input("Add new goals: \n"))
                            break
                        except ValueError:
                            print("\nGoals scored must be a number!")

                    while True:
                        try:
                            new_games = int(input("Add new games: \n"))
                            break
                        except ValueError:
                            print("\nGames played must be a number!")

                    football_club.up_sheet(name, new_age, new_goals, new_games)

                    print("Player data updated successfully!\n")
                    break
            else:
                print(f"Player with name '{name}' not found in the club.\n")

        elif choice == '4':
            print("Exiting the program..")
            break
        else:
            print("Invalid choice. Please try again!")


# Check if the script runs as the main
if __name__ == "__main__":
    main()