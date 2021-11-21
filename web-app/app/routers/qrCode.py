from fastapi import APIRouter

router = APIRouter(
		prefix="/qrcode",
		tags=["qrcode"])

@router.get("/")
async def read_qrcode():
    return [{"username": "Rick"}, {"username": "Morty"}]

