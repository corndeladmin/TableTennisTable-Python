import re
from typing import List
from src.invalid_argument_exception import InvalidArgumentException

def create_league():
  return BuildLeague([])

class LeagueRow:
  def __init__(self, maxSize, players=None):
    self.maxSize = maxSize
    self.players = players or []

  def swap (self, playerToRemove, playerToAdd):
    playerRemoveIndex = self.players.index(playerToRemove)
    self.players[playerRemoveIndex]= playerToAdd

  def get_players(self):
    return self.players
    
  def add(self, player):
    self.players.append(player)

  def is_full(self):
    return len(self.players) >= self.maxSize
  
  def inclues(self,player):
    return self.players.includes(player)

class BuildLeague:
  def __init__(self, players: List[str] = None):
    self.rows = [LeagueRow(i+1) for i in range(len(players) // 2)]
    self.added_players = set()
    if players:
      for player in players:
        self.add_player(player)

  def find_player_row_index (self, player):
    for i, row in enumerate(self.rows):
      if player in row.get_players():
        return i
    return -1

  def check_player_is_in_game (self, player):
    if (not self.is_player_in_game(player)):
      raise InvalidArgumentException(f"Player {player} is not in the game")

  def is_player_in_game (self, player):
    return self.find_player_row_index(player) >= 0
  
  def validate_name (self, player):
    pattern= re.compile("/^\w+$/")
    if (pattern.match(player)==False):
      raise InvalidArgumentException(f"Player name {player} contains invalid characters")
    else:  
      return player

  def check_player_is_unique (self, player):
    if self.is_player_in_game(player) or player in self.added_players:
      raise InvalidArgumentException(f"Cannot add player {player} because they are already in the game")
    else:
      return player
    
  def add_player (self, player):
    self.validate_name(player)
    self.check_player_is_unique(player)
    
    if (len(self.rows) == 0 or self.rows[-1].is_full()):
      self.add_row()
    self.rows[-1].add(player)
    self.added_players.add(player)

  def get_players(self):
        return [row.get_players() for row in self.rows]

  def add_row (self):
    new_row = LeagueRow(len(self.rows) + 1)
    self.rows.append(new_row)

  def record_win (self, winner, loser):
    self.check_player_is_in_game(winner)
    self.check_player_is_in_game(loser)

    winner_row_index = self.find_player_row_index(winner)
    loser_row_index = self.find_player_row_index(loser)

    if (winner_row_index - loser_row_index != 1):
      raise InvalidArgumentException(f"Cannot record match result. Winner {winner} must be one row below loser {loser}")

    self.rows[winner_row_index].swap(winner, loser)
    self.rows[loser_row_index ].swap(loser, winner)

  def get_winner (self):
    if (len(self.rows) > 0):
      return self.rows[0].get_players()[0]
    return None
