from fastapi import APIRouter

router = APIRouter(
		prefix="/envimonitor",
		tags=["envimonitor"])

@router.get("/")
async def get_environment_info():
    return [{"username": "Rick"}, {"username": "Morty"}]

