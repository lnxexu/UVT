from fastapi import APIRouter, Depends, HTTPException  
from models.database import SessionLocal, get_db
from models.models import SekyuAccount
from sqlalchemy.orm import Session

router = APIRouter(tags=["Security Guard"])  

@router.get("/sekyuUsers")
def read_users(db: Session = Depends(get_db)):
    users = db.query(SekyuAccount).all()
    return users

# get method to verify in the log in page that the account exists using the email and password
# email has to have "@" 
@router.get("/sekyuUsers/verify")
async def verify_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(SekyuAccount).filter(SekyuAccount.email == email).first()
    if user:
        if user.password == password:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# post method to create a new account consisting of full name, suffix, gender, age, email, password, and phone number
@router.post("/sekyuUsersAddAccount")
async def add_account(fullName: str, email: str, gender: str, age:int, suffix: str, password: str, db: Session = Depends(get_db)):
    user = SekyuAccount (fullName = fullName,email=email, password = password, gender = gender, age = age, suffix = suffix)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user






