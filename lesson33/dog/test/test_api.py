import pytest
from unittest.mock import Mock, patch
from methods import APIClient


# Positive, LIST ALL BREEDS, GET
# https://dog.ceo/api/breeds/list/all
@patch('methods.APIClient.get')
def test_list_all_get(mock_request, api_client):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {"status": "success"}
    res = APIClient.get(api_client, "/breeds/list/all")
    assert res.status_code == 200
    assert res.json()["status"] == "success"


# Positive, DISPLAY MULTIPLE RANDOM IMAGES FROM ALL DOGS COLLECTION, GET
# https://dog.ceo/api/breeds/image/random/5
@patch('methods.APIClient.get')
@pytest.mark.parametrize('input_num', [2])
def test_random_image_get(mock_request, api_client, input_num):
    data_json = {
        "message": [
            "https://images.dog.ceo/breeds/pomeranian/n02112018_863.jpg",
            "https://images.dog.ceo/breeds/finnish-lapphund/mochilamvan.jpg"
        ],
        "status": "success"
    }
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = data_json
    res = APIClient.get(api_client, "/breeds/list/all/" + str(input_num))
    assert len(res.json()['message']) == int(input_num)
    assert res.status_code == 200
    assert res.json()["status"] == "success"


# Positive, MULTIPLE IMAGES FROM A BREED COLLECTION, GET
# https://dog.ceo/api/breed/hound/images/random/3
@patch('methods.APIClient.get')
@pytest.mark.parametrize('input_num', [2])
def test_random_image_breed_get(mock_request, api_client, input_num):
    data_json = {
        "message": [
            "https://images.dog.ceo/breeds/hound-ibizan/n02091244_1917.jpg",
            "https://images.dog.ceo/breeds/hound-ibizan/n02091244_3320.jpg"
        ],
        "status": "success"
    }
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = data_json
    res = APIClient.get(api_client, "/breed/hound/images/random/" + str(input_num))
    assert len(res.json()['message']) == int(input_num)
    assert res.status_code == 200
    assert res.json()["status"] == "success"


# Positive, LIST ALL SUB-BREEDS, GET
# https://dog.ceo/api/breed/hound/list
@patch('methods.APIClient.get')
def test_list_sub_breed_get(mock_request, api_client):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {"status": "success"}
    res = APIClient.get(api_client, "/breed/hound/list/")
    assert res.status_code == 200
    assert res.json()["status"] == "success"


# Positive, RANDOM IMAGES FROM BREEDS LIST
# https://dog.ceo/api/breed/hound/afghan/images/random
@patch('methods.APIClient.get')
@pytest.mark.parametrize('hound', ["afghan", "basset", "blood"])
def test_random_afgan_get(mock_request, api_client, hound):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {"status": "success"}
    res = APIClient.get(api_client, "/breed/hound/" + hound + "/images/random")
    assert res.status_code == 200
    assert res.json()["status"] == "success"

