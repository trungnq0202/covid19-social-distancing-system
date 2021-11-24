from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.params import Body
from fastapi.responses import JSONResponse
from starlette import status
from typing import List
from utils import models, databaseHelper

router = APIRouter(
		prefix="/humanEntryAndExit",
		tags=["humanEntryAndExit"])

@router.get("/get/people")
async def get_number_of_people_in_room():
	people = await databaseHelper.people_collection.find_one()
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content=people
            )

@router.get("/get/motions", response_model=List[models.MotionModel])
async def get_motions():
	motions = await databaseHelper.motion_collection.find().to_list(100)
	return motions

@router.post("/PersonEnter")
async def notify_person_entring():
	motion = jsonable_encoder(models.MotionModel(status = "Somebody enters"))
	await databaseHelper.motion_collection.insert_one(motion)
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"details": "Somebody enters"}
            )

@router.post("/PersonExit")
async def notify_person_exit():
	motion = jsonable_encoder(models.MotionModel(status = "Somebody exits"))
	await databaseHelper.motion_collection.insert_one(motion)
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"details": "Somebody exits"}
            )

@router.put("/update/people/{total}")
async def update_num_people(total: int):
	current_people = await databaseHelper.people_collection.find_one()
	if current_people == None:
		people = jsonable_encoder(models.PeopleModel(total = total))
		await databaseHelper.people_collection.insert_one(people)
	else:
		await databaseHelper.people_collection.update_one({"_id": current_people['_id']}, {"$set": {"total": total}})
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" : "The number of people has been updated"}
            )

@router.delete("/delete/people")
async def delete_people_info():
	await databaseHelper.people_collection.delete_many({})
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"details": "People details have been cleared"}
            )

@router.delete("/delete/motion")
async def delete_motion_info():
	await databaseHelper.motion_collection.delete_many({})
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"details": "Motion details have been cleared"}
            )