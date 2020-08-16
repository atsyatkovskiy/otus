import random
import cerberus
from jsonschema import validate


def test_list_all_get(api_client):
    response = api_client.get("/breweries?by_city=san_diego")
    print(response.text)
    #    print(response.status_code)
    #    print(response.json()["examples"])
    assert response.status_code == 200
#    assert response.json()["status"] == "success"
#    validate(instance=response.json(), schema=schema)


def test_random_image_get(api_client):
    ran = random.randint(1, 50)
    response = api_client.get("/breeds/image/random/" + str(ran))
    data = response.json()['message']
    count_message = 0
    for i in data:
        count_message += 1
    print("Число картинок =", count_message, "число рандом =", ran)
    assert count_message == ran
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    validate(instance=response.json(), schema=schema)


def test_random_image_breed_get(api_client):
    ran = random.randint(1, 100)
    response = api_client.get("/breed/hound/images/random/" + str(ran))
    data = response.json()['message']
    count_message = 0
    for i in data:
        count_message += 1
        print(count_message, i)
    print("Число картинок =", count_message, "число рандом =", ran)
    assert count_message == ran
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    validate(instance=response.json(), schema=schema)


def test_list_sub_breed_get(api_client):
    response = api_client.get("/breed/hound/list/")
    data = response.json()
    count_message = 0
    for i in data['message']:
        count_message += 1
        print(count_message, i, type(i))
    print("Число =", count_message)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    validate(instance=response.json(), schema=schema)

def test_random_afgan_get(api_client):
    response = api_client.get("/breed/hound/afghan/images/random")
    data = response.json()
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    validate(instance=response.json(), schema=schema)

# schema = {
#     "name": {"type": "string", "required": True},
#     "surname": {"type": "string", "required": True},
#     "grade": {"type": "number", "required": True}
# }

schema = {
    "type": "object",
    "message": {"type": "string"},
    "status": {"type": "string"},
    "required": ["message", "status"]
}

