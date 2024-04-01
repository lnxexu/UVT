from datetime import date, datetime, time, timedelta
import os
from fastapi import FastAPI, Depends
from fastapi.exception_handlers import http_exception_handler
from fastapi.params import Form
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# Database configuration
DB_URL = "mysql+pymysql://kobe:oliviahyejoo@localhost:3306/dbgroup12"

# FastAPI app instance
app = FastAPI()
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 

class Administrator(Base):
    __tablename__ = "administrator"
    adminID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    position = sqlalchemy.Column(sqlalchemy.String)
    contactInformation = sqlalchemy.Column(sqlalchemy.String)

class Exception(Base):
    __tablename__ = "exception"
    exceptionID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    dateStart = sqlalchemy.Column(sqlalchemy.Date)
    dateEnd = sqlalchemy.Column(sqlalchemy.Date)
    studentID = sqlalchemy.Column(sqlalchemy.Integer)

class SchoolRules(Base):
    __tablename__ = "schoolRules"
    ruleID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
    category = sqlalchemy.Column(sqlalchemy.String)
    
class SecurityGuard(Base):
    __tablename__ = "securityGuard"
    guardID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    contactNumber = sqlalchemy.Column(sqlalchemy.Integer)
    shift = sqlalchemy.Column(sqlalchemy.Date)

class Student(Base):
    __tablename__ = "student"
    studentID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    section = sqlalchemy.Column(sqlalchemy.String)
    contactInformation = sqlalchemy.Column(sqlalchemy.String)

class Violation(Base):
    __tablename__ = "violation"
    violationID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
    ruleID = sqlalchemy.Column(sqlalchemy.Integer)
    adminID = sqlalchemy.Column(sqlalchemy.Integer)

class ViolationDetails(Base):
    __tablename__ = "violationDetails"
    reportID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    date = sqlalchemy.Column(sqlalchemy.Date)
    venue = sqlalchemy.Column(sqlalchemy.String)
    time = sqlalchemy.Column(sqlalchemy.DateTime)
    status = sqlalchemy.Column(sqlalchemy.Integer)
    sanctions = sqlalchemy.Column(sqlalchemy.String)
    studentID = sqlalchemy.Column(sqlalchemy.Integer)
    violationID = sqlalchemy.Column(sqlalchemy.Integer)
    guardID = sqlalchemy.Column(sqlalchemy.Integer)

class PendingViolationDetails(Base):
    __tablename__ = "pending"
    pendingReportID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    studentID = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String)
    section = sqlalchemy.Column(sqlalchemy.String)
    violation = sqlalchemy.Column(sqlalchemy.String)
    dateAndTime = sqlalchemy.Column(sqlalchemy.DateTime)
    description = sqlalchemy.Column(sqlalchemy.String)

class OSADAccount(Base):
    __tablename__ = "osadacc"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    username = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)

class SekyuAccount(Base):
    __tablename__ = "sekyuacc"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    username = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)


# Pydantic model for data validation
class AdministratorInfo(BaseModel):
    adminID: int 
    name: str
    position: str
    contactInformation: str

class ExceptionInfo(BaseModel):
    exceptionID: int
    dateStart: str
    dateEnd: str
    studentID: int

class SchoolRulesInfo(BaseModel):
    ruleID: int
    description: str
    category: str

class SecurityGuardInfo(BaseModel):
    guardID: int
    name: str
    contactNumber: str
    shift: int

class StudentInfo(BaseModel):
    studentID: int
    name: str
    section: str
    contactInformation: int

class ViolationInfo(BaseModel):
    violationID: int
    description: str
    ruleID: int
    adminID: int

class ViolationDetailsInfo(BaseModel):
    reportID: int
    date: int
    venue: str
    time: int
    status: str
    sanctions: str
    studentID: int
    violationID: int
    guardID: int

class PendingViolationDetailsInfo(BaseModel):
    name :str
    section :str
    studentID :int
    violation :str
    dateAndTime: datetime 
    description :str

class OSADAccInfo(BaseModel):
    id: int
    username: str
    password: str
    email: str

class SekyuAccInfo(BaseModel):
    id: int
    username: str
    password: str
    email: str
