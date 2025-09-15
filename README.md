# weather-api-fastapi
FastAPI-приложение для запросов информации о погоде с интеграцией OpenWeatherMap и отслеживанием истории запросов с сохранением в БД. Приложение готово к развёртыванию и использованием Docker-compose. В приложении используется СУБД Postgres15, в качестве ORM выступает SQLAlchemy. Работа с миграциями осуществляется при помощи Alembic. 

[![Python Version](https://img.shields.io/badge/python-3.11.6-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# Технологический стек
- FastAPI 0.116.1
- Pydantic 2.11.7
- SQLAlchemy 2.0.43
- Alembic 1.16.5
- Pytest 8.4.2
- Docker Compose

# Быстрый старт
```bash
git clone https://github.com/V1lad/weather-api-fastapi.git
```

После необходимо создать файл окружения
```env
OPENWEATHER_API_KEY=<Ключ API>
ENVIRONMENT=<development/deployment>
POSTGRES_USER=<user_name>
POSTGRES_PASSWORD=<user_password>
POSTGRES_DB=<db_name>
```

Запуск и сборка контейнеров осуществляется следующей командой
```bash
docker-compose up --build
```

Приложение будет доступно по адресу: http://localhost:8000

# Ручная установка для разработки

Установка зависимостей с тестированием
```bash
pip install -r requirements-tesing.txt
```

Применение миграций
```bash
alembic upgrade head
```

Запуск приложения для отладки
```bash
uvicorn app.main:app --reload
```
## Дополнительные команды
Создание новой миграции
```bash
alembic revision --autogenerate -m "database creation"
```

Запуск тестов
```bash
pytest
```

# API Endpoints

**POST /api/v1/weather** - Получение температуры по ширине и долготе.

## Формат запроса 
```json
{
  "lat": -90 < FLOAT < 90,
  "lon": -180 < FLOAT < 180>
}
```
## Формат ответа

Status Code: 200 OK
```json
{
  "temperature": FLOAT
}
```

## Пример запроса

HTTPie
```bash
http POST localhost:8000/api/v1/weather --raw '{"lat": -20, "lon": 90}'
```

CURL
```bash
curl --request POST \
  --url http://localhost:8000/api/v1/weather \
  --header 'Content-Type: application/json' \
  --data '{"lat": -20, "lon": 90}'
```

## Возможные ошибки

Status Code: 400 Bad Request
```json
{
  "detail": "Incorrect data is provided"
}
```

422 Unprocessable Entity
```json
{
  "detail": [
    {
      "type": "json_invalid",
      "loc": [
        "body",
        8
      ],
      "msg": "JSON decode error",
      "input": {},
      "ctx": {
        "error": "Expecting value"
      }
    }
  ]
}
```