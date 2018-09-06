# coding: utf-8
from copy import deepcopy

import requests


URL = 'http://localhost:8000'
TIMEOUT = 120


def check_str_fields(url, default_params, fields, error):
    for field in fields:
        for value in ['test'*1025, None]:
            params = deepcopy(default_params)
            params[field] = value
            response = requests.post(url=url, data=params, timeout=TIMEOUT)

            assert response.status_code == 400 and 'error' in response.json(), error


def check_int_fields(url, default_params, fields, error):
    for field in fields:
        for value in ['test', 0, None]:
            if field == 'assignee_id' and value is None:
                continue
            params = deepcopy(default_params)
            params[field] = value
            response = requests.post(url=url, data=params, timeout=TIMEOUT)

            assert response.status_code == 400 and 'error' in response.json(), error


def get_projects():
    url = '%s/project/get_all' % URL
    response = requests.get(url=url, timeout=TIMEOUT)
    return response.json()['result']


def get_users():
    url = '%s/user/get_all' % URL
    response = requests.get(url=url, timeout=TIMEOUT)
    return response.json()['result']


def get_tasks():
    url = '%s/task/get_all' % URL
    response = requests.get(url=url, timeout=TIMEOUT)
    return response.json()['result']
