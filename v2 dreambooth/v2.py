from diffusers import StableDiffusionPipeline
import torch

model_id = "model2/"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

prompt = "a photo of renal cell carcinoma"
image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]

image.save("rcc5.png")
