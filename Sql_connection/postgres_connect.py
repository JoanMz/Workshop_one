from decouple import config
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(f"postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}/{config("DB_DATABASE")}")
base = declarative_base()

class precleaned_table(base):
    __tablename__ = config("DB_TABLE1")
    id = Column(Integer(), primary_key=True)
    First_name = Column(String(30))
    Last_name = Column(String(30))
    Email = Column(String(50))
    Application_date = Column(DateTime())
    Country = Column(String(50))
    YOE = Column(Integer())
    Seniority = Column(String(30))
    Code_challenge_score = Column(Integer())
    Technical_Interview_Score = Column(Integer())

    def __str__(self):
        return self.username

class hires_table(base):
    __tablename__= config("DB_TABLE2")
    id = Column(Integer(), primary_key=True)
    First_name = Column(String(30))
    Last_name = Column(String(30))
    Email = Column(String(50))
    Application_date = Column(DateTime())
    Country = Column(String(50))
    YOE = Column(Integer())
    Seniority = Column(String(30))
    Code_challenge_score = Column(Integer())
    Technical_Interview_Score = Column(Integer())
    Hired = Column(Integer())

    def __str__(self):
        return self.username


Session = sessionmaker(engine)
session = Session()

def connection(engine=engine):
    return engine


if __name__ == "__main__":
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
