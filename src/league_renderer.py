max_name_length = 17
box_width = max_name_length + 2
boundary = '-' * box_width
empty_name = f"|{' ' * max_name_length}|"

def render(league):
  rows = league.get_players()
  row_count = len(rows)

  if row_count > 0:
    boxes = [render_box(players, row_index, row_count) for row_index, players in enumerate(rows)]
    return "\n".join(boxes)
  else:
    return "No players yet"

def render_box(players, row_index, row_count):
  max_players_in_row = row_index + 1
  row_boundary = " ".join([boundary] * max_players_in_row)

  formatted_names = [f"|{format_name(player)}|" for player in players]
  rows_remaining = row_count - (row_index + 1)
  padding_length = rows_remaining * (box_width // 2)
  padding = " " * padding_length

  empty_name_count = max_players_in_row - len(players)
  empty_names = [empty_name] * empty_name_count

  all_names = formatted_names + empty_names

  return f"{padding}{row_boundary}\n{padding}{' '.join(all_names)}\n{padding}{row_boundary}"

def format_name(name):
  name_length = len(name)

  if name_length <= max_name_length:
    pre_pad_spaces = (max_name_length - name_length) // 2
    post_pad_spaces = (max_name_length - name_length + 1) // 2
    return f"{' ' * pre_pad_spaces}{name}{' ' * post_pad_spaces}"
  else:
    return f"{name[:max_name_length-3]}..."
