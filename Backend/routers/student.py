from fastapi import APIRouter,Depends,HTTPException
from models.database import SessionLocal, get_db
from models.models import Student
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter(tags=["Student"])

@router.get("/student")
def get_all_student(db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM student")
    result =  db.execute(stmt)
    users = [row._asdict() for row in result]
    return users

@router.get("/student/{student_id}")
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM Student WHERE studentID = :student_id LIMIT 1")
    result = db.execute(stmt, {'student_id': student_id})
    student = result.fetchone()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return dict(student._mapping) if student else None