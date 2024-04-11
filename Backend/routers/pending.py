from datetime import datetime
from fastapi import APIRouter,Depends,HTTPException
from models.database import SessionLocal, get_db
from models.models import PendingViolationDetails, PendingViolationDetailsInfo
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/pending")
def pending(db: Session = Depends(get_db)):
    school_rules = db.query(PendingViolationDetails).all()
    return school_rules

@router.post("/pendingAdd/", response_model=list[PendingViolationDetailsInfo])
async def send_report(
    name: str,
    section: str ,
    studentID: int  , 
    violation: str ,
    dateAndTime: datetime , 
    description: str  , 
    db: Session = Depends(get_db)):
    try:
        send_report = PendingViolationDetails(
            name=name, 
            section=section,
            studentID=studentID,
            violation=violation, 
            dateAndTime=dateAndTime,
            description=description,
            )

        db.add(send_report)
        db.commit()
        db.refresh(send_report)
        return {"data": send_report}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
