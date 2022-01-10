from threading import Thread
from time import sleep
from cv2 import log
from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette import status
import json
from utils import models, databaseHelper, qr_scan


router = APIRouter(
		prefix="/qrcode",
		tags=["qrcode"])

@router.post("/")
async def read_qrcode(dateTime: str = Form(...), info: str = Form(...)):

    return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content= json.dumps({"dateTime": dateTime, "info": info})
            )

@router.post("/setStatus/{_status}")
async def set_status(_status: str):
	qr_status = await databaseHelper.qr_code_status_collection.find_one()
	if qr_status == None:
		qr_status = jsonable_encoder(models.QRCodeScanning(status=_status))
		await databaseHelper.qr_code_status_collection.insert_one(qr_status)
	else:
		await databaseHelper.qr_code_status_collection.update_one({"_id": qr_status['_id']}, 
														    	{"$set": {"status": _status}})
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"status" : _status}
            )

@router.get("/getStatus")   
async def get_status():
	qr_status = await databaseHelper.qr_code_status_collection.find_one()
	return qr_status["status"]

@router.get("/start-scanning")
async def scan_qr_code():   
    qr_scan_result = qr_scan.scan_qr_code("http://172.20.10.3:8082/")
    qr_status = await databaseHelper.qr_code_status_collection.find_one()
    res = ""
    if qr_scan_result:
        res = "success"
    else:
        res = "fail"
    await databaseHelper.qr_code_status_collection.update_one({"_id": qr_status['_id']}, 
														    	{"$set": {"status": res}})
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "pending"}
    )