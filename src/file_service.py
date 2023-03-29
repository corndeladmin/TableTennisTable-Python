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

def validate(gameState):
  bottomRowIndex = len(gameState) - 1
  for index, row in enumerate(gameState):
    maxLength = index + 1
    if index == bottomRowIndex:
        rowHasCorrectLength = len(row) <= maxLength
    else:
        rowHasCorrectLength = len(row) == maxLength

    if not rowHasCorrectLength:
        raise InvalidArgumentException('Invalid game state')
