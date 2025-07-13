from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.runpod import generate_image

#exposing runpod image generator function via Fast API (to call from frontend)

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/runpod-generate")
def generate_endpoint(request: PromptRequest):
    try:
        print(f"Received prompt: {request.prompt}")
        output_file = generate_image(request.prompt)
        print(f"Generated image saved to : {output_file}")
        return {"status": "success", "file": output_file}
    except Exception as e:
        print(f"Error during generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
