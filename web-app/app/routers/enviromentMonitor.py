from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette import status
from utils import models, databaseHelper
from typing import List

router = APIRouter(
		prefix="/envimonitor",
		tags=["envimonitor"])

@router.get("/get", response_model=List[models.EnviModel])
async def get_environment_info():
	envi_list = await databaseHelper.envi_collection.find().to_list(100)
	return envi_list



@router.post("/add/{humi}/{temp}/{level}")
async def create_envi(humi: float, temp: float, level: str):
	envi = jsonable_encoder(models.EnviModel(humi = humi, temp = temp, level = level))
	await databaseHelper.envi_collection.insert_one(envi)
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"details": "Environment details have been added"}
            )



@router.delete("/delete")
async def delete_environment_info():
	await databaseHelper.envi_collection.delete_many({})
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"details": "Environment details have been cleared"}
            )