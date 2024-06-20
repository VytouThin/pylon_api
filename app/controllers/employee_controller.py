from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.employee import fetch_all_employees, modify_employee
from app.schema.employee import EmployeeUpdate
from fastapi.responses import StreamingResponse
import pandas as pd
import io

def get_all_employees(db: Session):
    employees = fetch_all_employees(db)
    return employees

def update_employee_details(db: Session, manpowerId: str, employee_update: EmployeeUpdate):
    db_employee = modify_employee(db, manpowerId, employee_update)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

def download_employees_csv(db: Session):
    employees = fetch_all_employees(db)
    if not employees:
        raise HTTPException(status_code=404, detail="No employees found")
    
    # Convert to DataFrame
    df = pd.DataFrame([{
        'id': e.id,
        'nric4Digit': e.nric4Digit,
        'name': e.name,
        'manpowerId': e.manpowerId,
        'designation': e.designation,
        'project': e.project,
        'team': e.team,
        'supervisor': e.supervisor,
        'joinDate': e.joinDate,
        'resignDate': e.resignDate
    } for e in employees])
    
    # Save DataFrame to CSV
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]),
                                 media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=employees.csv"
    return response
