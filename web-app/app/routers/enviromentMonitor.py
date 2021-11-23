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


@router.post("/add/{humi}/{temp}/{mois}/{level}")
def create_envi(humi: float, temp: float, mois: float, level: str):
	
    return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content={"envi"}
            )