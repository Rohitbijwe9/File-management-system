# File Management System

A web-based file management system built using Django. This system allows users to upload, manage, and organize files in a secure and efficient way.

## Features

- User authentication (Signup, Login, Logout)
- File upload and management
- File categorization
- View files and details
- Admin panel to manage users and files

## Installation

### 1. Clone the repository

To get started with the project, clone the repository to your local machine:

```bash
git clone https://github.com/Rohitbijwe9/File-management-system.git
cd File-management-system
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Django==4.1
djangorestframework==3.14.0
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
