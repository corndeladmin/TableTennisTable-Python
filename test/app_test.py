import src.league
import src.league_renderer
import src.app

def test_app_command_processing(mocker):
  mocker.patch("src.league_renderer.render", return_value = 'rendered league')
  league = src.league.create_league()
  game = src.app.startGame(league)
  assert game.send_command('print') == 'rendered league'