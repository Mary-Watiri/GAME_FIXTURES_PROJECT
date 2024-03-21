# cli.py

from helpers import (
    list_stadiums, add_stadium, list_teams, add_team, list_players,
    add_player, list_fixtures, schedule_fixture, cancel_fixture, remove_player
)

def main():
    print("Welcome to the Game Fixture Manager!")

    while True:
        print("\nMenu:")
        print("1. List Stadiums")
        print("2. Add Stadium")
        print("3. List Teams")
        print("4. Add Team")
        print("5. List Players")
        print("6. Add Player")
        print("7. List Fixtures")
        print("8. Schedule Fixture")
        print("9. Cancel Fixture")
        print("10. Remove Player")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_stadiums()
        elif choice == "2":
            stadium_name = input("Enter the name of the stadium: ")
            location = input("Enter the location of the stadium: ")
            add_stadium(stadium_name, location)
        elif choice == "3":
            list_teams()
        elif choice == "4":
            team_name = input("Enter the name of the team: ")
            add_team(team_name)
        elif choice == "5":
            list_players()
        elif choice == "6":
            player_name = input("Enter the name of the player: ")
            position = input("Enter the position of the player: ")
            team_id = input("Enter the ID of the team: ")
            add_player(player_name, position, team_id)
        elif choice == "7":
            list_fixtures()
        elif choice == "8":
            game_date = input("Enter the date of the game (YYYY-MM-DD): ")
            game_time = input("Enter the time of the game (HH:MM): ")
            game_venue = input("Enter the venue of the game: ")
            match_id = input("Enter the match ID: ")
            
            while True:
                team1_id = input("Enter the ID of the first team: ")
                team2_id = input("Enter the ID of the second team: ")
                
                if team1_id == team2_id:
                    print("Error: Team IDs cannot be the same. Please enter different team IDs.")
                else:
                    schedule_fixture(game_date, game_time, game_venue, match_id, team1_id, team2_id)
                    break

        elif choice == "9":
            match_id = input("Enter the match ID to cancel: ")
            cancel_fixture(match_id)
        elif choice == "10":
            player_id = input("Enter the ID of the player to remove: ")
            remove_player(player_id)
        elif choice == "0":
            print("Adios!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
