from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse

from .routers import enviromentMonitor, humanEntryAndExit, qrCode

app = FastAPI()


app.include_router(enviromentMonitor.router)
app.include_router(humanEntryAndExit.router)
app.include_router(qrCode.router)



@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")
