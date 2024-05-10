from fastapi import APIRouter,Depends, HTTPException
from models.database import get_db
from models.models import ViolationDetails, Student
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import select

router = APIRouter(tags=["Violation Details"])

@router.get("/violationDetailsAll")
def get_violation_details(db: Session = Depends(get_db)):
    violation_details = db.query(ViolationDetails).all()
    return violation_details

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
async def add_violation(
    studentID: int,
    violation: str,
    dateTime: datetime,
    venue: str,
    sanction: str,
    guard: str,
    db: Session = Depends(get_db)):
    try:
        add_violation = ViolationDetails(
            studentID=studentID,
            violation=violation,
            dateTime=dateTime,
            venue=venue,
            sanction=sanction,
            guard=guard
        )
        db.add(add_violation)
        db.commit()
        db.refresh(add_violation)
        return {"data": add_violation}
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))




