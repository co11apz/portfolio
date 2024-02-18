# Используйте базовый образ Python
FROM python:3.12

# Установите рабочую директорию в /app
WORKDIR /app

# Скопируйте файл зависимостей в текущую директорию
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте текущий каталог (включая все файлы) в образ в /app
COPY . /app

# Определите команду, которая будет выполняться при запуске контейнера
CMD ["python", "app.py"]
