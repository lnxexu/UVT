from fastapi import APIRouter,Depends,HTTPException
from models.database import SessionLocal, get_db
from models.models import Student, StudentInfo
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/student", response_model=list[StudentInfo])
def get_student(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students