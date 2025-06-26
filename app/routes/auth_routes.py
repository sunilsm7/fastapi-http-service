from fastapi import APIRouter, Depends
from auth import verify_basic_auth, verify_bearer_auth

router = APIRouter()


@router.get("/basic-auth/{user}/{passwd}")
def basic_auth(user: str, passwd: str, _: None = Depends(verify_basic_auth)):
    return {"authenticated": True, "user": user}


@router.get("/bearer")
def bearer_auth(_: None = Depends(verify_bearer_auth)):
    return {"authenticated": True, "token_type": "Bearer"}
