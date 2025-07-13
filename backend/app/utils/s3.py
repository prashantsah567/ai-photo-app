from dotenv import load_dotenv
load_dotenv()

import boto3
import os
import uuid
from fastapi import UploadFile

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

def upload_file_to_s3(file_path: str):
    bucket = os.getenv("S3_BUCKET")
    folder = os.getenv("S3_FOLDER")

    if not bucket or not folder or not os.getenv("AWS_REGION"):
        raise ValueError("One or more required environment variables are missing.")
    
    unique_filename = f"{folder}/{uuid.uuid4()}-filename"

    with open(file_path, "rb") as f:
        s3.upload_fileobj(
            f, # open file stream
            bucket,
            unique_filename,
            ExtraArgs={"ContentType": "image/png"}
        )

    public_url = f"https://{bucket}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{unique_filename}"
    return public_url
