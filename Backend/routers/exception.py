from fastapi import APIRouter,Depends
from models.database import SessionLocal, get_db
from models.models import Exception, ExceptionInfo
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/exception", response_model=list[ExceptionInfo])
def get_exception(db: Session = Depends(get_db)):
    exceptions = db.query(Exception).all()
    return exceptions