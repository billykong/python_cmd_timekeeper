import database
import sys

def get_all_started_subjects():
  all_subjects = database.get_all_started_subjects()
  print(all_subjects)

def start_subject(subject, note):
  subject = database.start_subject(subject, note)
  print(subject)
  

def end_subject(subject, note):
  subject = database.end_subject(subject, note)
  print(subject)




if __name__ == '__main__':
  if len(sys.argv) == 2:
    globals()[sys.argv[1]]()
  elif len(sys.argv) == 3:
    globals()[sys.argv[1]](sys.argv[2])
  elif len(sys.argv) == 4:
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])

