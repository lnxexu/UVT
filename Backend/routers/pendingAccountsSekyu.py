from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from models.database import SessionLocal, get_db
from models.models import PendingAccountDetailsSekyu
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter(tags=["Pending_Accounts_Security"])

@router.get("/GetAllAccountsSekyu")
async def get_all_accounts(db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM PendingAccountsSekyu")
    result = db.execute(stmt)
    pending = [row._asdict() for row in result]
    return pending

@router.get("/CountAccountsSekyu")
async def count_accounts(db: Session = Depends(get_db)):
    stmt = text("SELECT COUNT(*) FROM PendingAccountsSekyu")
    result = db.execute(stmt).scalar()
    return result

@router.post("/AddAccountSekyu")
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, address: str, contactInformation: str, birthDate: date, password: str, db: Session = Depends(get_db)):
    user = PendingAccountDetailsSekyu(fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix, address = address, contactInformation = contactInformation, birthDate = birthDate)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/RejectAccountSekyu/{email}")
async def delete_account(email: str, db: Session = Depends(get_db)):
    user = db.query(PendingAccountDetailsSekyu).filter(PendingAccountDetailsSekyu.email == email).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "Account creation request deleted successfully"}
    else:
        return HTTPException(status_code=404, detail="User not found")
    
    