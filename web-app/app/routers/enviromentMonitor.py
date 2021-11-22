from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette import status


router = APIRouter(
		prefix="/envimonitor",
		tags=["envimonitor"])

@router.get("/")
async def get_environment_info():
	"""
	Get the environment information from the senor
	"""


	return [{"username": "Rick"}, {"username": "Morty"}]



@router.post("/updates")
async def update_environment_info(timestamp, temperature, humidity):
	"""
	Update the environment information from the senor
	"""

	responses_message = " The current temperature and humidity are " + humidity + "and" + temperature
	return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"detail" : responses_message}
            )