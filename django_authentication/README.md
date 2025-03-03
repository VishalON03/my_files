1. Django Authentication System

This project implements a Django-based authentication system with cookie-based authentication, including user registration, login, OTP verification, and protected API endpoints.

## Features
- **User Registration** with email OTP verification
- **Login** using email & password
- **Secure Cookie-based Authentication**
- **CSRF Protection**
- **User Details API**
- **Logout API**
- **Swagger API Documentation**
- **Simple Frontend (HTML + JavaScript) for Testing**

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/django-authentication.git
cd django-authentication

2. Create a virtual environment:
python -m venv env
source env/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Set up environment variables:
Create a .env file in the project root:

SECRET_KEY=your-secret-key
DEBUG=True
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

5. Apply Migrations & Create Superuser:(optional)
python manage.py migrate
python manage.py createsuperuser

6. Run the server:
python manage.py runserver

API Endpoints
Method	 Endpoint	             Description
POST	 /api/register/	         Register a new user
POST	 /api/register/verify/	 Verify OTP for registration
POST	 /api/login/	         Login & set auth cookie
GET	     /api/me/	             Get logged-in user details
POST	 /api/logout/	         Logout & clear auth cookie

Testing
Swagger Documentation: Available at http://127.0.0.1:8000/swagger/
Frontend: Open authentication/templates/index.html in a browser.

Deployment
For production, use Gunicorn & set environment variables:

gunicorn django_auth.wsgi:application --bind 0.0.0.0:8000

License
This project is licensed under the MIT License.