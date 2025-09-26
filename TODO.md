# TODO: Run Django Music Catalog Project

- [x] Create virtual environment: `python -m venv venv`
- [x] Install dependencies: `venv\Scripts\pip install -r requirements.txt`
- [x] Run migrations: `run_django.bat migrate`
- [ ] Run the Django development server: `run_django.bat runserver`

# Fix for Lyric Delete 404 Issue

- [x] Uncomment template_name in LyricDeleteView to show confirmation page on GET
- [x] Change delete links in lyric_list.html and lyric_detail.html to AJAX buttons using delete-btn class
- [x] This prevents 404 on GET for non-existent lyrics and uses AJAX POST for deletion
