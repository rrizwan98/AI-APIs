from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlmodel import Session
from utils import count_dogs_in_image


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class ImageUrl(BaseModel):
    url: str

router = APIRouter()

@router.get("/")
async def ok_endpoint():
    return {
        "message": """Hello Agriculture APIs!
        Please use the following endpoints:
        - /hello
        - /flower_recognition
        - /plant_diseases
        - /rec_plant_tree"""
    }

@router.post("/count_dogs_API")
async def count_dogs_API(
    image: ImageUrl,
    title: str = "count_dogs_API",
):
    """
    Count the number of dogs in an image using flower recognition logic.

    Parameters:
    image (ImageUrl): The URL of the image to analyze.
    title (str, optional): The title of the API. Defaults to "count_dogs_API".

    Returns:
    dict: A dictionary containing the title and the description of the image.

    """
    description: str = count_dogs_in_image(image.url)
    return {"title": title, "image_description": description}

