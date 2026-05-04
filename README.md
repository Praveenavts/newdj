# Simple Django Image Upload Project

## Features
- Admin panel image upload
- Uploaded images display on front page
- CSS stored in static folder
- SQLite database

## Run Steps

```bash
cd simple_django_image_project
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## URLs
- Front page: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Admin Usage
1. Login to admin panel.
2. Click **Home Images**.
3. Add title, description, and image.
4. Save.
5. Open front page to view the uploaded image.
