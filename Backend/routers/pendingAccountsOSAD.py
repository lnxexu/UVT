from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from models.database import SessionLocal, get_db
from models.models import PendingAccountDetailsOSAD
from sqlalchemy.orm import Session

router = APIRouter(tags=["Pending_Accounts_OSAD"])

@router.post("/AddAccountOSAD")
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, address: str, contactInformation: str, birthDate: date, password: str, db: Session = Depends(get_db)):
    user = PendingAccountDetailsOSAD(fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix, address = address, contactInformation = contactInformation, birthDate = birthDate)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/GetAllAccountsOSAD")
async def get_all_accounts(db: Session = Depends(get_db)):
    return db.query(PendingAccountDetailsOSAD).all()

@router.delete("/RejectAccountSekyu/{email}")
async def delete_account(email: str, db: Session = Depends(get_db)):
    user = db.query(PendingAccountDetailsOSAD).filter(PendingAccountDetailsOSAD.email == email).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "Account creation request deleted successfully"}
    else:
        return HTTPException(status_code=404, detail="User not found")
    
    