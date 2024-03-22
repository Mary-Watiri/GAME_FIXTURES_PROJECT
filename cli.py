from helpers import (
    connect_to_database, create_stadium_table, insert_home_stadiums,
    list_stadiums, add_stadium, delete_stadium,
    list_teams, add_team, delete_team,
    list_players, add_player, remove_player,
    list_fixtures, schedule_fixture, cancel_fixture
)

def main():
    print("Welcome to the Game Fixture Manager!")

    # Establish connection to the SQLite database
    conn = connect_to_database("sports.db")
    
    # Ensure the Stadium table is created and populated with predefined data
    create_stadium_table(conn)
    insert_home_stadiums(conn)

    while True:
        print("\nMenu:")
        print("1. List Stadiums")
        print("2. Add Stadium")
        print("3. Delete Stadium")
        print("4. List Teams")
        print("5. Add Team")
        print("6. Delete Team")
        print("7. List Players")
        print("8. Add Player")
        print("9. Remove Player")
        print("10. List Fixtures")
        print("11. Schedule Fixture")
        print("12. Cancel Fixture")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_stadiums(conn)
        elif choice == "2":
            stadium_name = input("Enter the name of the stadium: ")
            location = input("Enter the location of the stadium: ")
            capacity = int(input("Enter the capacity of the stadium: "))
            availability = input("Enter the availability of the stadium: ")
            add_stadium(conn, stadium_name, location, capacity, availability)
        elif choice == "3":
            stadium_id = input("Enter the ID of the stadium to delete: ")
            delete_stadium(conn, stadium_id)
        elif choice == "4":
            list_teams(conn)
        elif choice == "5":
            team_name = input("Enter the name of the team: ")
            add_team(conn, team_name)
        elif choice == "6":
            team_id = input("Enter the ID of the team to delete: ")
            delete_team(conn, team_id)
        elif choice == "7":
            list_players(conn)
        elif choice == "8":
            player_name = input("Enter the name of the player: ")
            position = input("Enter the position of the player: ")
            age = input("Enter  the players age: ")
            team_id = input("Enter the ID of the team: ")
            add_player(conn, player_name, position, team_id)
        elif choice == "9":
            player_id = input("Enter the ID of the player to remove: ")
            remove_player(conn, player_id)
        elif choice == "10":
            list_fixtures(conn)
        elif choice == "11":
            game_date = input("Enter the date of the game (YYYY-MM-DD): ")
            game_time = input("Enter the time of the game (HH:MM): ")
            game_venue = input("Enter the venue of the game: ")
            match_id = input("Enter the match ID: ")
            team1_id = input("Enter the ID of the first team: ")
            team2_id = input("Enter the ID of the second team: ")
            schedule_fixture(conn, game_date, game_time, game_venue, match_id, team1_id, team2_id)
        elif choice == "12":
            match_id = input("Enter the match ID to cancel: ")
            cancel_fixture(conn, match_id)
        elif choice == "0":
            print("Adios!")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection when exiting the program
    conn.close()

if __name__ == "__main__":
    main()
