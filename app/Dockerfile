# Используем минимальный образ Python
FROM python:3.12.8-alpine

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

COPY ./requirements.txt .

# Устанавливаем зависимости
RUN apk add --no-cache \
      gcc \
      musl-dev \
      mariadb-connector-c-dev \
      libffi-dev \
      curl && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del \
      gcc \
      musl-dev \
      mariadb-connector-c-dev \
      libffi-dev

COPY . .

EXPOSE 8000
