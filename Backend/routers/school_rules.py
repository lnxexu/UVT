from fastapi import APIRouter,Depends
from models.database import SessionLocal, get_db
from models.models import SchoolRules, SchoolRulesInfo
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/schoolRules", response_model=list[SchoolRulesInfo])
def get_school_rules(db: Session = Depends(get_db)):
    school_rules = db.query(SchoolRules).all()
    return school_rules