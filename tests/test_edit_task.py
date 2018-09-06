# coding: utf-8

import requests
from .common import URL, TIMEOUT, check_int_fields, check_str_fields, get_tasks, get_users


def test_pos_edit_task():
    url = '%s/task/edit' % URL

    users = get_users()
    user_id = users[0]['id']

    tasks = get_tasks()
    tasks_id = tasks[0]['id']

    params = {
        'status': 'closed',
        'assignee_id': user_id,
        'task_id': tasks_id,
    }
    response = requests.post(url=url, data=params, timeout=TIMEOUT)

    assert response.status_code == 200 and response.json() == {"result": "ok"}, 'Incorrect editing task 1'

    params = {
        'status': 'open',
        'assignee_id': None,
        'task_id': tasks_id,
    }
    response = requests.post(url=url, data=params, timeout=TIMEOUT)

    assert response.status_code == 200 and response.json() == {"result": "ok"}, 'Incorrect editing task 2'


def test_neg_edit_task():
    users = get_users()
    user_id = users[0]['id']

    tasks = get_tasks()
    tasks_id = tasks[0]['id']

    error = 'Incorrect editing task (negative case)'
    url = '%s/task/edit' % URL

    params = {
        'status': 'closed',
        'assignee_id': user_id,
        'task_id': tasks_id,
    }

    check_str_fields(url, params, ['status'], error)
    check_int_fields(url, params, ['assignee_id', 'task_id'], error)
