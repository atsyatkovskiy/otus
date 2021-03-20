import pytest
from unittest.mock import Mock, patch
from methods import APIClient


# Positive, GET posts/1
@patch('methods.APIClient.get')
@pytest.mark.parametrize('input_id', [1, 55, 33])
def test_posts_get(mock_request, api_client, input_id):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {'id': input_id}
    res = APIClient.get(api_client, "/posts/" + str(input_id))
    assert res.json()['id'] == int(input_id)
    assert res.status_code == 200, "Status code is not 200"


# Positive, Get Brewery
# https://api.openbrewerydb.org/breweries/5494
@patch('methods.APIClient.get')
@pytest.mark.parametrize('input_id_brewery', [100, 432, 551, 1012])
def test_breweries_get(mock_request, api_client, input_id_brewery):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {'id': input_id_brewery}
    res = APIClient.get(api_client, "/breweries/" + str(input_id_brewery))
    assert res.json()["id"] == input_id_brewery
    assert res.status_code == 200


# Get Brewery, no valid id
# https://api.openbrewerydb.org/breweries/5494
@patch('methods.APIClient.get')
@pytest.mark.parametrize('input_id_brewery', [-100, 444432, "&", 0])
def test_breweries_no_valid_get(mock_request, api_client, input_id_brewery):
    data = {"message": f"Couldn't find Brewery with 'id'={input_id_brewery}"}
    mock_request.return_value = Mock(status_code=404)
    mock_request.return_value.json.return_value = data
    res = APIClient.get(api_client, "/breweries/" + str(input_id_brewery))
    assert res.json() == data
    assert res.status_code == 404


# Filter breweries by name, Get
# https://api.openbrewerydb.org/breweries?by_name=cooper
@pytest.mark.parametrize('by_name', ['moscow', 'cooper'])
@patch('methods.APIClient.get')
def test_filter_name_get(mock_request, api_client, by_name):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {'name': by_name}
    res = APIClient.get(api_client, path="/breweries/", params={'by_name': by_name})
    assert res.json()["name"] == str(by_name)
    assert res.status_code == 200


# Filter by type of brewery, Get
# https://api.openbrewerydb.org/breweries?by_type=micro
@patch('methods.APIClient.get')
@pytest.mark.parametrize('by_type', ['micro', 'regional', 'brewpub', 'large',
                                     'planning', 'contract', 'proprietor'])
def test_filter_type_get(mock_request, api_client, by_type):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {'brewery_type': by_type}
    res = APIClient.get(api_client, path="/breweries", params={'brewery_type': by_type})
    assert res.json()["brewery_type"] == str(by_type)
    assert res.status_code == 200


# Number of breweries to return each call, Get
# https://api.openbrewerydb.org/breweries?per_page=25
@patch('methods.APIClient.get')
@pytest.mark.parametrize('per_page', [20, 25, 44])
def test_posts2_get(mock_request, api_client, per_page):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = per_page
    res = APIClient.get(api_client, path="/breweries", params={'per_page': per_page})
    assert res.json() == per_page
    assert res.status_code == 200
