from fastapi import APIRouter, Depends, HTTPException  
from models.database import SessionLocal, get_db
from models.models import SekyuAccount
from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import text

router = APIRouter(tags=["Security Guard"])  

@router.get("/sekyuUsers")
def read_users(db: Session = Depends(get_db)):
    result = db.execute(text("select fullname, suffix, age, gender, contactInformation, address, birthDate, assignedLoc from sekyuacc"))
    users = [{column: value for column, value in zip(result.keys(), row)} for row in result.fetchall()]
    return users

# Get guards names form dropdown
@router.get("/sekyuUsers/guards")
def get_guards(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT fullName FROM sekyuacc"))
    guards = [row[0] for row in result.fetchall()]
    return guards

@router.get("/sekyuUsers/verify")
def verify_user(email: str, password: str, db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM sekyuacc WHERE email = :email AND password = :password")
    result = db.execute(stmt, {"email": email, "password": password})
    user = result.fetchone()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(user._mapping)

@router.get("/sekyuUsers/searchUser/{email}")
def search_user(email: str, db: Session = Depends(get_db)):
    stmt = text("SELECT * FROM sekyuacc WHERE email = :email")
    result = db.execute(stmt, {"email": email})
    user = result.fetchone()
    if user:
        return {"fullName": user._mapping['fullName']}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    

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
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, address: str, contactInformation: str, birthDate: date, password: str, assignedLoc: str, db: Session = Depends(get_db)):
    user = SekyuAccount(fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix, address = address, contactInformation = contactInformation, birthDate = birthDate, assignedLoc = assignedLoc)
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
    
# get only the assignedLoc column in the sekyuacc table by thier fullName
@router.get("/sekyuUsers/assignedLoc/{fullName}")
def get_assignedLoc(fullName: str, db: Session = Depends(get_db)):
    stmt = text("SELECT assignedLoc FROM sekyuacc WHERE fullName = :fullName")
    result = db.execute(stmt, {"fullName": fullName})
    assignedLoc = result.fetchone()
    if assignedLoc:
        return {"assignedLoc": assignedLoc[0]}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    


    











