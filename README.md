# fastapi-postgresql-crud
Async CRUD API using FastAPI, PostgreSQL, and SQLAlchemy.
# FastAPI PostgreSQL CRUD

Asynchronous CRUD API built with FastAPI, PostgreSQL, SQLAlchemy Async ORM, and Repository Pattern.

## Features

- Create Student
- Get Student by ID
- Get All Students
- Update Student
- Delete Student

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (Async)
- Pydantic
- Uvicorn

## Project Structure

app/
├── db/
├── models/
├── repositories/
├── routers/
└── schemas/

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /students | Create Student |
| GET | /students | Get All Students |
| GET | /students/{id} | Get Student |
| PUT | /students/{id} | Update Student |
| DELETE | /students/{id} | Delete Student |
