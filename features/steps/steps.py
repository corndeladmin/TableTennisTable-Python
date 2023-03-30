from behave import given, when, then

from src.app import StartGame
from src.league import create_league

@given('the league has no players')
def step_impl(context):
  context.game = StartGame(create_league())
  pass

@when('I print the league')
def step_impl(context):
  context.response = context.game.send_command('print')

@then('I should see that there are no players')
def step_impl(context):
  assert (context.response =='No players yet')