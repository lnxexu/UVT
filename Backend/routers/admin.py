from fastapi import APIRouter,Depends
from models.database import SessionLocal, get_db
from models.models import Administrator, AdministratorInfo
from sqlalchemy.orm import Session

router = APIRouter(tags=["Admin"])

@router.get("/admin", response_model=list[AdministratorInfo])
def get_administrator(db: Session = Depends(get_db)):
    administrators = db.query(Administrator).all()
    return administrators