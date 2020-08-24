import random
import pytest
import cerberus
from jsonschema import validate


# Get Brewery
# https://api.openbrewerydb.org/breweries/5494
@pytest.mark.parametrize('input_id_brewery', [100, 432, 551, 1012])
#@pytest.mark.parametrize('input_id_brewery, output_id_brewery', [("100", '100'), ("55", '55'), ("2121", '2121')])
def test_posts_get(api_client, input_id_brewery):
#def test_get_brewery(api_client, id_brewery):
    # response = api_client.get(path="/breweries/", params={'id': input_id_brewery})
    response = api_client.get("/breweries/" + str(input_id_brewery))
    # print(response)
    # print(len(response.json()))
    print(response.json())
    print(input_id_brewery)
    assert response.json()["id"] == input_id_brewery
    # print(response.text)
    # print(response.status_code)
    # print(response.json()["examples"])
    assert response.status_code == 200
    # assert response.json()["status"] == "success"
    # validate(instance=response.json(), schema=schema)


# Search, Get Brewery (проверка поиска по значению)
# https://api.openbrewerydb.org/breweries/search?query=dog
@pytest.mark.parametrize('input_value', ["Colorado", "California"])
def test_posts_get(api_client, input_value):
    response = api_client.get("/breweries/search?query=" + str(input_value))
    # print(response)
    # print(len(response.json()))
    print(response.json())
    print(input_value)
    # assert response.json()["id"] == input_id_brewery
    # print(response.text)
    # print(response.status_code)
    assert response.status_code == 200
    # validate(instance=response.json(), schema=schema)

# def test_list_all_get(api_client):
#     response = api_client.get("/breweries?by_city=san_diego")
#     print(response.text)
#     #    print(response.status_code)
#     #    print(response.json()["examples"])
#     assert response.status_code == 200
# #    assert response.json()["status"] == "success"
# #    validate(instance=response.json(), schema=schema)
#
#
# def test_random_image_get(api_client):
#     ran = random.randint(1, 50)
#     response = api_client.get("/breeds/image/random/" + str(ran))
#     data = response.json()['message']
#     count_message = 0
#     for i in data:
#         count_message += 1
#     print("Число картинок =", count_message, "число рандом =", ran)
#     assert count_message == ran
#     assert response.status_code == 200
#     assert response.json()["status"] == "success"
#     validate(instance=response.json(), schema=schema)
#
#
# def test_random_image_breed_get(api_client):
#     ran = random.randint(1, 100)
#     response = api_client.get("/breed/hound/images/random/" + str(ran))
#     data = response.json()['message']
#     count_message = 0
#     for i in data:
#         count_message += 1
#         print(count_message, i)
#     print("Число картинок =", count_message, "число рандом =", ran)
#     assert count_message == ran
#     assert response.status_code == 200
#     assert response.json()["status"] == "success"
#     validate(instance=response.json(), schema=schema)
#
#
# def test_list_sub_breed_get(api_client):
#     response = api_client.get("/breed/hound/list/")
#     data = response.json()
#     count_message = 0
#     for i in data['message']:
#         count_message += 1
#         print(count_message, i, type(i))
#     print("Число =", count_message)
#     assert response.status_code == 200
#     assert response.json()["status"] == "success"
#     validate(instance=response.json(), schema=schema)
#
#
# def test_random_afgan_get(api_client):
#     response = api_client.get("/breed/hound/afghan/images/random")
#     data = response.json()
#     assert response.status_code == 200
#     assert response.json()["status"] == "success"
#     validate(instance=response.json(), schema=schema)

# schema = {
#     "name": {"type": "string", "required": True},
#     "surname": {"type": "string", "required": True},
#     "grade": {"type": "number", "required": True}
# }

# schema = {
#     "type": "object",
#     "message": {"type": "string"},
#     "status": {"type": "string"},
#     "required": ["message", "status"]
# }

# schema = {
#     "type": "object",
#     "properties": {
#         "id": {"type": "integer"},
#         "name": {"type": "string"},
#         "brewery_type": {"type": "string"},
#         "street": {"type": "string"},
#         "city": {"type": "string"},
#         "state": {"type": "string"},
#         "postal_code": {"type": "string"},
#         "country": {"type": "string"},
#         "longitude": {"type": "string"},
#         "latitude": {"type": "string"},
#         "phone": {"type": "string"},
#         "website_url": {"type": "string"},
#         "updated_at": {"type": "string"},
#     },
#     "required": [
#         "id",
#         "name",
#         "brewery_type",
#         "street",
#         "city",
#         "state",
#         "postal_code",
#         "country",
#         "longitude",
#         "latitude",
#         "phone",
#         "website_url",
#         "updated_at"
#     ]
# }
