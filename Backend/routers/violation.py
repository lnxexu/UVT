from fastapi import APIRouter, Depends
from models.database import SessionLocal, get_db
from models.models import Violation, ViolationInfo
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/violation", response_model=list[ViolationInfo])
def get_violation(db: Session = Depends(get_db)):
    violations = db.query(Violation).all()
    return violations