# coding: utf-8

import requests
from .common import URL, TIMEOUT, get_tasks


def test_pos_get_task():
    tasks = get_tasks()
    tasks_id = tasks[0]['id']

    url = '%s/task/get/%s' % (URL, tasks_id)

    response = requests.get(url=url, timeout=TIMEOUT)

    assert response.status_code == 200 and 'result' in response.json(), 'Incorrect getting task'


def test_neg_get_task():
    for value in ['test', None]:
        url = '%s/task/get/%s' % (URL, value)
        response = requests.get(url=url, timeout=TIMEOUT)

        assert response.status_code == 404, 'Incorrect getting task(negative case)'

    url = '%s/task/get/%d' % (URL, 0)
    response = requests.get(url=url, timeout=TIMEOUT)

    assert response.status_code == 400, 'Incorrect getting task(negative case)'
