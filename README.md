# PP4 Booking System - Golf Booking Site

A full-stack web application for managing golf course bookings. Built as part of the Code Institute Portfolio Project 4 (PP4).

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Features

- **User Authentication** — Register, login, logout (with Django Allauth)
- **Booking Management** — Create, view, and manage golf tee time bookings
- **Responsive Design** — Mobile-friendly UI built with Bootstrap
- **Admin Dashboard** — Manage bookings and users via Django admin
- **Real-time Feedback** — Success messages and validation
- **Secure** — CSRF protection, user-specific booking access

## Demo

Live demo: [Add your deployed link here](https://your-app.herokuapp.com)  
*(Currently deployed on Heroku / Render / Railway)*

## Technologies Used

**Backend:**
- Python 3.8+
- Django 4.x
- SQLite (development) / PostgreSQL (production)

**Frontend:**
- HTML5 / CSS3
- JavaScript
- Bootstrap 5
- Font Awesome

**Other:**
- Git / GitHub
- Gitpod
- Whitenoise (static files)
- Gunicorn + Procfile (deployment)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/keith1729/pp4-booking-system.git
   cd pp4-booking-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file and add:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ```

5. **Run migrations & start server**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

## Usage

- Visit `http://127.0.0.1:8000`
- Register a new account or login
- Browse available tee times and create bookings
- View your bookings in the dashboard

## Project Structure

```
pp4-booking-system/
├── booking/              # Main booking app
├── my_project/           # Django project settings
├── static/               # Static files (CSS, JS)
├── templates/            # HTML templates
├── manage.py
├── Procfile
├── requirements.txt
└── README.md
```

## Testing

- Manual testing completed for all user flows
- Django unit tests available: `python manage.py test`
- All CRUD functionality and authentication tested

## Deployment

This project is configured for deployment on **Heroku**. Key files:
- `Procfile`
- `requirements.txt`
- Static files handled with Whitenoise

## Credits

- **Code Institute** — PP4 Full Stack Frameworks with Django template & guidance
- **Bootstrap** — UI framework
- **Font Awesome** — Icons

---

**Made with ❤️ by Keith O'Donoghue**