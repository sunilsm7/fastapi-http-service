from fastapi.security import HTTPBearer, HTTPBasic, HTTPBasicCredentials, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
import secrets

basic_auth = HTTPBasic()
bearer_auth = HTTPBearer()

def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    correct_username = secrets.compare_digest(credentials.username, "user")
    correct_password = secrets.compare_digest(credentials.password, "pass")
    if not (correct_username and correct_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Basic Auth")

def verify_bearer_auth(token: HTTPAuthorizationCredentials = Depends(bearer_auth)):
    if token.credentials != "testtoken123":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Bearer Token")
