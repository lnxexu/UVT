from fastapi import APIRouter, Depends, HTTPException  # Added import statement
from models.database import SessionLocal, get_db
from models.models import SekyuAccount
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/sekyuUsers")
def read_users(db: Session = Depends(get_db)):
    users = db.query(SekyuAccount).all()
    return users

@router.get("/sekyuUsers/{user_id}", response_model=dict)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(SekyuAccount).filter(SekyuAccount.id == user_id).first()
    if user:
        return {"id": user.id, "username": user.username}
    raise HTTPException(status_code=404, detail="User not found")