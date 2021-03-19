import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_url + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_url + str(path)
        resp = requests.get(url=url, params=params)
        # return requests.get(url=url, params=params)
        return resp.json()

    def delete(self, path="/", params=None):
        url = self.base_url + path
        return requests.delete(url=url, params=params)