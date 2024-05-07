from fastapi import APIRouter, Depends, HTTPException
from models.database import get_db
from models.models import LoginSekyu, SekyuAccount
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import text

router = APIRouter(tags=["LoginSekyu"])


@router.get("/loginSekyu")
async def get_latest_login(db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM LoginSekyu ORDER BY timestampLogin DESC LIMIT 1")
    result = db.execute(stmt)
    user = result.fetchone()
    return dict(user._mapping) if user else None

# get method for getting username by searching email from other data

@router.post("/loginSekyu")
async def add_login(email: str, fullName: str, timestampLogin : datetime, db: Session = Depends(get_db)):
    name = SekyuAccount.fullName = fullName
    user = LoginSekyu(timestampLogin = timestampLogin, email = email, fullName = name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
