from fastapi import APIRouter, Depends, HTTPException
from models.database import SessionLocal, get_db
from models.models import Violation, ViolationInfo
from sqlalchemy.orm import Session

router = APIRouter(tags=["Violation"])

@router.get("/violation", response_model=list[ViolationInfo])
def get_violation(db: Session = Depends(get_db)):
    violations = db.query(Violation).all()
    return violations



@router.post("/violationAdd/")
async def add_violation(
    description: str,
    ruleID: int,
    adminID: int,
    db: Session = Depends(get_db)):
    try:
        add_violation = Violation(
            description=description,
            ruleID=ruleID,
            adminID=adminID,
        )
        db.add(add_violation)
        db.commit()
        db.refresh(add_violation)
        return {"data": add_violation}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
