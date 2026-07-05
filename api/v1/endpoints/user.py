from typing import List, Optional, Any

from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from models.user_model import UserModel
from schemas.user_schema import UserSchemaBase, UserSchemaCreate, UserSchemaUp, UserSchemaProducts
from core.deps import get_session
from core.security import generate_hash_password
from core.auth import authenticate, create_access_token, create_refresh_token, get_current_user

router = APIRouter()

# GET LOGGED IN
@router.get('/logged', response_model=UserSchemaBase)
async def get_logged(user_logged: UserModel = Depends(get_current_user)):
    return user_logged

# POST LOGIN
@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await authenticate(email=form_data.username, password=form_data.password, db=db)

    if not user:
        raise HTTPException(detail="Incorrent login details.",
                            status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content={"access_token": create_access_token(sub=str(user.id)), "token_type": "bearer"}, status_code=status.HTTP_200_OK)

# POST / SIGNUP
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserSchemaBase)
async def post_user(user: UserSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_user: UserModel = UserModel(
        name=user.name,
        lastname=user.lastname,
        email=user.email,
        password=generate_hash_password(user.password),
        is_admin=user.is_admin
    )

    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        return new_user
    except IntegrityError:
        raise HTTPException(detail="There is already a registered user with this email.",
                            status_code=status.HTTP_406_NOT_ACCEPTABLE)
    
# GET USERS
@router.get('/', response_model=List[UserSchemaBase])
async def get_users(db: AsyncSession = Depends(get_session), user_logged: UserModel = Depends(get_current_user)):
    query = select(UserModel)
    result = await db.execute(query)
    users: List[UserSchemaBase] = result.scalars().unique().all()

    return users

# GET USER
@router.get('/{user_id}', response_model=UserSchemaBase, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    query = select(UserModel).filter(UserModel.id == user_id)
    result = await db.execute(query)
    user: UserSchemaProducts = result.scalars().unique().one_or_none()

    if user:
        return user
    else:
        raise HTTPException(detail="User not found.",
                            status_code=status.HTTP_404_NOT_FOUND)
    
# PUT USER
@router.put('/{user_id}', response_model=UserSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_user(user_id: int, user: UserSchemaUp, db: AsyncSession = Depends(get_session), user_logged: UserModel = Depends(get_current_user)):
    query = select(UserModel).filter(UserModel.id == user_id)
    result = await db.execute(query)
    user_up: UserSchemaBase = result.scalars().unique().one_or_none()

    if user_up:
        if user.name:
            user_up.name = user.name
        if user.lastname:
            user_up.lastname = user.lastname
        if user.email:
            user_up.email = user.email
        if user.password:
            user_up.password = generate_hash_password(user.password)
        if user.is_admin:
            user_up.is_admin = user.is_admin

        await db.commit()
        await db.refresh(user_up)

        return user_up
    else:
        raise HTTPException(detail="User not found",
                            status_code=status.HTTP_404_NOT_FOUND)
    
# DELETE USER
@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_session), user_logged: UserModel = Depends(get_current_user)):
    query = select(UserModel).filter(UserModel.id == user_id)
    result = await db.execute(query)
    user_del: UserSchemaProducts = result.scalars().unique().one_or_none()

    if user_del:
        await db.delete(user_del)
        await db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(detail="User not found", 
                            status_code=status.HTTP_404_NOT_FOUND)
    