# Dependency function to get database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# GET
@app.get("/admin")
def get_administrator(db: Session = Depends(get_db)):
    admin = db.query(Administrator).all()
    return admin

@app.get("/exception")
def get_exception(db: Session = Depends(get_db)):
    exception = db.query(Exception).all()
    return exception 

@app.get("/schoolRules")
def get_schoolRules(db: Session = Depends(get_db)):
    schoolRules = db.query(SchoolRules).all()
    return schoolRules 

@app.get("/securityGuard")
def get_securityGuard(db: Session = Depends(get_db)):
    securityGuard = db.query(SecurityGuard).all()
    return securityGuard 

@app.get("/student")
def get_student(db: Session = Depends(get_db)):
    student = db.query(Student).all()
    return student

@app.get("/violation")
def get_violation(db: Session = Depends(get_db)):
    violation = db.query(Violation).all()
    return violation

@app.get("/violationDetails")
def get_violationDetails(db: Session = Depends(get_db)):
    vDetails = db.query(ViolationDetails).all()
    return vDetails

@app.get("/OSADusers/", response_model=list)
def read_users(db: Session = Depends(get_db)):
    users = db.query(OSADAccount).all()
    return [{"id": user.id, "username": user.username} for user in users]

@app.get("/sekyuUsers/", response_model=list)
def read_users(db: Session = Depends(get_db)):
    users = db.query(SekyuAccount).all()
    return [{"id": user.id, "username": user.username} for user in users]

@app.get("/OSADusers/{user_id}", response_model=dict)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(OSADAccount).filter(OSADAccount.id == user_id).first()
    if user:
        return {"id": user.id, "username": user.username}
    raise http_exception_handler(status_code=404, detail="User not found")

@app.get("/sekyuUsers/{user_id}", response_model=dict)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(SekyuAccount).filter(SekyuAccount.id == user_id).first()
    if user:
        return {"id": user.id, "username": user.username}
    raise http_exception_handler(status_code=404, detail="User not found")

# POST


@app.post("/osadacc/", response_model=dict)
async def create_user(email: str = Form(...), username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # Hash the password using bcrypt
    hashed_password = password

    try:
        new_user = OSADAccount(email=email, username=username, password=hashed_password)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"id": new_user.id, "username": new_user.username}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@app.post("/pending/", response_model=dict)
async def send_report(
    name: str = Form(...),
    section: str  = Form(...),
    studentID: int  = Form(...), 
    violation: str  = Form(...),
    dateAndTime: datetime  = Form(...), 
    description: str  = Form(...), 
    db: Session = Depends(get_db)):
    try:
        send_report = PendingViolationDetails(
            name=name, 
            section=section,
            studentID=studentID,
            violation=violation, 
            dateAndTime=dateAndTime,
            description=description,
            )

        db.add(send_report)
        db.commit()
        db.refresh(send_report)
        return {"data": send_report}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
# PUT
@app.put("/users/{user_id}", response_model=dict)
async def update_user(
    user_id: int,
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db=Depends(get_db)
):
    # Hash the password using bcrypt
    hashed_password = hash_password(password)

    # Update user information in the database 
    query = "UPDATE users SET email = %s, username = %s, password = %s WHERE id = %s"
    db[0].execute(query, (email, username, hashed_password, user_id))

    # Check if the update was successful
    if db[0].rowcount > 0:
        db[1].commit()
        return {"message": "User updated successfully"}
    
    # If no rows were affected, user not found
    raise http_exception_handler(status_code=404, detail="User not found")


# DELETE
@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(
    user_id: int,
    db=Depends(get_db)
):
    try:
        # Check if the user exists
        query_check_user = "SELECT id FROM users WHERE id = %s"
        db[0].execute(query_check_user, (user_id,))
        existing_user = db[0].fetchone()

        if not existing_user:
            raise http_exception_handler(status_code=404, detail="User not found")

        # Delete the user
        query_delete_user = "DELETE FROM users WHERE id = %s"
        db[0].execute(query_delete_user, (user_id,))
        db[1].commit()

        return {"message": "User deleted successfully"}
    except Exception as e:
        # Handle other exceptions if necessary
        raise http_exception_handler(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        # Close the database cursor
        db[0].close()

# Password hashing function using bcrypt

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all origins (restrict in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)