# Используем минимальный образ Python
FROM python:3.12.8-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для psycopg2
RUN apk update && apk add --no-cache \
    postgresql-dev gcc python3-dev musl-dev

# Устанавливаем pip-зависимости
COPY devsearch/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY devsearch /app

# Указываем команду запуска Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
