# coding: utf-8

import requests
from .common import URL, TIMEOUT


def test_pos_create_users():
    url = '%s/user/create' % URL

    for i in range(5):
        params = {'name': 'user %d' % i}
        response = requests.post(url=url, data=params, timeout=TIMEOUT)

        assert response.status_code == 200 and response.json() == {"result": "ok"}, 'Incorrect creating user'
