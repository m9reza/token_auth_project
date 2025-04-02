# Token-Based Authentication Web App

## Overview
This is a simple web application built with **Python** and **Django** as part of a student project. The app allows users to register, log in, post text content, and view posts on a homepage. The key feature of this project is the **manual implementation of token-based authentication** using access and refresh tokens, without relying on Django's built-in authentication or third-party libraries.

### Features
- **User Registration and Login**: Users can create an account and log in using a username and password.
- **Token-Based Authentication**:
  - Manually implemented access tokens (short-lived, 5 minutes) and refresh tokens (long-lived, 7 days).
  - Access tokens are validated for expiration and integrity.
  - Refresh tokens are stored in the database and can be invalidated on logout.
- **Post Submission**: Authenticated users can submit text posts, which are displayed on the homepage.
- **Logout**: Users can log out, which invalidates their refresh token and clears the session.
- **Basic Styling**: The app includes a clean, modern design with CSS for a better user experience.

### Tech Stack
- **Backend**: Python, Django
- **Database**: SQLite (default for Django)
- **Frontend**: HTML, CSS
- **Authentication**: Custom token-based authentication (access and refresh tokens)

## Setup and Installation
Follow these steps to run the project locally:

### Prerequisites
- Python 3.10 or higher
- Git

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/token-auth-project.git
   cd token-auth-project

2. **Create a Virtual Environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Run the Development Server**:
   ```bash
   python manage.py runserver

6. **Access the App**: Open your browser and go to http://127.0.0.1:8000/.



### Usage

- Visit /register/ to create a new account.
- Visit /login/ to log in with your credentials.
- After logging in, you’ll be redirected to the homepage (/), where you can submit posts and view all posts.
- Click "Logout" to end your session.

### Project Structure

token_auth_project/
├── manage.py
├── static/
│   ├── css/
│   │   └── styles.css
│   └── images/
├── templates/
│   ├── login.html
│   ├── register.html
│   └── home.html
├── token_auth_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts/
│   ├── __init__.py
│   ├── migrations/
│   ├── models.py
│   ├── token_manager.py
│   └── views.py
├── .gitignore
├── README.md
└── requirements.txt

### Notes

- This project was developed as a student exercise to demonstrate manual token-based authentication.
- The app uses SQLite for simplicity, but you can switch to another database (e.g., PostgreSQL) by updating settings.py.
- Tokens are stored in the session for simplicity. In a production app, they should be sent via HTTP headers or secure cookies.

### License
This project is licensed under the MIT License.

