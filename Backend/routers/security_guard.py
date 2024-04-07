from fastapi import APIRouter,Depends
from models.database import SessionLocal, get_db
from models.models import SecurityGuard
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/securityGuard")
def get_security_guard(db: Session = Depends(get_db)):
    security_guards = db.query(SecurityGuard).all()
    return security_guards