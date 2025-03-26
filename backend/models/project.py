from pydantic import BaseModel, Field, GetJsonSchemaHandler
from typing import Optional, Any
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: Any, handler: GetJsonSchemaHandler) -> dict[str, Any]:
        # Pydantic v2-compliant schema override
        return {"type": "string"}


# Model used for reading from DB
class ProjectModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    client_name: str
    industry: str
    description: str
    geography: Optional[str] = None
    language: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


# Model used when creating a new project
class CreateProjectModel(BaseModel):
    name: str
    client_name: str
    industry: str
    description: str
    geography: Optional[str] = None
    language: str
