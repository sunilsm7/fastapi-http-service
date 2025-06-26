from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/anything")
@router.post("/anything")
@router.put("/anything")
@router.delete("/anything")
@router.patch("/anything")
async def handle_anything(anything: str = "", request: Request = None):
    body = await request.body()
    return {
        "method": request.method,
        "url": str(request.url),
        "path": anything,
        "headers": dict(request.headers),
        "query": dict(request.query_params),
        "body": body.decode("utf-8") if body else None
    }
