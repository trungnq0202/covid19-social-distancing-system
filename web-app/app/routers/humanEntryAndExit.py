from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette import status


router = APIRouter(
		prefix="/humanEntryAndExit",
		tags=["humanEntryAndExit"])


@router.get("/")
async def get_number_of_people_in_room():
	"""
	get the current number of people in a room
	"""
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" :" There are no more people in the room"}
            )

@router.post("/PersonEnter")
async def notify_person_entring():
	'''
	Notify there is a person entering
	'''
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" :" A person is entering the room"}
            )

@router.post("/PersonExit")
async def notify_person_exit():
	"""
	Notify there is a person leaving
	"""
	
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" :" A person is leaving the room"}
            )

@router.put("/updateNumPeople")
async def update_num_people(numberOfPeople):
	"""
	Update number of people in the room
	"""
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" :" The numbe of people is updated"}
            )