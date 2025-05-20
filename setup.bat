@echo off
echo Setting up AI Art Generator...

echo Installing dependencies...
pip install -r requirements.txt

echo Running migrations...
python manage.py migrate

echo Creating directories...
if not exist media mkdir media
if not exist media\generated_images mkdir media\generated_images
if not exist media\edited_images mkdir media\edited_images
if not exist static mkdir static

echo Collecting static files...
python manage.py collectstatic --noinput

echo Setup complete!
echo.
echo To start the application, run: run.bat
echo.