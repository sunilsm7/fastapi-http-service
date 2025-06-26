from fastapi import APIRouter, Response
import base64
import os
import uuid
import time

router = APIRouter()


@router.get("/base64/{value}")
def decode_base64(value: str):
    return base64.urlsafe_b64decode(value.encode()).decode("utf-8")


@router.get("/bytes/{n}")
def random_bytes(n: int):
    return Response(content=os.urandom(n), media_type="application/octet-stream")


@router.get("/delay/{delay}")
@router.post("/delay/{delay}")
@router.put("/delay/{delay}")
@router.delete("/delay/{delay}")
@router.patch("/delay/{delay}")
def delay_response(delay: float):
    delay = min(delay, 10.0)
    time.sleep(delay)
    return {"delayed": delay}


@router.get("/uuid")
def get_uuid():
    return {"uuid": str(uuid.uuid4())}
