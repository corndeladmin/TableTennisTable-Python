import json
from src.invalid_argument_exception import InvalidArgumentException

def save(path, league):
  players = league.get_players()
  try:
    json_object = json.dumps(players)
    with open(path, "w") as f:
      f.write(json_object)
  except FileNotFoundError:
    raise InvalidArgumentException(f"Could not save file to {path}")
  except:
    raise InvalidArgumentException('Error saving file')

def load(path, league):
  try:
    with open(path, 'r') as file:
        players = json.load(file)
    validate(players)
    for i in range(len(players)):
      league.add_player(players[i][0])
  except json.JSONDecodeError:
    raise InvalidArgumentException(f"File is not valid JSON: {path}")
  except FileNotFoundError:
    raise InvalidArgumentException(f"Could not load file from {path}")
  except: 
    raise InvalidArgumentException(f"Error loading file")

def validate(game_state):
  bottom_row_index = len(game_state) - 1
  for index, row in enumerate(game_state):
    max_length = index + 1
    if index == bottom_row_index:
        row_has_correct_length = len(row) <= max_length
    else:
        row_has_correct_length = len(row) == max_length

    if not row_has_correct_length:
        raise InvalidArgumentException('Invalid game state')
