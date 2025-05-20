# AI Art Generator

A web application that generates animistic images from text descriptions using AI.

## Features

- Text-to-image generation with AI
- Image editing capabilities
- User authentication
- Save and manage generated images
- Public/private image sharing

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/ai_art_generator.git
cd ai_art_generator
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run migrations:
```
python manage.py migrate
```

4. Create a superuser (admin):
```
python manage.py createsuperuser
```

5. Run the development server:
```
python manage.py runserver
```

6. Access the application at http://127.0.0.1:8000/

## Usage

1. Register for an account or log in
2. Go to "Generate Image" to create a new image
3. Enter a detailed text prompt describing the image you want
4. View and edit your images in "My Images"

## Technologies Used

- Django
- Hugging Face Diffusion Models
- PyTorch
- Bootstrap
- HTML/CSS/JavaScript