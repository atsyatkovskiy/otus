import random
import pytest


# Get Brewery
# https://api.openbrewerydb.org/breweries/5494
@pytest.mark.parametrize('input_id_brewery', [100, 432, 551, 1012])
def test_breweries_get(api_client, input_id_brewery):
    response = api_client.get("/breweries/" + str(input_id_brewery))
    assert response.json()["id"] == input_id_brewery
    assert response.status_code == 200


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
    resp_json = response.json()
    for list_ in resp_json:
        name_value = list_["name"]
        print(name_value.lower())
        assert by_name in name_value.lower()
    assert response.status_code == 200


# Filter by type of brewery, Get
# https://api.openbrewerydb.org/breweries?by_type=micro
@pytest.mark.parametrize('by_type', ['micro', 'regional', 'brewpub', 'large',
                                     'planning', 'contract', 'proprietor'])
def test_filter_type_get(api_client, by_type):
    response = api_client.get(path="/breweries",
                              params={'by_type': by_type})
    random_num = random.randint(1, 5)
    assert response.json()[random_num]["brewery_type"] == str(by_type)
    assert response.status_code == 200


# Number of breweries to return each call, Get
# https://api.openbrewerydb.org/breweries?per_page=25
@pytest.mark.parametrize('per_page', [20, 25, 44])
def test_posts2_get(api_client, per_page):
    response = api_client.get(path="/breweries",
                              params={'per_page': per_page})
    resp_json = response.json()
    assert len(resp_json) == per_page
