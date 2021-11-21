from fastapi import APIRouter

router = APIRouter(
		prefix="/humanEntryAndExit",
		tags=["humanEntryAndExit"])


@router.get("/")
async def get_number_of_people_in_room():
    return [{"username": "Rick"}, {"username": "Morty"}]

