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
