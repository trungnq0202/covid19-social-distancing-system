# username: admin
# password: admin
import motor.motor_asyncio

MONGODB_URL = "mongodb+srv://admin:admin@cluster0.xnulm.mongodb.net/Covid19socialDistancingSystem?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.covidDistancingSystem

motion_collection = db.motion_collection
envi_collection = db.envi_collection
people_collection = db.people_collection
task3_flag_collection = db.task3_flag_collection
task4_flag_collection = db.task4_flag_collection
qr_code_status_collection = db.qr_code_status_collection