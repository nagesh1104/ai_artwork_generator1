import torch
from diffusers import StableDiffusionPipeline

print(f'PyTorch version: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
print('Import successful!')

# Try to initialize a simple model
try:
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    )
    print("Model initialization successful!")
except Exception as e:
    print(f"Error initializing model: {str(e)}")