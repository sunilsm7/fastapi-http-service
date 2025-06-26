from fastapi import APIRouter, Request


router = APIRouter()


@router.get("/headers")
async def get_headers(request: Request):
    return dict(request.headers)


@router.get("/ip")
async def get_ip(request: Request):
    return {"origin": request.client.host}


@router.get("/user-agent")
async def get_user_agent(request: Request):
    return {"user-agent": request.headers.get("user-agent")}
