FROM python:3.12

# Устанавливаем зависимости
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Копируем исходный код
COPY . /app

# Запускаем тесты
CMD ["sh", "autotests.sh"]
