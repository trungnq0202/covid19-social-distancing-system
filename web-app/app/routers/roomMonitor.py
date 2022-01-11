from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette import status
import json
from utils import models, databaseHelper


router = APIRouter(
		prefix="/roomMonitor",
		tags=["roomMonitor"])


@router.post("/setTask3Flag/{flag}")
async def set_task3_flag(flag: bool):
	task3_flag = await databaseHelper.task3_flag_collection.find_one()
	if task3_flag == None:
		task3_flag = jsonable_encoder(models.AlertFlag(flag=flag))
		await databaseHelper.task3_flag_collection.insert_one(task3_flag)
	else:
		await databaseHelper.task3_flag_collection.update_one({"_id": task3_flag['_id']}, 
														    	{"$set": {"flag": flag}})
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" : "task 3 flag updated"}
            )


@router.get("/getTask3Flag")
async def get_task3_flag():
	flag = await databaseHelper.task3_flag_collection.find_one()
	return flag["flag"]


@router.post("/setTask4Flag/{flag}")
async def set_task4_flag(flag: bool):
	task4_flag = await databaseHelper.task4_flag_collection.find_one()
	if task4_flag == None:
		task4_flag = jsonable_encoder(models.AlertFlag(flag=flag))
		await databaseHelper.task4_flag_collection.insert_one(task4_flag)
	else:
		await databaseHelper.task4_flag_collection.update_one({"_id": task4_flag['_id']}, 
														    	{"$set": {"flag": flag}})
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" : "task 4 flag updated"}
            )


@router.get("/getTask4Flag")
async def get_task4_flag():
	flag = await databaseHelper.task4_flag_collection.find_one()
	return flag["flag"]