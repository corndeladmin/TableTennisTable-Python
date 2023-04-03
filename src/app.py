from src.file_service import save, load
from src.league import BuildLeague
import src.league_renderer
import re
from src.invalid_argument_exception import InvalidArgumentException

class StartGame:
  def __init__(self, initial_league):
    self.league = initial_league

  def record_win(self,command):
    regex = r"record win (\w*) (\w*)"
    match = re.search(regex, command)
    winner = match.group(1)
    loser = match.group(2)

    BuildLeague.record_win(self.league, winner, loser)

  def save_game (self, command):
    regex = r"save (.*)" 
    filename = re.search(regex, command)[1]
    save(filename, self.league)

  def load_game (self, command):
    regex = r"load (.*)"
    filename = re.search(regex, command)[1]
    load(filename, self.league)

  def send_command(self, command):
    try:
      if (command.startswith('add player')):
        self.league.add_player(command[11:])
      elif (command.startswith('record win')):
        self.record_win(command)
      elif (command == 'print'):
        return src.league_renderer.render(self.league)
      elif (command == 'winner'):
        return self.league.get_winner()
      elif (command.startswith('save')):
        self.save_game(command)
      elif (command.startswith('load')):
        self.load_game(command)
      else:
        return f'Unknown command {command}'
    except InvalidArgumentException as e:
      return e.message
    except:
      raise 'An error has occured'
