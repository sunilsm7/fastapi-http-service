from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/redirect-to")
@router.post("/redirect-to")
@router.put("/redirect-to")
@router.delete("/redirect-to")
@router.patch("/redirect-to")
def redirect_to(url: str = Query(...)):
    return RedirectResponse(url=url)


@router.get("/redirect/{n}")
def redirect_n(n: int):
    if n <= 0:
        return {"message": "Final destination"}
    return RedirectResponse(url=f"/redirect/{n-1}")


@router.get("/relative-redirect/{n}")
def relative_redirect(n: int):
    if n <= 0:
        return {"message": "Final relative destination"}
    return RedirectResponse(url=f"/relative-redirect/{n-1}")


@router.get("/absolute-redirect/{n}")
def absolute_redirect(n: int):
    if n <= 0:
        return {"message": "Final absolute destination"}
    return RedirectResponse(url=f"/absolute-redirect/{n-1}", status_code=302)
