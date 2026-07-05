from pytz import timezone

from typing import Optional, List
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt, JWTError 

from models.user_model import UserModel
from core.configs import settings
from core.security import check_password
from core.deps import get_session

from pydantic import EmailStr

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/users/login"
)

async def authenticate(email: str, password: str, db: AsyncSession) -> Optional[UserModel]:
    query = select(UserModel).filter(UserModel.email == email)
    result = await db.execute(query)
    user: UserModel = result.scalars().unique().one_or_none()

    if not user:
        return None
    
    if not check_password(password, user.password):
        return None
    
    return user

async def get_current_user(db:AsyncSession = Depends(get_session), token: str = Depends(oauth2_schema)) -> UserModel:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        sub: str = payload.get("sub")

        if sub is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    query = select(UserModel).filter(UserModel.id == int(sub))
    result = await db.execute(query)
    user = result.scalars().unique().one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user
    
def _create_token(type_token: str, time_life: timedelta, sub: str) -> str:
    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    payload = {}

    pt = timezone('Europe/Lisbon')
    expira = datetime.now(tz=pt) + time_life

    payload["type"] = type_token

    payload["exp"] = expira

    payload["iat"] = datetime.now(tz=pt)

    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def create_access_token(sub: str) -> str:
    return _create_token(
        type_token='access_token',
        time_life=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )

def create_refresh_token(sub: str) -> str:
    return _create_token(
        type_token='refresh_token',
        time_life=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        sub=sub
    )


