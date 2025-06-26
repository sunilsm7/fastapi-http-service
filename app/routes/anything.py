from fastapi import APIRouter, Request

router = APIRouter()


@router.api_route(
	"/anything",
	methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
	operation_id="handle_anything_root"
)
@router.api_route(
	"/anything/{anything:path}",
	methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
	operation_id="handle_anything_path"
)
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
