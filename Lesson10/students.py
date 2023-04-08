from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INT, FLOAT, VARCHAR
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(20))
    age = Column(INT)
    avg_grade = Column(FLOAT)