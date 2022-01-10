from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette import status
import json
from utils import models, databaseHelper

router = APIRouter(
		prefix="/qrcode",
		tags=["qrcode"])

@router.post("/")
async def read_qrcode(dateTime: str = Form(...), info: str = Form(...)):

    return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content= json.dumps({"dateTime": dateTime, "info": info})
            )



@router.post("/setFlag/{flag}")
async def set_flag(flag: bool):
	qr_flag = await databaseHelper.qr_flag_collection.find_one()
	if qr_flag == None:
		qr_flag = jsonable_encoder(models.Flag(flag=flag))
		await databaseHelper.qr_flag_collection.insert_one(qr_flag)
	else:
		await databaseHelper.qr_flag_collection.update_one({"_id": qr_flag['_id']}, 
														    	{"$set": {"flag": flag}})
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" : "QR code flag has been updated"}
            )


@router.get("/getFlag")
async def get_flag():
	flag = await databaseHelper.qr_flag_collection.find_one()
	return bool(flag["flag"])