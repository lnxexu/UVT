from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from models.database import SessionLocal, get_db
from models.models import PendingViolationDetails, PendingViolationDetailsInfo
from sqlalchemy.orm import Session
from sqlalchemy import text


router = APIRouter(tags=["Pending"])

@router.get("/pending")
def pending(db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM pendingv")
    result = db.execute(stmt)
    pending = [row._asdict() for row in result]
    return pending

@router.get("/pendingCount")
def pending_count(db: Session = Depends(get_db)):
    stmt = text("SELECT COUNT(*) FROM pendingv")
    result = db.execute(stmt).scalar()
    return result


@router.post("/pendingAdd/")
async def send_report(
    name: str,
    section: str,
    studentID: int , 
    violation: str ,
    dateTime: datetime, 
    description: str, 
    guard: str,
    db: Session = Depends(get_db)):
    try:
        send_report = PendingViolationDetails(
            name=name, 
            section=section,
            studentID=studentID,
            violation=violation, 
            dateTime=dateTime,
            description=description,
            guard=guard
            )
        db.add(send_report)
        db.commit()
        db.refresh(send_report)
        return {"data": send_report}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    



@router.delete("/pendingDelete/{pReportID}")
def delete_pending(pReportID: int, db: Session = Depends(get_db)):
    delete = db.query(PendingViolationDetails).filter(PendingViolationDetails.pReportID == pReportID).first()
    if delete:
        db.delete(delete)
        db.commit()
        return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Not found")


@router.put("/pendingUpdate/{pReportID}")
def update_pending(pReportID: int, violation: str, venue: str, sanction: str, status: str, guard: str, db: Session = Depends(get_db)):
    update = db.query(PendingViolationDetails).filter(PendingViolationDetails.pReportID == pReportID).first()
    if update:
        update.violation = violation
        update.venue = venue
        update.sanction = sanction
        update.status = status
        update.guard = guard
        db.commit()
        return {"message": "Updated"}
    print(f"Did not find record with pReportID {pReportID}")
    raise HTTPException(status_code=404, detail="Not found")


    
