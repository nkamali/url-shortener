# Navid's Url Shortener Service

The Url Shortener Service is a simple RESTful service that shortens long URLs. This project is built with FastAPI, SQLAlchemy, and SQLite.

## Prerequisites

Python 3.11 or higher
Docker and Docker-Compose
Getting Started
Clone the repository:

```
git clone https://github.com/nkamali/url-shortener.git
cd url-shortener
```

## Install dependencies locally:

See below if you like to install this service within a docker container instead.

```
pip install -r requirements.txt
```

Create an .env file for environment variables in your server. For example:

```
DATABASE_URL=sqlite:///:memory:
```

## Running the Application

To run the application locally. See below if you like to install this service within a docker container instead.

```
uvicorn main:app --reload
```

The application will be available at http://localhost:8000. The interactive OpenAPI documentation will be available at http://localhost:8000/docs.

## To install and run the application with Docker:

This will also download the docker image and install everything within a docker container.

`docker-compose up --build`

The application will be available at http://localhost:8000. The interactive OpenAPI documentation will be available at http://localhost:8000/docs.

![Screenshot](https://github.com/nkamali/url-shortener/blob/main/Screen%20Shot%202023-07-12%20at%2011.06.42%20PM.png)

## Project Structure

The project's structure is as follows:

```
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── models.py
|   |   ├── types.py
│   │   └── session.py
│   ├── main.py
│   └── services
│       ├── __init__.py
│       └── url_service.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Built With

FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
SQLAlchemy: The Python SQL Toolkit and Object-Relational Mapper that gives application developers the full power and flexibility of SQL.
SQLite: A C library that provides a lightweight disk-based database.

## Contributing

We love contributions! Please feel free to submit pull requests.

## License

This project is licensed under the terms of the MIT license. See LICENSE for more details.

## Contact

Navid Kamali - navidgems at gmail dot com

Project Link: https://github.com/nkamali/url-shortener
