from fastapi import FastAPI
from models.database import SessionLocal, engine
from models.models import Base
from routers import  student, violation_details, osad_users, sekyu_users, loginOSAD, loginSekyu, pendingViolations, pendingAccountsSekyu, pendingAccountsOSAD, exception, violation
from fastapi.middleware.cors import CORSMiddleware
from models.models import Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student.router)
app.include_router(violation_details.router)
app.include_router(osad_users.router)
app.include_router(sekyu_users.router)
app.include_router(pendingViolations.router)
app.include_router(loginOSAD.router)
app.include_router(loginSekyu.router)
app.include_router(pendingAccountsSekyu.router)
app.include_router(pendingAccountsOSAD.router)
app.include_router(exception.router)
app.include_router(violation.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all origins (restrict in production)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)