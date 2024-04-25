from fastapi import APIRouter, Depends, HTTPException
from models.database import get_db
from models.models import OSADAccount, OSADAccInfo
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=["OSAD"])

# get method to get all the accounts in the database
@router.get("/OSADusers", response_model=List[OSADAccInfo])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(OSADAccount).all()
    return users
    
# get method to verify in the log in page that the account exists using the email and password
@router.get("/OSADusers/verify" )
async def verify_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(OSADAccount).filter(OSADAccount.email == email).first()
    if user:
        if user.password == password:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# post method to create a new account consisting of full name, suffix, gender, age, email, password, and phone number
@router.post("/OSADusersAddAccount")
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, password: str, db: Session = Depends(get_db)):
    user = OSADAccount(fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

                       

