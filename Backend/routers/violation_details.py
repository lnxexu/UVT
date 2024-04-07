from fastapi import APIRouter,Depends, HTTPException
from models.database import SessionLocal, get_db
from models.models import ViolationDetails, ViolationDetailsInfo
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/violationDetails")
def get_violation_details(db: Session = Depends(get_db)):
    violation_details = db.query(ViolationDetails).all()
    return violation_details

@router.get("/violationDetails/{reportID}", response_model=dict)
def get_specifyViolation(report_id: int, db: Session = Depends(get_db)):
    get_specify = db.query(ViolationDetails).filter(ViolationDetails.reportID == report_id).first()
    if get_specify:
        return {"id": get_specify.reportID, "Violation ID": get_specify.violationID, "date": get_specify.dateTime, "status": get_specify.status, "venue":get_specify.venue}
    raise HTTPException(status_code=404, detail="Violation not found")