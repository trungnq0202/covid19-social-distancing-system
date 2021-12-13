from time import daylight
from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn
from routers import enviromentMonitor, humanEntryAndExit, qrCode

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(enviromentMonitor.router)
app.include_router(humanEntryAndExit.router)
app.include_router(qrCode.router)



@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")

#if __name__ == "__main__":
#	uvicorn.run(app, host="0.0.0.0", port=8000, access_log=True)

