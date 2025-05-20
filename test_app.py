import os
import django
import sys

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_art_generator.settings')
django.setup()

# Import models and functions
from django.contrib.auth.models import User
from image_generator.models import GeneratedImage, EditHistory
from image_generator.views import get_image_generator

def test_model_loading():
    """Test if the model can be loaded successfully"""
    print("Testing model loading...")
    try:
        pipe = get_image_generator()
        print("[SUCCESS] Model loaded successfully!")
        return pipe
    except Exception as e:
        print(f"[ERROR] Error loading model: {str(e)}")
        return None

def test_image_generation(pipe, prompt="A beautiful sunset over mountains"):
    """Test image generation with a simple prompt"""
    if pipe is None:
        print("[ERROR] Cannot test image generation because model failed to load")
        return None
    
    print(f"Testing image generation with prompt: '{prompt}'...")
    try:
        image = pipe(
            prompt,
            num_inference_steps=25,
            guidance_scale=7.5,
            height=512,
            width=512,
        ).images[0]
        print("[SUCCESS] Image generated successfully!")
        
        # Save the image to a file for inspection
        test_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_image.png')
        image.save(test_image_path)
        print(f"[SUCCESS] Test image saved to: {test_image_path}")
        return image
    except Exception as e:
        print(f"[ERROR] Error generating image: {str(e)}")
        return None

def test_database():
    """Test database connectivity and models"""
    print("Testing database connectivity...")
    try:
        # Count users
        user_count = User.objects.count()
        print(f"[SUCCESS] Database connected successfully! Found {user_count} users.")
        
        # Count images
        image_count = GeneratedImage.objects.count()
        print(f"[SUCCESS] Found {image_count} generated images in the database.")
        
        # Count edits
        edit_count = EditHistory.objects.count()
        print(f"[SUCCESS] Found {edit_count} edit history records in the database.")
        
        return True
    except Exception as e:
        print(f"[ERROR] Error connecting to database: {str(e)}")
        return False

def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("STARTING APPLICATION TESTS")
    print("=" * 50)
    
    # Test model loading
    pipe = test_model_loading()
    
    # Test image generation
    test_image_generation(pipe)
    
    # Test database
    test_database()
    
    print("=" * 50)
    print("TESTS COMPLETED")
    print("=" * 50)

if __name__ == "__main__":
    run_all_tests()