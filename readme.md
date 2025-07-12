# section-1 -> To run the application ==============================================================

To Start the back-end:
uvicorn main:app --reload

To Start the Front-end:
npm run dev
http://localhost:3000/

# section-2 -> Major Features ======================================================================

1. Professional photo 
    a. full body
    b. headshot
2. Modeling photos
    a. Instagram
    b. Dating Sites
3. Gym photos
    a. Muscular
    b. Lifting weights
    c. doings other workouts
    d. Muscular photos with visible abs

# section-3 -> TODO ================================================================================

1. Ensure Image Size, quality, format - model not accepting RGBA photo (generally taken from interenet without permission or screenshot)
2. Implement in a way that new model (addition to existing) can be done easily
3. Choose a model 
    - model should have the ability to process the full body image or just the face image
    - or give multiple options
        - like photo for LinkedIn/Professional Looking photo
        - for Instagram (masculine, faminine), more attractive
        - for dating sites (like tinder, bumble)
        - gibili arts
4. Limits (Rate Limiting)
5. Organize the input and output 
    - so that it also works for different size of phone and computer
6. Design the UI (that looks attractive)

# section-4 -> Next Step ==========================================================================

1. Choose a base model from HuggingFace (e.g. Stable Diffusion (SD) V1.5, V2.1, Realistic Vision, DreamShaper)
    Note: SD -> are compatible with DreamBooth/LoRA, Realistic Vision, DreamShaper, etc. -> fine-tuned for realism/styling
2. Fine-tune the model using (DreamBooth or LoRA)
    a. Options to choose pre-styled LoRA model (like Movie look, Barbie, etc)
    b. And OR use custom interface scripts (with prompt engineering, upscalers, etc.)
3. Now train it on cloud infra (like RunPod, AWS or Replicate) - each of them have pros and cons
4. Once the model is trained, 
5. then generate the image with a prompt (like: "a cinematic photo of <token> wearing a tuxedo on the red carpet")
6. Extras:
    a. apply prompt engineering tricks to improve quality, GFPGAN or CodeFormer for face refiners, upscalers (e.g. Real-ESRGAN) for HD
    a. do post-processing like sharpening, face-fixing, automatic face cropping, background blur, etc.
7. Save images to cloud (S3) - based on the same token generated earlier when storing the image in the beginning to may be not neededs
5. Notify user - Return the image to user via the website or email

# My choice: 
    -> SDXL1.0 (base+refiner)
    -> Runpod (to run this model)

# section-5 -> Technical Understanding =============================================================

| Feature       | DreamBooth       | LoRA               |
| ------------- | ---------------- | ------------------ |
| Training Time | 30–60 mins       | 5–15 mins          |
| File Size     | \~4GB            | \~3–10MB           |
| Quality       | Very high        | High (if tuned)    |
| GPU Cost      | Higher           | Lower              |
| Flexibility   | Less (per model) | More (swap easily) |

LoRA - Lightweight Fine-Tuning
