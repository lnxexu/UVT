from fastapi import APIRouter, Depends, HTTPException  
from models.database import SessionLocal, get_db
from models.models import SekyuAccount
from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import text

router = APIRouter(tags=["Security Guard"])  

@router.get("/sekyuUsers")
def read_users(db: Session = Depends(get_db)):
    result = db.execute(text("select fullname, suffix, age, gender, contactInformation, address, birthDate from sekyuacc"))
    users = [{column: value for column, value in zip(result.keys(), row)} for row in result.fetchall()]
    return users

@router.get("/sekyuUsers/verify")
async def verify_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(SekyuAccount).filter(SekyuAccount.email == email, SekyuAccount.password == password).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/sekyuUsers/searchUser/{email}")
async def search_user(email: str, db: Session = Depends(get_db)):
    user = db.query(SekyuAccount).filter(SekyuAccount.email == email).first()
    if user:
        return {"fullName": user.fullName}
    else:
        return HTTPException(status_code=404, detail="User not found")
    

@router.put("/sekyuUsers/changePassword/{email}")
async def change_password(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(SekyuAccount).filter(SekyuAccount.email == email).first()
    if user:
        user.password = password
        db.commit()
        return {"message": "Password changed successfully"}
    else:
        return HTTPException(status_code=404, detail="User not found")

@router.post("/sekyuUsers/addUser")
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, address: str, contactInformation: str, birthDate: date, password: str, db: Session = Depends(get_db)):
    user = SekyuAccount(fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix, address = address, contactInformation = contactInformation, birthDate = birthDate)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/sekyuUsers/deleteUser/{email}")
async def delete_user(email: str, db: Session = Depends(get_db)):
    user = db.query(SekyuAccount).filter(SekyuAccount.email == email).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    else:
        return HTTPException(status_code=404, detail="User not found")
    










