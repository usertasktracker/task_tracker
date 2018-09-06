# coding: utf-8

import requests
from .common import URL, TIMEOUT, check_int_fields, check_str_fields, get_tasks


def test_pos_add_comment():
    url = '%s/task/add_comment' % URL

    params = {
        'comment': 'My comment',
        'task_id': get_tasks()[0]['id'],
    }
    response = requests.post(url=url, data=params, timeout=TIMEOUT)

    assert response.status_code == 200 and response.json() == {"result": "ok"}, 'Incorrect adding comment'


def test_neg_add_comment():
    error = 'Incorrect adding comment (negative case)'
    url = '%s/task/add_comment' % URL

    params = {
        'comment': 'My comment',
        'task_id': 2,
    }

    check_str_fields(url, params, ['comment'], error)
    check_int_fields(url, params, ['task_id'], error)
