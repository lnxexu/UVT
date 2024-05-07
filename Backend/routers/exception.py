from fastapi import APIRouter, Depends, HTTPException
from models.database import get_db
from models.models import Exception, Student
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["Exception"])

# post for exception reports
@router.post("/exception")
async def add_exception_report(
    studentID: int,
    violation: str,
    dateTime: datetime,
    venue: str,
    sanction: str,
    status: str,
    guard: str,
    db: Session = Depends(get_db)):
    try:
        student = db.query(Student).filter(Student.studentID == studentID).first()
        if not student:
            raise HTTPException(status_code=400, detail="Student not found")
        violation = Exception(
            studentID=studentID,
            violation=violation,
            dateTime=dateTime,
            venue=venue,
            sanction=sanction,
            status=status,
            guard=guard)
        db.add(violation)
        db.commit()
        db.refresh(violation)
        return violation
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Foreign key constraint failed")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
