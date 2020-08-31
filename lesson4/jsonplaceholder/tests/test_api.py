import pytest
import pprint


# Удалить ресурс, метод delete
# https://jsonplaceholder.typicode.com/posts
def test_api_delete(api_client):
    res = api_client.delete(path="/posts")
    # Проверка на пустой json
    pprint.pprint(res.json())
    assert res.json() == {}


# Получение ресурса, метод get
# https://jsonplaceholder.typicode.com/posts/1
@pytest.mark.parametrize('input_id, output_id', [(1, '1'), (55, '55'), (33, '33')])
def test_posts_get(api_client, input_id, output_id):
    response = api_client.get(path="/posts",
                              params={'id': input_id})
    res_json = response.json()
    assert res_json[0]['id'] == int(output_id)
    assert response.status_code == 200


# Получение всех ресурсов, метод get
# https://jsonplaceholder.typicode.com/posts
@pytest.mark.parametrize('all_posts', [(100)])
def test_post_get_all(api_client, all_posts):
    response = api_client.get(path="/posts")
    res_json = response.json()
    assert len(res_json) == all_posts


# Создание ресурса, метод post
# https://jsonplaceholder.typicode.com/posts
@pytest.mark.parametrize('input_userid, output_userid', [(5, '5'), (-1, '-1'), (0, '0')])
@pytest.mark.parametrize('input_title, output_title', [('test Title', 'test Title'), (100, '100'), ('-', '-')])
def test_api_post_request(api_client, input_userid, output_userid, input_title, output_title):
    res = api_client.post(path="/posts",
                          data={'title': input_title, 'body': 'bar', 'userId': input_userid})
    res_json = res.json()
    pprint.pprint(res_json)
    assert res_json['title'] == output_title
    assert res_json['body'] == 'bar'
    assert res_json['userId'] == output_userid
    assert (res.headers['content-type']) == "application/json; charset=utf-8"


# Параметр фильтрации фото по Id альбома
# https://jsonplaceholder.typicode.com/photos?albumId=1
@pytest.mark.parametrize('albumid', [101, 0, -6, 273])
def test_api_empty_response(api_client, albumid):
    res = api_client.get(path="/photos", params={'albumId': albumid})
    # Проверяем что на таких данных нет, ответ пустой
    assert res.json() == []
