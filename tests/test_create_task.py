# coding: utf-8

import requests
from .common import URL, TIMEOUT, check_int_fields, check_str_fields, get_users, get_projects


def test_pos_create_task():
    url = '%s/task/create' % URL

    users = get_users()
    user_id_one = users[0]['id']
    user_id_two = users[1]['id']

    projects = get_projects()
    project_id = projects[0]['id']

    params = {
        'name': 'task 1',
        'status': 'active',
        'assignee_id': user_id_one,
        'reporter_id': user_id_one,
        'project_id': project_id,
        'description': 'this is first task',
    }

    response = requests.post(url=url, data=params, timeout=TIMEOUT)
    assert response.status_code == 200 and response.json() == {"result": "ok"}, 'Incorrect creating task 1'

    params = {
        'name': 'task 2',
        'status': 'active',
        'assignee_id': None,
        'reporter_id': user_id_two,
        'project_id': user_id_two,
        'description': 'this is second task',
    }
    response = requests.post(url=url, data=params, timeout=TIMEOUT)

    assert response.status_code == 200 and response.json() == {"result": "ok"}, 'Incorrect creating task 2'


def test_neg_create_task():
    users = get_users()
    user_id = users[0]['id']

    projects = get_projects()
    project_id = projects[0]['id']

    error = 'Incorrect creating task (negative case)'
    params = {
        'name': 'task',
        'status': 'active',
        'assignee_id': user_id,
        'reporter_id': user_id,
        'project_id': project_id,
        'description': 'this is incorrect task',
    }
    url = '%s/task/create' % URL

    check_str_fields(url, params, ['name', 'status', 'description'], error)
    check_int_fields(url, params, ['assignee_id', 'reporter_id', 'project_id'], error)
