import mysql.connector




DB_URL = "mysql+pymysql://kobe:oliviahyejoo@localhost:3306/dbgroup12"

app = FastAPI()
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
