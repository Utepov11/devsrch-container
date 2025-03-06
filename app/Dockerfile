# Используем официальный минимальный образ Python
FROM python:3.9.6-alpine

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем системные зависимости
RUN apk update && apk add --no-cache \
      gcc \
      musl-dev \
      mariadb-dev \
      libffi-dev \
      curl \
      python3-dev \
      py3-pip \
      build-base

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Открываем порт (если приложение слушает, например, 8000)
EXPOSE 8000
