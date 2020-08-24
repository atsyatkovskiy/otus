import random
import pytest
import cerberus
from jsonschema import validate


# Get Brewery
# https://api.openbrewerydb.org/breweries/5494
@pytest.mark.parametrize('input_id_brewery', [100, 432, 551, 1012])
def test_breweries_get(api_client, input_id_brewery):
    response = api_client.get("/breweries/" + str(input_id_brewery))
    assert response.json()["id"] == input_id_brewery
    assert response.status_code == 200
    # assert response.json()["status"] == "success"
    # validate(instance=response.json(), schema=schema)


# Get Brewery, no valid id
# https://api.openbrewerydb.org/breweries/5494
@pytest.mark.parametrize('input_id_brewery', [-100, 444432, "&", 0])
def test_breweries_no_valid_get(api_client, input_id_brewery):
    response = api_client.get("/breweries/" + str(input_id_brewery))
    data = {"message": f"Couldn't find Brewery with 'id'={input_id_brewery}"}
    assert response.json() == data
    assert response.status_code == 404


# Filter breweries by name, Get
# https://api.openbrewerydb.org/breweries?by_name=cooper
@pytest.mark.parametrize('by_name', ['moscow', 'cooper'])
def test_filter_name_get(api_client, by_name):
    response = api_client.get(path="/breweries",
                              params={'by_name': by_name})
    # assert response.json()["id"] == input_id_brewery
    print(response.json())
    assert response.status_code == 200
    # assert response.json()["status"] == "success"
    # validate(instance=response.json(), schema=schema)


# Filter by type of brewery, Get
# https://api.openbrewerydb.org/breweries?by_type=micro
@pytest.mark.parametrize('by_type', ['micro', 'regional', 'brewpub', 'large',
                                     'planning', 'contract', 'proprietor'])
def test_posts2_get(api_client, by_type):
    response = api_client.get(path="/breweries",
                              params={'by_type': by_type})
    random_num = random.randint(1, 5)
    assert response.json()[random_num]["brewery_type"] == str(by_type)
    # assert response.status_code == 200
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
