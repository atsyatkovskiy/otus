from subprocess import Popen, PIPE, STDOUT
from conftest import ssh_connect, ssh_close


def exec_command(command):
    exec_command_get_id = Popen \
        (command, shell=True, stdout=PIPE, stderr=STDOUT)
    result_command = (exec_command_get_id.communicate()[0]).decode()
    return result_command


# Функция получения времени старта контейнера
def get_time_started_container(name_container):

    # Получаем id контейнера по name
    get_container_id = f"docker ps -aqf 'name={name_container}'"
    container_id = exec_command(get_container_id)
    print("ID контейнера: ", container_id)

    # Получаем время запуска по id контейнера
    get_time_started_docker = "docker inspect --format='{{.State.StartedAt}}' " + container_id
    time_started_container = exec_command(get_time_started_docker)
    print("Время запуска контейнера: ", time_started_container)
    return time_started_container


def test_restart_opencart(param_name_opencart):

    # Выполняем подключеение по ssh
    ssh_connect()

    # Получаем время запуска контейнера до рестарта
    time_before = get_time_started_container(param_name_opencart)

    # Делаем рестарт сервиса
    restart_docker = f"docker container restart {param_name_opencart}"
    exec_command(restart_docker)

    # Получаем время запуска контейнера после рестарта
    time_after = get_time_started_container(param_name_opencart)

    # Сравниваем время запуска ДО и ПОСЛЕ restart
    assert time_before != time_after
    ssh_close()


def test_restart_db(param_name_db):

    # Выполняем подключеение по ssh
    ssh_connect()

    # Получаем время запуска контейнера до рестарта
    time_before = get_time_started_container(param_name_db)

    # Делаем рестарт сервиса
    restart_docker = f"docker container restart {param_name_db}"
    exec_command(restart_docker)

    # Получаем время запуска контейнера после рестарта
    time_after = get_time_started_container(param_name_db)

    # Сравниваем время запуска ДО и ПОСЛЕ restart
    assert time_before != time_after
    ssh_close()