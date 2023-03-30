from src.app import StartGame
from src.league import create_league

def main():
  league = create_league()
  game = StartGame(league)
  print("""Welcome to the table tennis table
    =================================
  Commands:
  - add player <name>
    Example:
      add player Alice

  - record win <winner> <loser>
    Example:
      record win Alice Bob

  - print
      Prints the current league

  - winner
      Prints the name of the player at the top of the league

  - save <filepath>
      Save the current league to a JSON file
    Examples:
      save my_league.json
      save ~/some/directory/my_league.json

  - load <filepath>
      Load a saved league from a JSON file
    Examples:
      load my_league.json
      load ~/some/directory/my_league.json

  - quit
  """)
  is_game_active = True

  while (is_game_active):
    command = input()

    if (command == 'quit'):
      is_game_active = False
    else:
      response = game.send_command(command)
      if (response):
        print(response)
