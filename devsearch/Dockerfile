# Используем минимальный образ Python
FROM python:3.12.8-alpine

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

COPY ./requirements.txt .

# Устанавливаем pip-зависимости
RUN apt-get update && \
    apt-get install -y \
      gcc \
      default-libmysqlclient-dev \
      pkg-config \
      curl && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y \
      gcc \
      pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000
