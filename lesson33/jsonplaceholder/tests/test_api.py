import pytest
from unittest.mock import Mock, patch
from methods import APIClient


# Positive, DELETE posts
@patch('methods.APIClient.delete')
# https://jsonplaceholder.typicode.com/posts
def test_api_delete(mock_request, api_client):
    mock_request.return_value = Mock(status_code=200)
    posts = {}
    mock_request.return_value.json.return_value = posts
    res = APIClient.delete(api_client, "/posts")
    assert res.json() == posts
    assert res.status_code == 200, "Status code is not 200"


# Positive, GET posts/1
@patch('methods.APIClient.get')
@pytest.mark.parametrize('input_id', [1, 55, 33])
def test_posts_get(mock_request, api_client, input_id):
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {'id': input_id}
    res = APIClient.get(api_client, "/posts" + str(input_id))
    assert res.json()['id'] == int(input_id)
    assert res.status_code == 200, "Status code is not 200"


# Positive, POST /posts
# https://jsonplaceholder.typicode.com/posts
@patch('methods.APIClient.post')
@pytest.mark.parametrize('input_userid ', [5, -1, 0])
@pytest.mark.parametrize('input_title', ['test Title', '100', '-'])
def test_api_post_request(mock_request, api_client, input_userid, input_title):
    data_json={'title': input_title, 'body': 'bar', 'userId': input_userid}
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = {'title': input_title, 'body': 'bar', 'userId': input_userid}
    res = APIClient.post(api_client, "/posts", data_json)
    assert res.json()['title'] == input_title
    assert res.json()['body'] == 'bar'
    assert res.json()['userId'] == input_userid
    assert res.status_code == 200, "Status code is not 200"


# Параметр фильтрации фото по Id альбома
# Positive, GET posts/1
# https://jsonplaceholder.typicode.com/photos?albumId=1
@patch('methods.APIClient.get')
@pytest.mark.parametrize('albumid', [101, 0, -6, 273])
def test_api_empty_response(mock_request, api_client, albumid):
    data_json = {'albumId': albumid}
    res_data = []
    mock_request.return_value = Mock(status_code=200)
    mock_request.return_value.json.return_value = res_data
    res = APIClient.get(api_client, "/posts", data_json)
    # Проверяем что на таких данных нет, ответ пустой
    assert res.status_code == 200, "Status code is not 200"
    assert res.json() == []