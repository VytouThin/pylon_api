from sqlalchemy.orm import Session
from app.repository.employee import get_all_employees, update_employee
from app.schema.employee import EmployeeUpdate

def fetch_all_employees(db: Session):
    return get_all_employees(db)

def modify_employee(db: Session, manpowerId: str, employee_update: EmployeeUpdate):
    return update_employee(db, manpowerId, employee_update)
