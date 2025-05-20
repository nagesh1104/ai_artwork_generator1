import os
from diffusers import DiffusionPipeline

# Create the models directory
models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
os.makedirs(models_dir, exist_ok=True)

# Path for the tiny model
tiny_model_path = os.path.join(models_dir, 'tiny-stable-diffusion-pipe')

# Download the tiny test model
print(f"Downloading tiny test model to: {tiny_model_path}")
pipe = DiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-pipe")
pipe.save_pretrained(tiny_model_path)
print("Tiny test model downloaded successfully!")