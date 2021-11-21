from fastapi import Depends, FastAPI

from .routers import enviromentMonitor, humanEntryAndExit, qrCode

app = FastAPI()


app.include_router(enviromentMonitor.router)
app.include_router(humanEntryAndExit.router)
app.include_router(qrCode.router)



@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
