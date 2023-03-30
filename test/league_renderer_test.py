from src.league import create_league
from src.league_renderer import render

def test_league_renderer():
  league_instance = create_league()
  rendered = render(league_instance)
  assert rendered == 'No players yet'
