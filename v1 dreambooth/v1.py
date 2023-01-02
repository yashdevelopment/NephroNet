from diffusers import StableDiffusionPipeline
import torch

model_id = "model1/"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

prompt = "a photo of renal cell carcinoma"
image = pipe(prompt, num_inference_steps=40, guidance_scale=7.5).images[0]

image.save("40rcc5.png")
