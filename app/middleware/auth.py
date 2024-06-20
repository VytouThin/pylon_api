import os
from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
# from app.models.employee import SessionLocal
from app.core.connection import SessionLocal

load_dotenv()

security = HTTPBasic()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPBasicCredentials = Security(security)):
    correct_username = os.getenv('USERNAME') 
    correct_password = os.getenv('PASSWORD')
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
