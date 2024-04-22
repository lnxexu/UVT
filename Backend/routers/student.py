from fastapi import APIRouter,Depends,HTTPException
from models.database import SessionLocal, get_db
from models.models import Student, StudentInfo
from sqlalchemy.orm import Session

router = APIRouter(tags=["Student"])

@router.get("/student", response_model=list[StudentInfo])
def get_student(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students

@router.get("/student/{student_id}", response_model=StudentInfo)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.studentID == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student