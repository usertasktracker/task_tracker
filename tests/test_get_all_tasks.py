# coding: utf-8

import requests
from .common import URL, TIMEOUT, get_projects, get_users


def test_pos_get_all_tasks():
    url = '%s/task/get_all' % URL

    response = requests.get(url=url, timeout=TIMEOUT)
    assert response.status_code == 200 and 'result' in response.json(), 'Incorrect get all tasks'

    users = get_users()
    user_id_one = users[0]['id']
    user_id_two = users[1]['id']

    projects = get_projects()
    project_id = projects[0]['id']

    params = {
        'name': 'task 2',
        'status': 'active',
        'assignee_id': user_id_one,
        'reporter_id': user_id_two,
        'project_id': project_id,
        'description': 'this is second task',
    }
    for field, value in params.items():
        response = requests.get(url=url, params={field: value}, timeout=TIMEOUT)
        assert response.status_code == 200 and 'result' in response.json(), 'Incorrect get all tasks'


def test_neg_get_all_tasks():
    url = '%s/task/get_all' % URL

    for field in ['name', 'status', 'description']:
        response = requests.get(url=url, params={field: 'test'*1025}, timeout=TIMEOUT)
        assert response.status_code == 400 and 'error' in response.json(),\
            'Incorrect get all tasks (negative case)'

    for field in ['assignee_id', 'reporter_id', 'project_id']:
        for value in ['test'*1025, 0]:
            response = requests.get(url=url, params={field: value}, timeout=TIMEOUT)

            assert response.status_code == 400 and 'error' in response.json(),\
                'Incorrect get all tasks (negative case)'
