from diffusers import StableDiffusionPipeline
import torch

model_id = "model3/"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

prompt = "A <kidney cancer-image>"

num_images = 5

for i in range(num_images):
    image = pipe(prompt, num_inference_steps=40, guidance_scale=7.5).images[0]
    image.save(f"40rcc{i}.png")
