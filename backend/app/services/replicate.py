import replicate
import os

replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

MODEL_VERSION = "adirik/stylemc:708f7bca82339e47999c6dcec9bae35e134997dc7cfa40108eea4e4f0defcfe7"

def generate_image(image_url: str, prompt: str) -> str:
    print(f"[Replicate] Calling model with image: {image_url}, prompt: {prompt}")

    output = replicate.run(
        MODEL_VERSION,
        input={
            "image": image_url,
            "prompt": prompt
        }
    )

    print("[Replicate] Output:", output)

    return str(output)  # This is a URL to the edited image
