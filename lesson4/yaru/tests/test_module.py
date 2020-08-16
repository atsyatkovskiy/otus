
def test_url_status(url, status, method):  # функция принимает два параметра из фикстур
    response = method(url)
    # print("status = ", status, "type =", type(status))
    print("status response = ", response.status_code, "type response =", type(response.status_code))
    assert response.status_code == int(status)
