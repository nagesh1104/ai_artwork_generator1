import os

# Create the models directory
models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
os.makedirs(models_dir, exist_ok=True)
print(f"Created models directory at: {models_dir}")