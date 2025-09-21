# Django Music Catalog Website

## Project Overview

This is a comprehensive music catalog website built with Django (Python web framework) and styled with Tailwind CSS. It manages artists, songs, and lyrics with complete CRUDL (Create, Read, Update, Delete, List) functionality.

## Features

- Complete CRUDL operations for Artistes, Songs, and Lyrics
- Responsive design with Tailwind CSS
- Django admin interface for backend management
- Sample data included (5 records per model)
- Clean navigation system

## Installation

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## Usage

- Home page: List of artistes
- Navigate to Songs and Lyrics lists via the navigation bar
- Use "Add" buttons to create new records
- View, Edit, and Delete records from the respective pages

## Models

### Artiste Model
- Fields: first_name, last_name, age, date_created
- Relationship: One-to-Many with Song

### Song Model
- Fields: title, release_date
- Relationships: Many-to-One with Artiste, One-to-One with Lyric

### Lyric Model
- Fields: content, date_created
- Relationship: One-to-One with Song

## Model Relationships Diagram

```
Artiste (1) -----> (*) Song (1) -----> (1) Lyric
```

## Screenshots

- Home page showing artiste list
- Song list with artiste information
- Lyric list with song previews
- Add/Edit forms for each model

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Technologies Used

- Django 5.2.6
- Tailwind CSS
- SQLite (default Django database)

## Contact

For questions or feedback, please open an issue on GitHub.