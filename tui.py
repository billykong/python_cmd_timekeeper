import sys
import database
import tui_helper as helper
  
def setup():
  database.setup_table()

def start():
  setup()
  go_on = True
  while go_on:
    try:
      helper.display_menu()
      user_input = helper.get_menu_input()
      helper.process_menu_input(user_input)
    except KeyboardInterrupt:
      y = input("Are you sure to quit [y/n]?: ")
      if y == "y":
        go_on = False



if __name__ == '__main__':
  if len(sys.argv) == 2:
    globals()[sys.argv[1]]()