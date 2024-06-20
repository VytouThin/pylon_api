from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeBase(BaseModel):
    nric4Digit: str
    name: str
    manpowerId: str
    designation: str
    project: str
    team: str
    supervisor: str
    joinDate: date
    resignDate: Optional[date] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    nric4Digit: Optional[str] = None
    name: Optional[str] = None
    manpowerId: Optional[str] = None
    designation: Optional[str] = None
    project: Optional[str] = None
    team: Optional[str] = None
    supervisor: Optional[str] = None
    joinDate: Optional[date] = None
    resignDate: Optional[date] = None

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
