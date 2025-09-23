from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from user import UserDb
from pydantic import BaseModel, EmailStr, field_validator

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


    
class Tweet(BaseModel):
    content: str
    hastags: list[str]


class UserBody(BaseModel):
    name: str
    email: EmailStr
    age: int
    tweets: list[Tweet] | None = None

    @field_validator("age")
    @classmethod
    def validate_age(cls, value: int):
        if value < 18 or value > 100:
            raise ValueError(
                "Age must be between 18 and 100"
            )
        return value
    


@app.post("/user")
async def add_user(user: UserBody, db: Session = Depends(get_db)):
    new_user = UserDb(
        name = user.name, 
        email = user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/user/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = (db.query(UserDb).filter(UserDb.id == user_id).first())

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )
    
    return user

@app.put("/user/{user_id}")
async def update_user(user_id: int,
                      user: UserBody,
                      db: Session = Depends(get_db)):
    db_user =  db.query(UserDb).filter(UserDb.id == user_id).first()

    if not db_user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)

    return db_user



@app.get("/users", response_model= list[UserBody])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(UserDb).all()
    return users


@app.delete("/user/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDb).filter(UserDb.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )
    
    db.delete(user)
    db.commit()
    return {"detail": "User deleted"}


