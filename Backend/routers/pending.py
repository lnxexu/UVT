from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from models.database import SessionLocal, get_db
from models.models import PendingViolationDetails, PendingViolationDetailsInfo
from sqlalchemy.orm import Session

router = APIRouter(tags=["Pending"])


@router.get("/pending")
def pending(db: Session = Depends(get_db)):
    school_rules = db.query(PendingViolationDetails).all()
    return school_rules

@router.post("/pendingAdd/")
async def send_report(
    name: str,
    section: str,
    studentID: int , 
    violation: str ,
    dateTime: datetime, 
    description: str, 
    db: Session = Depends(get_db)):
    try:
        send_report = PendingViolationDetails(
            name=name, 
            section=section,
            studentID=studentID,
            violation=violation, 
            dateTime=dateTime,
            description=description,
            )
        db.add(send_report)
        db.commit()
        db.refresh(send_report)
        return {"data": send_report}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/pendingCount")
def pending_count(db: Session = Depends(get_db)):
    count = db.query(PendingViolationDetails).count()
    return count


@router.delete("/pendingDelete/{pReportID}")
def delete_pending(pReportID: int, db: Session = Depends(get_db)):
    delete = db.query(PendingViolationDetails).filter(PendingViolationDetails.pReportID == pReportID).first()
    if delete:
        db.delete(delete)
        db.commit()
        return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Not found")

    
