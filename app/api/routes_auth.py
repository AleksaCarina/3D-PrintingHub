from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db import crud
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserCreate, UserOut
from app.schemas.auth import Token
from app.api.deps import get_current_user  
from pydantic import BaseModel



router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut, status_code=201)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.create_user(
        db,
        email=payload.email,
        hashed_password=hash_password(payload.password),
        full_name=payload.full_name
    )
    return user

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    token = create_access_token(subject=user.email)
    return Token(access_token=token)

# Optional helper: whoami
@router.get("/me", response_model=UserOut)
def me(current_user = Depends(get_current_user)):   # ← fix Depends(...)
    # You can import get_current_user lazily to avoid circulars
    from app.api.deps import get_current_user
    user = get_current_user()  # FastAPI resolves Depends
    return user

class LoginJSON(BaseModel):
    email: str
    password: str

@router.post("/login-json", response_model=Token)
def login_json(payload: LoginJSON, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, payload.email)
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    token = create_access_token(subject=user.email)
    return Token(access_token=token)
