from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette import status
import json
from utils import models, databaseHelper


router = APIRouter(
		prefix="/roomMonitor",
		tags=["roomMonitor"])


@router.post("/setFlag/{flag}")
async def set_flag(flag: bool):
	alert_flag = await databaseHelper.alert_flag_collection.find_one()
	if alert_flag == None:
		alert_flag = jsonable_encoder(models.Flag(flag=flag))
		await databaseHelper.alert_flag_collection.insert_one(alert_flag)
	else:
		await databaseHelper.alert_flag_collection.update_one({"_id": alert_flag['_id']}, 
														    	{"$set": {"flag": flag}})
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" : "Alert flag has been updated"}
            )

@router.get("/getFlag")
async def get_flag():
	flag = await databaseHelper.alert_flag_collection.find_one()
	return bool(flag["flag"])