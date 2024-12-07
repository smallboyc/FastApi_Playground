from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import base64
import os
import binascii

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Image(BaseModel):
    image_name: str = Field(alias="imageName")
    image_data: str = Field(alias="imageData")


def base64_to_image(image: Image):
    try:
        if not os.path.exists("images"):
            os.makedirs("images")

        decoded_image_data = base64.b64decode(image.image_data, validate=True)
        file_to_save = f"images/{image.image_name}"

        with open(file_to_save, "wb") as file:
            file.write(decoded_image_data)
            print(f"Image saved as {file_to_save}")

    except binascii.Error as e:
        print(f"Error in decoding base64: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


@app.post("/process-image/")
async def process_image(images: List[Image]):
    for image in images:
        print(f"{image.image_name} = {len(image.image_data)} bytes")
        base64_to_image(image)

    return {"Image processing complete"}
