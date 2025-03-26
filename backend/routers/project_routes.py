from fastapi import APIRouter, HTTPException
from models.project import CreateProjectModel, ProjectModel
from services.db import db
from bson import ObjectId

router = APIRouter()


@router.post("/", response_model=ProjectModel)
async def create_project(project: CreateProjectModel):
    project_data = project.dict()
    result = await db["projects"].insert_one(project_data)

    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to create project")

    created_project = await db["projects"].find_one({"_id": result.inserted_id})
    return ProjectModel(**created_project)
