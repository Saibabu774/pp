from fastapi import APIRouter, HTTPException
from ..schemas import response_schema

router = APIRouter()

fake_users_db = {} # temporary. Replace with DB later

@router.post("/register", response_model=response_schema.UserOut)
def register(user: response_schema.UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    fake_users_db[user.email] = user.dict()
    return {"id": len(fake_users_db), "name": user.name, "email": user.email, "role": user.role}

@router.post("/login")
def login(user: response_schema.UserLogin):
    db_user = fake_users_db.get(user.email)
    if not db_user or db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return {"access_token": "fake-token-for-" + user.email, "token_type": "bearer"}