import random
import pytest
from jsonschema import validate


# LIST ALL BREEDS, GET
# https://dog.ceo/api/breeds/list/all
def test_list_all_get(api_client):
    response = api_client.get("/breeds/list/all")
    # print(response.text)
    # print("status = ", response.status_code)
    # print(response.json()["message"])
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    validate(instance=response.json(), schema=schema)


# DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION, GET
# https://dog.ceo/api/breeds/image/random/5
@pytest.mark.parametrize('input_num, output_num', [(5, '5'), (10, '10'), (15, '15')])
def test_random_image_get(api_client, input_num, output_num):
    response = api_client.get("/breeds/image/random/" + str(input_num))
    print(response.json())
    assert len(response.json()['message']) == int(output_num)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    validate(instance=response.json(), schema=schema)


# MULTIPLE IMAGES FROM A BREED COLLECTION, GET
# https://dog.ceo/api/breed/hound/images/random/3
@pytest.mark.parametrize('input_num, output_num', [(3, '3'), (9, '9'), (20, '20')])
def test_random_image_breed_get(api_client, input_num, output_num):
    response = api_client.get("/breed/hound/images/random/" + str(input_num))
    assert len(response.json()['message']) == int(output_num)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    validate(instance=response.json(), schema=schema)


# LIST ALL SUB-BREEDS, GET
# https://dog.ceo/api/breed/hound/list
def test_list_sub_breed_get(api_client):
    response = api_client.get("/breed/hound/list/")
    # data = response.json()
    # count_message = 0
    # for i in data['message']:
    #     count_message += 1
    #     print(count_message, i, type(i))
    # print("Число =", count_message)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    validate(instance=response.json(), schema=schema)


# RANDOM IMAGES FROM BREEDS LIST
# https://dog.ceo/api/breed/hound/afghan/images/random
@pytest.mark.parametrize('hound', ["afghan", "basset", "blood"])
def test_random_afgan_get(api_client, hound):
    response = api_client.get("/breed/hound/" + hound + "/images/random")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


schema = {
    "type": "object",
    "message": {"type": "string"},
    "status": {"type": "string"},
    "required": ["message", "status"]
}
