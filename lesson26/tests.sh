#!/bin/bash

# Собираем (создаем) image с тегом my_tests
# image от python:3.8
# "-t" тег
docker build -t my_tests .

# Запускаем контейнер под именем my_run из image my_tests
#docker run --name my_run my_tests --browser opera -n 2
docker run --name my_run my_tests --browser chrome

# Копируем из контейнера созданный allure-report
docker cp my_run:/app/allure-report .

# Запускаем хост для отчёта аллюр (утилита лежит локально)
# Хост отчёта нужно будет остановить руками
# Ссылка на allure должна быть своя
allure serve allure-report

# Удаляем из системы созданный контейнер
docker system prune -f