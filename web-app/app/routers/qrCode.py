from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from starlette import status
import json

router = APIRouter(
		prefix="/qrcode",
		tags=["qrcode"])

@router.post("/")
async def read_qrcode(dateTime: str = Form(...), info: str = Form(...)):

    return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content= json.dumps({"dateTime": dateTime, "info": info})
            )

