from fastapi import APIRouter, Request, Query, Body
from fastapi import HTTPException, Depends, status
from mock_data import mock_data
from typing import List, Optional
from models import User


router = APIRouter()


@router.get("/users", response_model=List[User])
def get_users():
    return mock_data["users"]


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((u for u in mock_data["users"] if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
