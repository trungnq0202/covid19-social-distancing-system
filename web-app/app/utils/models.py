from pydantic import BaseModel, Field
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class MotionModel(BaseModel):
    status: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class EnviModel(BaseModel):
    humi: float = Field(...)
    temp: float = Field(...)
    mois: float = Field(...)
    level: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class PeopleModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    total: int = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
