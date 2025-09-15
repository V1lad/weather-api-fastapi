FROM python:3.11.6-slim

# Предотвращает создание .pyc-файлов
ENV PYTHONDONTWRITEBYTECODE 1

# Обеспечивает вывод в терминал
ENV PYTHONUNBUFFERED 1

# Зеркала для debian
RUN echo 'deb http://mirror.yandex.ru/debian/ bookworm main contrib non-free non-free-firmware deb-src http://mirror.yandex.ru/debian/ bookworm main contrib non-free non-free-firmware deb http://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware deb-src http://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware deb http://mirror.yandex.ru/debian/ bookworm-updates main contrib non-free non-free-firmware deb-src http://mirror.yandex.ru/debian/ bookworm-updates main contrib non-free non-free-firmware' > /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3-dev gcc libpq-dev
RUN apt-get clean
RUN  rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Установка python зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

# Перенос необходимых файлов в контейнер
COPY app/ ./app/
COPY alembic/ ./alembic/
COPY alembic.ini .

# Команда для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]