from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError
from app.core.security import decode_token
from app.db.database import get_db
from app.db.crud import get_user_by_email
from app.schemas.auth import TokenPayload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = TokenPayload(**decode_token(token))
    except JWTError:
        raise credentials_exc
    if not payload.sub:
        raise credentials_exc
    user = get_user_by_email(db, payload.sub)
    if not user or not user.is_active:
        raise credentials_exc
    return user
