from fastapi import FastAPI, Depends
from app.routes import employee
from app.middleware.auth import get_current_user

app = FastAPI()

app.include_router(employee.router, prefix="/api/v1", dependencies=[Depends(get_current_user)])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee API"}
