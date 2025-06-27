# Sample-Django-API

This project implements a REST API using [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/). Below are the steps to get the project up and running.

## Purpose

This project serves as a **starter template** for backend developers. It is designed to help them extend the API based on provided requirements and test API endpoints.

The project is set up with [PostgreSQL](https://www.postgresql.org/) as the default database for development purposes, which provides a robust solution for handling relational data.

## Requirements

- **Docker and Docker Compose**: Used for containerizing the application and managing dependencies.
- **Git**: Used for cloning the project repository.
- **Python 3.12+**: Required to run the application.
- **Poetry**: Used for managing Python dependencies.

## Installation

Follow these steps to set up the project for development:

1. **Check dependencies**

   Ensure Docker, Docker Compose, Git, Python 3.12+, and Poetry are installed on your system.

2. **Clone the repository**

   Clone the repository and navigate to the project directory:
   ```bash
   git clone git@github.com:Deeplace/Sample-Django-API.git
   cd Sample-Django-API
   ```

3. **Install Python dependencies**

   Use Poetry to install the required Python dependencies:
   ```bash
   poetry install
   ```

4. **Copy the environment file**

   Copy the `.env-example` file to `.env` and update the environment variables if necessary:
   ```bash
   cp .env-example .env
   ```

5. **Copy the override file**

   Copy the `docker-compose.override-example.yml` file to `docker-compose.override.yml` to enable additional configurations:
   ```bash
   cp docker-compose.override-example.yml docker-compose.override.yml
   ```

6. **Build and start the containers**

   Build and start the containers. The application will be accessible at `http://localhost:8000`:
   ```bash
   docker compose up --build --detach
   ```

7. **Start watch mode**

   Use the following command to enable watch mode for development:
   ```bash
   docker compose watch
   ```

## Additional Information

- You only need to copy the environment and override files, build the containers, and set up the database once. These steps prepare your local environment for development.
- You need to run the containers each time you want to test or develop the project.



 ______________________________________________________
 ______________________________________________________
## Project Steps



🚀 Survey Project — Django + React Setup Guide
📦 Requirements:
    1. Python 3.12+
    2. Node.js 18+ / npm
    3. Docker + Docker Compose
    4. Git (optional but helpful)


⚙️ Backend (Django)
🔹 1. Create .env (or use existing) 
   Make sure the .env contains at least:

env:
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
POSTGRES_DB=survey
POSTGRES_USER=survey
POSTGRES_PASSWORD=survey

🔹 2. Build and start backend
docker compose up -d --build

🔹 3. Run migrations + seed data

docker compose exec django python manage.py migrate
docker compose exec django python manage.py createsuperuser

Or use the built-in migration that auto-creates questions (with admin user):

docker compose exec django python manage.py migrate


🌐 Frontend (React)

🔹 1. Go to survey-frontend

   cd survey-frontend

🔹 2. Install dependencies

   npm install

🔹 3. Start development server

   npm start

Visit: http://localhost:3000


🔑 Auth & API

    Obtain JWT token: POST /api/token/ With { "email": "admin@example.com", "password": "admin123" }

    Use token for authorized requests:

    Authorization: Bearer <access_token>




For questions run command

python manage.py makemigrations --empty survey -n initial_questions

create migration file and insert next qustions

```
from django.db import migrations
from django.contrib.auth import get_user_model

def create_initial_questions(apps, schema_editor):
    Question = apps.get_model("survey", "Question")
    Answer = apps.get_model("survey", "Answer")

    q1 = Question.objects.create(text="Столица Франции?", is_active=True)
    Answer.objects.create(question=q1, text="Париж", is_correct=True, user=admin)
    Answer.objects.create(question=q1, text="Берлин", is_correct=False, user=admin)

    q2 = Question.objects.create(text="2 + 2 = ?", is_active=True)
    Answer.objects.create(question=q2, text="4", is_correct=True, user=admin)
    Answer.objects.create(question=q2, text="5", is_correct=False, user=admin)

    q3 = Question.objects.create(text="Цвет неба в ясный день?", is_active=True)
    Answer.objects.create(question=q3, text="Синий", is_correct=True, user=admin)
    Answer.objects.create(question=q3, text="Оранжевый", is_correct=False, user=admin)


def reverse_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_initial_questions, reverse_func),
    ]
```
