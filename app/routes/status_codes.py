from fastapi import APIRouter, HTTPException
from fastapi.responses import Response, JSONResponse
from http import HTTPStatus
import random

router = APIRouter()


@router.get("/status/{codes}")
@router.post("/status/{codes}")
@router.put("/status/{codes}")
@router.delete("/status/{codes}")
@router.patch("/status/{codes}")
async def return_status_code(codes: str):
    """
    Returns the specified HTTP status code or a random one if multiple codes are provided.
    """
    try:
        code_list = [code.strip() for code in codes.split(',') if code.strip()]

        if not code_list:
            raise HTTPException(
                status_code=400,
                detail="At least one status code must be provided"
            )

        # Validate all codes before processing
        validated_codes = validate_all_codes(code_list)

        # Select a code (random if multiple provided)
        selected_code = random.choice(validated_codes) if len(
            validated_codes) > 1 else validated_codes[0]

        # Special handling for codes with no content
        if selected_code in (HTTPStatus.NO_CONTENT, HTTPStatus.NOT_MODIFIED):
            return Response(status_code=selected_code)

        # Standard response with status code
        return JSONResponse(
            content={
                "status": selected_code,
                "message": HTTPStatus(selected_code).phrase,
                "description": HTTPStatus(selected_code).description
            },
            status_code=selected_code
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error processing status codes: {str(e)}"
        )


def is_valid_http_status(code: int) -> bool:
    """Check if the code is a valid HTTP status code"""
    try:
        HTTPStatus(code)
        return True
    except ValueError:
        return False


def validate_all_codes(code_list: list):
    validated_codes = []
    for code in code_list:
        try:
            status_code = int(code)
            if not is_valid_http_status(status_code):
                raise ValueError(
                    f"Invalid HTTP status code: {status_code}")
            validated_codes.append(status_code)
        except ValueError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid status code: {code}. {str(e)}"
            )
    return validated_codes
