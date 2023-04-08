#import sqlite3
#from collections import namedtuple
from students import Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
# conn = sqlite3.connect('itstep.db')
# curs = conn.cursor()

#create
#curs.execute('CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(20), age INT, avg_grade FLOAT)')

#insert
# curs.execute('INSERT INTO students VALUES(1, "Eva", 15, 12)')
# curs.execute('INSERT INTO students VALUES(2, "Uliana", 15, 12)')
# curs.execute('INSERT INTO students VALUES(3, "Bogdan", 14, 12)')
# curs.execute('INSERT INTO students VALUES(4, "Mark", 14, 12)')
# curs.execute('INSERT INTO students VALUES(5, "Boris", 15, 12)')
# curs.execute('INSERT INTO students VALUES(6, "Lev", 14, 12)')
# curs.execute('INSERT INTO students VALUES(7, "Magomed-Saleh", 13, 10)')
# curs.execute('INSERT INTO students VALUES(7, "Magomed-Emin", 14, 12)')
# conn.commit()


#select 1
'''
fields = ["id", "name", "age", "avg_grade"]
student = namedtuple('Student', fields)
curs.execute('SELECT * FROM students')
conn.commit()
# rows = curs.fetchall()
# print(rows)
# print(type(rows))#list
# print(type(rows[0]))#tuple
students = []
for row in curs.fetchall():
    students.append(student(*row))
print(students)
curs.close()
conn.close()
'''
#select 2
#create object for connect to database
engine = create_engine('sqlite:///itstep.db', echo=True)
#create session for work with database
Session = sessionmaker(bind=engine)
session = Session()
students = session.query(Student).all()
for st in students:
    print(f'Id={st.id}\t'
          f'Name={st.name}\t'
          f'Age={st.age}\t'
          f'Avg Grage={st.avg_grade}\n')
# df = pd.DataFrame.from_records([data.__dict__ for data in students])
# print(df)
session.close()
