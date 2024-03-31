from datetime import date, datetime, time, timedelta
import os
from fastapi import FastAPI, Depends
from sqlalchemy import VARCHAR, create_engine
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
    studentID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    section = sqlalchemy.Column(sqlalchemy.String)
    violation = sqlalchemy.Column(sqlalchemy.String)
    dateAndTime = sqlalchemy.Column(sqlalchemy.DateTime)
    description = sqlalchemy.Column(sqlalchemy.String)


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
    dateAndTime: datetime = None
    description :str

# Dependency function to get database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


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




@app.post("/addViolation")
def add_violation(violations: ViolationDetailsInfo, db: Session = Depends(get_db)):
    new_violation = ViolationDetailsInfo(
        name = violations.name,
        section = violations.section,
        studentID = violations.studentID,
        violation = violations.violation,
        dateAndTime = violations.dateAndTime,
        description = violations.description
    )
    db.add(new_violation)
    db.commit()
    db.refresh(new_violation)  
    return {"message": "violation added successfully"}  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all origins (restrict in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)