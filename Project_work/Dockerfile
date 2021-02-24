# Устанавливаю базовый образ
FROM python:3.8

# Устанавливаю рабочую директорию внутри контейнера
# Директория будет создана если её не было
# Будет в дальнейшем использоваться, как базовая (основная)
WORKDIR /app

# Копирую сначала зависимости
# Для того чтобы не пересобирать их каждый раз при сборке
COPY requirements.txt .

# Выполняю необходимые команды
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN export PYTHONPATH=/app/

# Копирую остальные файлы проекта в /app
COPY . .

# Предустанавливаем команду pytest и отчёт
ENTRYPOINT ["pytest", "--alluredir", "allure-report"]

# Этот параметр можно переопределить при СОЗДАНИИ контейнера т.е. run команде
# Можно исапользовать так `docker run --rm my_tests --browser firefox`
CMD ["--browser", "chrome"]
