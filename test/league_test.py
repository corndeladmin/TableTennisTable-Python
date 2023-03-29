from src.league import create_league

def test_league_add_player():
  league_instance = create_league()
  league_instance.add_player('Bob')

  players = league_instance.get_players()

  assert len(players) == 1
  assert players[0] == ['Bob']