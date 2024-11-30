# Data Drive System - Django Project

## Overview
Data Drive System is a web-based file management system built using Django. It allows users to perform CRUD (Create, Read, Update, Delete) operations on files and folders, similar to Google Drive. Users can create accounts, log in, create, update, and delete files and folders, and organize them into a hierarchical structure.

## Key Features
- User Authentication: Users can create accounts, log in, and log out.
- Folder Hierarchy: Users can create nested folders to organize their files.
- File Management: Users can create, update, and delete files within folders.

## Technology Stack
- Django (version 3+)
- Django ORM (Object-Relational Mapping)
- SQLite Database
- HTML, CSS (User Interface)

## Getting Started
1. Clone the repository to your local machine:

    ```bash
git clone https://github.com/Rohitbijwe9/File-management-system.git
cd File-management-system/Data-Drive-System
    ```

2. Create a virtual environment and install dependencies:

    
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    

3. Apply database migrations:

    python manage.py migrate

4. Create a superuser account to access the admin panel (optional):

    ```bash
    python manage.py createsuperuser
    ```

5. Start the development server:

    python manage.py runserver

6. Access the web application at [http://localhost:8000](http://localhost:8000).

## Usage
- Visit the registration page to create a new account.
- Log in using your credentials.
- Create, update, and delete folders and files within your account.

## Folder Structure
- `file_manager`: Django app for file management.
- `templates`: HTML templates for views.
- `static`: Static files (CSS, JavaScript, etc.).
- `media`: User-uploaded files (configurable in Django settings).

## Project Structure
- `file_manager/models.py`: Defines the database models (File and Folder).
- `file_manager/views.py`: Contains view functions for CRUD operations.
- `file_manager/forms.py`: Defines forms for creating and updating files and folders.
- `templates`: Contains HTML templates.
- `static`: Static files (CSS, JavaScript, etc.).
- `media`: User-uploaded files.

