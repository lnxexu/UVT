from fastapi import APIRouter, Depends, HTTPException
from models.database import get_db
from models.models import OSADAccount, OSADAccInfo
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from sqlalchemy import text


router = APIRouter(tags=["OSAD"])

@router.get("/OSADusers")
def get_all_users(db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM osadacc")
    result =  db.execute(stmt)
    users = [row._asdict() for row in result]
    return users

@router.get("/OSADusers/verify")
def verify_user(email: str, password: str, db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM osadacc WHERE email = :email AND password = :password")
    result = db.execute(stmt, {"email": email, "password": password})
    user = result.fetchone()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(user._mapping)

@router.get("/OSADusers/searchUser/{email}")
def search_user(email: str, db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM osadacc WHERE email = :email")
    result = db.execute(stmt, {"email": email})
    user = result.fetchone()
    if user:
        return {"fullName": user._mapping['fullName']}
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/osadUsers/addUser")
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, address: str, contactInformation: str, birthDate: date, password: str, db: Session = Depends(get_db)):
    user = OSADAccount(fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix, address = address, contactInformation = contactInformation, birthDate = birthDate)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# change password that requires new password and confirm password
@router.put("/OSADusers/changePassword/{email}")
async def change_password(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(OSADAccount).filter(OSADAccount.email == email).first()
    if user:
        user.password = password
        db.commit()
        return {"message": "Password changed successfully"}
    else:
        return HTTPException(status_code=404, detail="User not found")
    

    


                       

