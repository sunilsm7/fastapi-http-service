from datetime import datetime, timedelta
from jose import JWTError, jwt

from pydantic import BaseModel
from typing import Optional

from fastapi.security import HTTPBearer, HTTPBasic, HTTPDigest, HTTPBasicCredentials, HTTPAuthorizationCredentials
from fastapi import HTTPException, Depends, status
from config import settings
import secrets
import bcrypt

# JWT Configuration
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
AUTH_TEST_USERNAME = settings.AUTH_TEST_USERNAME
AUTH_TEST_PASSWORD = settings.AUTH_TEST_PASSWORD


# Models
class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# Mock database
fake_users_db = {
    "testuser": {
        "username": AUTH_TEST_USERNAME,
        "hashed_password": bcrypt.hashpw(AUTH_TEST_PASSWORD.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
    }
}


security_basic = HTTPBasic()
security_bearer = HTTPBearer()
security_digest = HTTPDigest()


def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security_basic)):
    correct_username = secrets.compare_digest(credentials.username, AUTH_TEST_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, AUTH_TEST_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Basic Auth")


def verify_bearer_auth(token: HTTPAuthorizationCredentials = Depends(security_bearer)):
    if token.credentials != "testtoken123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Bearer Token")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User(username=user_dict["username"], password=user_dict["hashed_password"])


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(HTTPBearer())):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY,
                             algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user
