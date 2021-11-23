# username: admin
# password: admin
import motor.motor_asyncio

MONGODB_URL = "mongodb+srv://admin:<admin>@cluster0.xnulm.mongodb.net/Covid19socialDistancingSystem?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.covidDistancingSystem

motion_collection = db.motion_collection
envi_collection = db.envi_collection
