from src.league import create_league
from src.app import StartGame

def test_app_prints_empty_game_state():
  game = StartGame(create_league())
  assert game.send_command('print') == 'No players yet'
