from fastapi import APIRouter, Depends, HTTPException
from models.database import get_db
from models.models import OSADAccount, OSADAccInfo
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=["OSAD"])

@router.get("/OSADusers")
def read_users(db: Session = Depends(get_db)):
    users = db.query(OSADAccount).all()
    return users

@router.get("/OSADusers/{user_id}", response_model=dict)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(OSADAccount).filter(OSADAccount.id == user_id).first()
    if user:
        return {"id": user.id, "name":user.fullname}
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/OSADusers/add", response_model=dict)
async def create_user(fullName: str, email: str, password: str, age: int, suffix: str, gender: str, db: Session = Depends(get_db)):
    # Hash the password using bcrypt
    hashed_password = password

    try:
        new_user = OSADAccount(fullname=fullName, email=email, age=age, suffix=suffix, gender=gender, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"id": new_user.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))