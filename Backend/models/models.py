from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Administrator(Base):
    __tablename__ = "administrator"
    adminID = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    position = Column(String)
    contactInformation = Column(String)

class Exception(Base):
    __tablename__ = "exception"
    exceptionID = Column(Integer, primary_key=True, index=True)
    dateStart = Column(Date)
    dateEnd = Column(Date)
    studentID = Column(Integer)

class SchoolRules(Base):
    __tablename__ = "schoolRules"
    ruleID = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    category = Column(String)

class SecurityGuard(Base):
    __tablename__ = "securityGuard"
    guardID = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contactNumber = Column(Integer)
    age = Column(Integer)

class Student(Base):
    __tablename__ = "student"
    studentID = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    section = Column(String)
    contactInformation = Column(String)

class Violation(Base):
    __tablename__ = "violation"
    violationID = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    ruleID = Column(Integer)
    adminID = Column(Integer)

class ViolationDetails(Base):
    __tablename__ = "violationdetails"
    reportID = Column(Integer, primary_key=True, index=True)
    dateTime = Column(DateTime)
    venue = Column(String)
    status = Column(Integer)
    sanction = Column(String)
    studentID = Column(Integer)
    violation = Column(String)
    guard = Column(String)

class PendingViolationDetails(Base):
    __tablename__ = "pending"
    pReportID = Column(Integer, primary_key=True, index=True)
    studentID = Column(Integer)
    name = Column(String)
    section = Column(String)
    violation = Column(String)
    dateTime = Column(DateTime)
    description = Column(String)
    venue = Column(String)
    status = Column(String)
    sanction = Column(String)
    guard = Column(String)

class OSADAccount(Base):
    __tablename__ = "osadacc"
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    fullName = Column(String)   
    email = Column(String)
    age = Column(Integer)
    suffix = Column(String)
    gender = Column(String)

class SekyuAccount(Base):
    __tablename__ = "sekyuacc"
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    email = Column(String)
    fullName = Column(String)
    gender = Column(String)
    age = Column(Integer)
    suffix = Column(String)

class LoginOSAD(Base):
    __tablename__ = "loginOSAD"
    timestampLogin = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    fullName = Column(String)

class LoginSekyu(Base):
    __tablename__ = "loginSekyu"
    timestampLogin = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    fullName = Column(String)


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
    age: int

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
    dateTime: datetime 
    venue: str
    status: str
    sanction: str
    studentID: int
    violationID: int
    guard: str

class PendingViolationDetailsInfo(BaseModel):
    pReportID: int
    name :str
    section :str
    studentID :int
    violation :str
    dateTime: datetime 
    description :str
    venue :str
    status :str
    sanction :str
    guard :str

class OSADAccInfo(BaseModel):
    id: int
    password: str
    email: str
    fullname: str
    age: int
    suffix: str
    gender: str

class SekyuAccInfo(BaseModel):
    id: int
    password: str
    email: str
    fullname: str
    age: int
    suffix: str
    gender: str

class LoginInfoOSAD(BaseModel):
    timestampLogin: int
    email: str
    fullName: str

class LoginInfoSekyu(BaseModel):
    timestampLogin: int
    email: str
    fullName: str


