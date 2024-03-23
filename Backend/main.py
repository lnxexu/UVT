import os
from fastapi import FastAPI, Depends
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
    dateStart = sqlalchemy.Column(sqlalchemy.String)
    dateEnd = sqlalchemy.Column(sqlalchemy.String)
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



# Pydantic model for data validation
class ProductIn(BaseModel):
    adminID: int 
    name: str
    position: str
    contactInformation: str


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

@app.get("/violationDetails")
def get_violationDetails(db: Session = Depends(get_db)):
    vDetails = db.query(ViolationDetails).all()
    return vDetails


@app.post("/addproduct")
def add_product(product: ProductIn, db: Session = Depends(get_db)):
    new_product = Product(
        ProductID=product.ProductID,
        ProductName=product.ProductName,
        Category=product.Category,
        Description=product.Description,
        UnitPrice=product.UnitPrice,
        StockQuantity=product.StockQuantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)  
    return {"message": "Product added successfully"}  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all origins (restrict in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)