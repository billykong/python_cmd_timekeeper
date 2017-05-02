import database
import sys

def get_all_unended_subjects():
  unended_subjects = database.get_all_unended_subjects()
  return unended_subjects

def get_all_subjects_of_today():
  today_subjects = database.get_all_subjects_of_today()
  return today_subjects

def start_subject(subject, note=None):
  subject = database.start_subject(subject, note)
  return subject
  
def end_subject(id, note=None):
  subject = database.end_subject(id, note)
  return subject




if __name__ == '__main__':
  if len(sys.argv) == 2:
    globals()[sys.argv[1]]()
  elif len(sys.argv) == 3:
    globals()[sys.argv[1]](sys.argv[2])
  elif len(sys.argv) == 4:
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3]) #function taking two arguements

