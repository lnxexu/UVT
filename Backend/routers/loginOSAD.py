from fastapi import APIRouter, Depends, HTTPException
from models.database import get_db
from models.models import LoginOSAD, OSADAccount
from sqlalchemy.orm import Session
from datetime import datetime

router = APIRouter(tags=["LoginOSAD"])


@router.get("/loginOSAD")
async def get_latest_login(db: Session = Depends(get_db)):
    user = db.query(LoginOSAD).order_by(LoginOSAD.timestampLogin.desc()).first()
    return user

@router.post("/loginOSAD")
async def add_login(email: str, fullName: str, timestampLogin : datetime, db: Session = Depends(get_db)):
    name = OSADAccount.fullName = fullName
    user = LoginOSAD(timestampLogin = timestampLogin, email = email, fullName = name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
