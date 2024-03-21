# cli.py

from helpers import list_games, add_game, list_stadiums, add_stadium, list_teams, add_team, \
    list_players, add_player, list_fixtures, schedule_fixture, connect_to_database

def main():
    # Establish connection to the database
    conn = connect_to_database("sports.db")

    print("Welcome to the Game Fixture Manager!")

    while True:
        print("\nMenu:")
        print("1. List Games")
        print("2. Add Game")
        print("3. List Stadiums")
        print("4. Add Stadium")
        print("5. List Teams")
        print("6. Add Team")
        print("7. List Players")
        print("8. Add Player")
        print("9. List Fixtures")
        print("10. Schedule Fixture")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_games(conn)
        elif choice == "2":
            game_name = input("Enter the name of the game: ")
            add_game(conn, game_name)  # Pass conn and game_name as arguments
        # Similarly, modify other function calls to pass the conn argument where necessary
        elif choice == "0":
            print("Goodbye! See you later!!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close connection to the database after exiting the loop
    conn.close()

if __name__ == "__main__":
    main()
