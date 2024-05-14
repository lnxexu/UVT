from fastapi import APIRouter,Depends, HTTPException
from models.database import get_db
from models.models import Violation
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

router = APIRouter(tags=["Violation"])


@router.post("/violation")
async def add_violation(
    violationName: str,
    description: str,
    category: str,
    dateCreated: datetime,
    createdBy: str,
    db: Session = Depends(get_db)):
    try:
        violation = Violation(
            violationName=violationName,
            description=description,
            category=category,
            dateCreated=dateCreated,
            createdBy=createdBy)
        db.add(violation)
        db.commit()
        db.refresh(violation)
        return violation
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Foreign key constraint failed")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/violation")
async def get_violations(db: Session = Depends(get_db)):
    return db.query(Violation).all()



