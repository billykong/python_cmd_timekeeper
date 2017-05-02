import sqlite3
import sys

sqlite_file = 'timekeeper_db.sqlite'
table_name = 'time_log'
id_col = 'id'
subject_col = 'subject'
start_time_col = 'start_time'
end_time_col = 'end_time'
note_col = 'note'

conn = sqlite3.connect(sqlite_file)

def setup_table():
  c = conn.cursor()
  sql = """
    CREATE TABLE IF NOT EXISTS time_log (
      id INTEGER PRIMARY KEY,
      subject TEXT,
      note TEXT,
      start_time TEXT,
      end_time TEXT
    )
  """
  c.execute(sql)
  conn.commit()

def get_all_unended_subjects():
  c = conn.cursor()
  # select rows with start_time != NULL & end_time = NULL  
  c.execute("SELECT * FROM {tn} WHERE {start_col} IS NOT NULL AND {end_col} IS NULL".\
    format(tn=table_name, start_col=start_time_col, end_col=end_time_col))
  return c.fetchall()

def get_all_subjects_of_today():
  c = conn.cursor()
  c.execute("SELECT * FROM {tn} WHERE strftime('%Y-%m-%d', {start_col}) = strftime('%Y-%m-%d', 'now')".\
    format(tn=table_name, start_col=start_time_col))
  return c.fetchall()

def start_subject(subject, note=None):
  c = conn.cursor()
  # TODO: check there is not unended subject
  
  # insert new row with subject
  if note is None:
    c.execute("INSERT INTO {tn} ({i_col}, {sub_col}, {start_col}) VALUES (NULL, \"{sb}\", (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')))".\
      format(tn=table_name, i_col=id_col, sub_col=subject_col, start_col=start_time_col, sb=subject))
  else:
    c.execute("INSERT INTO {tn} ({i_col}, {sub_col}, {start_col}, {nt_col}) VALUES (NULL, \"{sb}\", (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')), \"{nt}\")".\
      format(tn=table_name, i_col=id_col, sub_col=subject_col, start_col=start_time_col, nt_col=note_col, sb=subject, nt=note))
  conn.commit()
  
  # return the row of updated subject
  c.execute("SELECT * FROM {tn} WHERE {sub_col} = \"{sub}\" ORDER BY id DESC LIMIT 1".\
    format(tn=table_name, sub_col=subject_col, sub=subject))
  return c.fetchone()


def end_subject(row_number, note=None):
  c = conn.cursor()
  if note is None:
    c.execute("UPDATE {tn} SET {end_col}=(DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')) WHERE {i_col}={id}".\
      format(tn=table_name, end_col=end_time_col, i_col=id_col, id=row_number))
  else:
    c.execute("UPDATE {tn} SET {end_col}=(DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')), {nt_col}=\"{nt}\" WHERE {i_col}={id}".\
      format(tn=table_name, end_col=end_time_col, nt_col=note_col, nt=note, i_col=id_col, id=row_number))

  conn.commit()
  # return the row of updated subject
  c.execute("SELECT * FROM {tn} WHERE {i_col}={id} ORDER BY id DESC LIMIT 1".\
    format(tn=table_name, i_col=id_col, id=row_number))
  return c.fetchone()


def reset_database():
  c = conn.cursor()
  c.execute("DROP TABLE IF EXISTS {tn}".\
    format(tn=table_name))
  conn.commit()
  setup_table()

def validate_database():
  pass
  # check for missing start_time or end_time




if __name__ == '__main__':
  if len(sys.argv) == 2:
    globals()[sys.argv[1]]()
  elif len(sys.argv) == 3:
    globals()[sys.argv[1]](sys.argv[2])
  elif len(sys.argv) == 4:
    globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
