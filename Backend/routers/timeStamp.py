from fastapi import APIRouter, Depends, HTTPException  
from models.database import SessionLocal, get_db
from models.models import SekyuAccount
from sqlalchemy.orm import Session

router = APIRouter(tags=["timeStamp"])  

# Assuming you have a dictionary to store the logged-in users and their timestamps
logged_in_users = {
    "2022-12-01": "user1",
    "2022-12-02": "user2",
    "2022-12-03": "user3"
}

@app.route("/username", methods=["GET"])
def get_username():
    # Get the current date
    current_date = datetime.date.today().isoformat()

    # Check if the current date exists in the logged-in users dictionary
    if current_date in logged_in_users:
        return logged_in_users[current_date]
    else:
        return "No user logged in today"

if __name__ == "__main__":
    app.run()