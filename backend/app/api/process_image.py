from fastapi import APIRouter, UploadFile, File, Form
from app.services.ai import generate_image
from app.utils.s3 import upload_file_to_s3

router = APIRouter()

@router.post("/api/process")
async def process_image(
    image: UploadFile = File(...),
    prompt: str = Form(...)
    ):
    #this is a hard coded image for testing
    #image_url = "https://photoeditsai-bucket.s3.us-east-2.amazonaws.com/test-images/img03.jpg"

    print("Uploading image to s3...")
    image_url = upload_file_to_s3(image)
    print("Image URL:",image_url)

    result_url = generate_image(image_url=image_url, prompt=prompt)
    
    return {
        "status": "success",
        "image": result_url  # This will be whatever replicate API returns
    }
