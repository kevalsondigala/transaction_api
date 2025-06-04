from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
API_TOKEN = "secret-token"

def authenticate(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
