from fastapi import APIRouter,Depends, HTTPException
from models.database import get_db
from models.models import ViolationDetails, Student
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import select

router = APIRouter(tags=["Violation Details"])



@router.get("/violationDetails")
def get_violation_count(db: Session = Depends(get_db)):
    violation_count = db.query(ViolationDetails.reportID).count()
    return violation_count

@router.get("/violationDetails/{reportID}", response_model=dict)
def get_specifyViolation(report_id: int, db: Session = Depends(get_db)):
    get_specify = db.query(ViolationDetails).filter(ViolationDetails.reportID == report_id).first()
    if get_specify:
        return {"id": get_specify.reportID, "date": get_specify.dateTime, "venue":get_specify.venue}
    raise HTTPException(status_code=404, detail="Violation not found")

@router.get("/violationDetails/student/{studentID}")
def get_violation_details(studentID: int, db: Session = Depends(get_db)):
    violation_details = db.query(ViolationDetails).filter(ViolationDetails.studentID == studentID).all()
    return violation_details

@router.post("/violationDetailsPost/")
async def create_violation_details(
    studentID: int,
    violation: str,
    dateTime: datetime,
    venue: str,
    sanction: str,
    guard: str,
    db: Session = Depends(get_db)):
    try:
        # Check if the student exists in the database
        student = db.query(Student).filter(Student.studentID == studentID).first()
        if not student:
            raise HTTPException(status_code=400, detail="Student not found")
        violation = ViolationDetails(
            studentID=studentID,
            violation=violation,
            dateTime=dateTime,
            venue=venue,
            sanction=sanction,
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




