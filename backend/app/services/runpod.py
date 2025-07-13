from diffusers import DiffusionPipeline
import torch
import uuid

#function that generate image from a prompt (on runpod) and save output as output.png
def generate_image(prompt: str, output_path: str = None):
    
    # load both base model
    base = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", 
        torch_dtype=torch.float16, 
        variant="fp16", 
        use_safetensors=True
    )
    base.to("cuda")

    # load refiner
    refiner = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-refiner-1.0",
        text_encoder_2=base.text_encoder_2,
        vae=base.vae,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16",
    )
    refiner.to("cuda")

    # Define how many steps and what % of steps to be run on each experts (80/20) here
    n_steps = 40
    high_noise_frac = 0.8

    # set the output path if not given
    if output_path is None:
        output_path = f"{uuid.uuid4().hex}.png"

    # generate with base
    image = base(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_end=high_noise_frac,
        output_type="latent",
    ).images

    # refine image
    image = refiner(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_start=high_noise_frac,
        image=image,
    ).images[0]

    # Save to disk
    image.save(output_path)
    return output_path