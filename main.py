from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Photo(BaseModel):
    imageName: str
    imageData: str


@app.post("/process-image/")
async def process_image(photos: List[Photo]):
    for photo in photos:
        print(photo.imageName)

    return {"Image processing complete"}
