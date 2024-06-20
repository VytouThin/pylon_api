import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# DATABASE_URL = "mssql+pyodbc://sa:Pa$$w0rd123@localhost/PylonProductionData_ForTesting?driver=ODBC+Driver+17+for+SQL+Server"
DATABASE_URL = f"mssql+pyodbc://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}?driver=ODBC Driver 17 for SQL Server"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
