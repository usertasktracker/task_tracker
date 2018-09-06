#!/bin/bash

py.test -vs test_create_users.py \
test_create_projects.py \
test_create_task.py \
test_edit_task.py \
test_delete_task.py \
test_add_comment.py \
test_get_all_tasks.py \
test_get_task.py
