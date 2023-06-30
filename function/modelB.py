from sqlalchemy import Sequence, create_engine,Column,ForeignKey,Double,Integer,DateTime
from sqlalchemy.orm import Session,declarative_base
Base=declarative_base()
class TemperatureB(Base):
    __tablename__="temperatures"
    id=Column(Integer,Sequence("some_id_seq",start=1),primary_key=True)
    createdAt=Column(DateTime,primary_key=True)
    sensor1=Column(Double,nullable=False)
class HumidityB(Base):
    __tablename__="humidities"
    id=Column(Integer,Sequence("some_id_seq",start=1),primary_key=True)
    createdAt=Column(DateTime,primary_key=True)
    sensor1=Column(Double,nullable=False)
class SoilTemperatureB(Base):
    __tablename__="soiltemperatures"
    id=Column(Integer,Sequence("some_id_seq",start=1),primary_key=True)
    createdAt=Column(DateTime,primary_key=True)
    sensor1=Column(Double,nullable=False)
    sensor2=Column(Double,nullable=False)
    sensor3=Column(Double,nullable=False)
    sensor4=Column(Double,nullable=False)
    sensor5=Column(Double,nullable=False)
    sensor6=Column(Double,nullable=False)
    sensor7=Column(Double,nullable=False)
engine = create_engine("postgresql+psycopg2://postgres:keochanny$1@localhost/test_raspberrypib")
Base.metadata.create_all(engine)
dbB=Session(engine)


