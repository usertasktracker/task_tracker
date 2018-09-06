# coding: utf-8

import requests
from .common import URL, TIMEOUT, check_int_fields, get_tasks


def test_pos_delete_task():
    url = '%s/task/delete' % URL

    params = {'task_id': get_tasks()[0]['id']}

    response = requests.post(url=url, data=params, timeout=TIMEOUT)

    assert response.status_code == 200 and response.json() == {"result": "ok"}, 'Incorrect deleting task 1'


def test_neg_delete_task():
    error = 'Incorrect deleting task (negative case)'
    url = '%s/task/delete' % URL

    params = {'task_id': 1}

    check_int_fields(url, params, ['task_id'], error)
