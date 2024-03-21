from sqlalchemy import create_engine, text
import os

engine = create_engine(os.environ['DB_CONNECTION_STRING'])


def load_students_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Mystudents"))
    projects = []
    for row in result.all():
      projects.append(dict(row._mapping))
  return projects


def load_student_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from Mystudents where id = {id}"))
    rows = result.all()
    return dict(rows[0]._mapping)


def add_message_to_db(data):
  with engine.connect() as conn:
    sql = text(
        f"INSERT INTO mymessages (full_name, email, message) VALUES (\'{data['full_name']}\', \'{data['email']}\', \'{data['message']}\')"
    )
    print(sql)
    conn.execute(sql)
    conn.commit()
