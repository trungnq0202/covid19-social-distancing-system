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
async def set_flag():
	flag = await databaseHelper.alert_flag_collection.find_one()
	if flag == None:
		flag = jsonable_encoder(models.AlertFlag(flag=flag))
		await databaseHelper.alert_flag_collection.insert_one(flag)
	else:
		await databaseHelper.alert_flag_collection.update_one({"_id": flag['_id']}, 
														    	{"$set": {"flag": flag}})
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" : "The number of people has been updated"}
            )

@router.get("/getFlag")
async def get_flag():
	flag = await databaseHelper.alert_flag_collection.find_one()
	return flag["flag"]