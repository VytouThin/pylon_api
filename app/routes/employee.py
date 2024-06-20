from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schema.employee import Employee
from app.schema.employee import EmployeeUpdate
from app.middleware.auth import get_db
from app.controllers import employee_controller

router = APIRouter()

@router.get("/employees", response_model=List[Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = employee_controller.get_all_employees(db)
    return employees

@router.patch("/employees/{manpowerId}", response_model=Employee)
def update_employee(manpowerId: str, employee_update: EmployeeUpdate, db: Session = Depends(get_db)):
    return employee_controller.update_employee_details(db, manpowerId, employee_update)

@router.get("/employees/csv")
def download_employees_csv(db: Session = Depends(get_db)):
    return employee_controller.download_employees_csv(db)
