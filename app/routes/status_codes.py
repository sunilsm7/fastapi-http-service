from fastapi import APIRouter
from fastapi.responses import Response
import random


router = APIRouter()


@router.api_route(
    "/status/{codes}",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    operation_id="return_status_code_all_methods"
)
def return_status_code(codes: str):
    code_list = [int(c) for c in codes.split(",")]
    selected = random.choice(code_list) if len(code_list) > 1 else code_list[0]
    return Response(status_code=selected)
