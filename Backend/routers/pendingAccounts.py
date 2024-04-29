from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from models.database import SessionLocal, get_db
from models.models import PendingAccountDetails, PendingAccountDetailsInfo
from sqlalchemy.orm import Session

router = APIRouter(tags=["Pending_Accounts"])

@router.post("/AddAccount")
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, address: str, contactInformation: str,  password: str, db: Session = Depends(get_db)):
    user = PendingAccountDetails(fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix, address = address, contactInformation = contactInformation)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/GetAllAccounts")
async def get_all_accounts(db: Session = Depends(get_db)):
    return db.query(PendingAccountDetails).all()
    