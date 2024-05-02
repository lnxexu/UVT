from fastapi import APIRouter, Depends, HTTPException
from models.database import get_db
from models.models import OSADAccount, OSADAccInfo
from sqlalchemy.orm import Session
from typing import List
from datetime import date

router = APIRouter(tags=["OSAD"])


@router.post("/osadUsers/addUser")
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, address: str, contactInformation: str, birthDate: date, password: str, db: Session = Depends(get_db)):
    user = OSADAccount(fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix, address = address, contactInformation = contactInformation, birthDate = birthDate)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/OSADusers", response_model=List[OSADAccInfo])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(OSADAccount).all()
    return users
    
@router.get("/OSADusers/verify" )
async def verify_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(OSADAccount).filter(OSADAccount.email == email, OSADAccount.password == password).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/OSADusers/searchUser/{email}")
async def search_user(email: str, db: Session = Depends(get_db)):
    user = db.query(OSADAccount).filter(OSADAccount.email == email).first()
    if user:
        return {"fullName": user.fullName}
    else:
        return HTTPException(status_code=404, detail="User not found")
    
# change password
@router.put("/OSADusers/changePassword/{email}")
async def change_password(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(OSADAccount).filter(OSADAccount.email == email).first()
    if user:
        user.password = password
        db.commit()
        return {"message": "Password changed successfully"}
    else:
        return HTTPException(status_code=404, detail="User not found")
    


                       

