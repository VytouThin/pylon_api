from sqlalchemy import Column, Integer, String, Date, inspect
from app.core.connection import Base, engine
# from app.core.config import DATABASE_URL
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine

# DATABASE_URL='mssql+pyodbc://sa:Pa$$w0rd123@localhost/PylonProductionData_ForTesting?driver=ODBC Driver 17 for SQL Server'

# engine = create_engine(DATABASE_URL)
# metadata = MetaData()
# Base = declarative_base(metadata=metadata)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Employee(Base):
    __tablename__ = 'SampleManpowerList'

    id = Column(Integer, primary_key=True, index=True)
    nric4Digit = Column(String(50))
    name = Column(String(50))
    manpowerId = Column(String(50))
    designation = Column(String(50))
    project = Column(String(50))
    team = Column(String(50))
    supervisor = Column(String(50))
    joinDate = Column(Date)
    resignDate = Column(Date, nullable=True)


def create_tables_if_not_exist():
    inspector = inspect(engine)
    if not inspector.has_table("SampleManpowerList", schema="test"):
        Employee.metadata.create_all(bind=engine)

create_tables_if_not_exist()