# coding: utf-8
from django.conf.urls import url, include

from task_tracker.project import views as project_views
from task_tracker.user import views as user_views
from task_tracker.task import views as task_views

urlpatterns = [
    # Пользователь
    url(r'^user/', include([
        url(r'^create$', user_views.create_user),
        url(r'^get_all$', user_views.get_all_users),
    ])),

    # Проект
    url(r'^project/', include([
        url(r'^create$', project_views.create_project),
        url(r'^get_all$', project_views.get_all_projects),
    ])),

    # Задача
    url(r'^task/', include([
        url(r'^create$', task_views.create_task),
        url(r'^edit$', task_views.edit_task),
        url(r'^delete$', task_views.delete_task),
        url(r'^add_comment$', task_views.add_comment),
        url(r'^get_all$', task_views.get_all_tasks),
        url(r'^get/(?P<task_id>\d+)$', task_views.get_task),
    ])),
]
