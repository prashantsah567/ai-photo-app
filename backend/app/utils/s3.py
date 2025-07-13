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

print("AWS_BUCKET_NAME::::::::::::::::::::::::::::::::: ", os.getenv("S3_BUCKET"))

def upload_file_to_s3(file: UploadFile):
    bucket = os.getenv("S3_BUCKET")
    folder = os.getenv("S3_FOLDER")
    unique_filename = f"{folder}/{uuid.uuid4()}-filename"

    s3.upload_fileobj(
        file.file, # the actual file stream
        bucket,
        unique_filename,
        ExtraArgs={"ContentType": file.content_type}
    )

    public_url = f"https://{bucket}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{unique_filename}"
    return public_url
