from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schema.employee import EmployeeUpdate

def get_all_employees(db: Session):
    return db.query(Employee).all()

def update_employee(db: Session, manpowerId: str, employee_update: EmployeeUpdate):
    employee = db.query(Employee).filter(Employee.manpowerId == manpowerId).first()
    if employee:
        for key, value in employee_update.dict(exclude_unset=True).items():
            setattr(employee, key, value)
        db.commit()
        db.refresh(employee)
    return employee
