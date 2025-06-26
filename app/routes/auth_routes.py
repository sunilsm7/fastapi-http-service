from datetime import timedelta
from fastapi import APIRouter, Depends
from auth import (
    verify_basic_auth,
    verify_bearer_auth,
    authenticate_user,
    create_access_token,
    get_current_user,
    Token,
    User,
    fake_users_db
)
from fastapi import Depends, HTTPException, status

router = APIRouter()


ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.get("/basic-auth/{user}/{passwd}")
def basic_auth(user: str, passwd: str, _: None = Depends(verify_basic_auth)):
    return {"authenticated": True, "user": user}


@router.get("/bearer")
def bearer_auth(_: None = Depends(verify_bearer_auth)):
    return {"authenticated": True, "token_type": "Bearer"}


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: User):
    user = authenticate_user(
        fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Protected endpoint example


@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "You have accessed a protected route", "user": current_user.username}
