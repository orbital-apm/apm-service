# apm-service
Back-end service for APM.

## Description
This is a brief template that provides the basic setup to create the backend portion using FastAPI. The documentation of the API is done using SwaggerUI, and Pydantic is used for data validation and setting management.

## Dependencies
- Python 3.12.3

## &#127939; Running Locally
Preparation:
1. Setup a virtual environment (conda, venv, etc).
2. Run `pip install -r requirements.txt` to install necessary packages.
3. Create an _env file_ named `.env` in the project root path and add the following environment variables:
   ```
    ACCESS_TOKEN_SECRET_KEY
    ACCESS_TOKEN_VALIDITY_MINUTES

    DB_NAME
    DB_HOST
    DB_PORT
    DB_USERNAME
    DB_PASSWORD
   ```

Running:
1. Run service with `uvicorn app.main:app --reload`.
2. Run tests with `to be configured`.
3. Check code style with `flake8`.
4. Check for static typing with `mypy .`.
