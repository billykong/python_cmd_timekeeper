import controller
from tabulate import tabulate
import lang



def display_menu():
  menu = """
    Please choose one of the followings:
      1. Show all unended task
      2. Start a task
      3. End a task 
  """
  print(menu)

def get_menu_input():
  try:
    return int(input("Enter one digit: "))
  except ValueError:
    print(lang.unrecognised)
    get_menu_input()

def process_menu_input(user_input):
  if user_input == 1:
    show_all_unended_tasks()
  elif user_input == 2:
    start_a_task()
  elif user_input == 3:
    end_a_task()
  else:
    print(lang.unavailable)
  

def show_all_unended_tasks():
  unended_subjects = controller.get_all_unended_subjects()
  # (13, 'quoted', 'None', '19:07:25', None)
  print(tabulate(unended_subjects, headers=["id", "subject", "desc", "start-time", "end-time"]))
  return unended_subjects

def start_a_task():
  subject = input("Please enter task subject: ")
  note = input("Please enter task description: ")
  task = controller.start_subject(subject, note)
  print("Task started: ", task)

def end_a_task():
  unended_subjects = show_all_unended_tasks()
  try:
    some_id = int(input("Please choose a task to end: "))
    subject = [x for x in unended_subjects if x[0] == some_id]
    if len(subject) != 1:
      raise ValueError(lang.unavailable)
    note = subject[0][2] + "; "
    note += input("Do you want to append some description: ")
    subject = controller.end_subject(some_id, note)
    print("Task ended: ", subject)
  except ValueError:
    print(lang.unrecognised)
