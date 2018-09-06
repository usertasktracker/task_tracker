# coding: utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db import transaction

from .models import Task, TaskDescription, TaskComment
from .forms import CreateTaskForm, EditTaskForm, OneTaskForm, AddCommentForm, TaskForm


@csrf_exempt
def create_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Request is not POST'}, status=400)

    form = CreateTaskForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    params = form.cleaned_data

    task_kwargs = {
        'name': params['name'],
        'status': params['status'],
        'assignee_id': params['assignee_id'],
        'reporter_id': params['reporter_id'],
        'project_id': params['project_id'],
    }

    with transaction.atomic():
        task = Task.objects.create(**task_kwargs)
        TaskDescription.objects.create(description=params['description'], task=task)

    return JsonResponse({'result': 'ok'})


@csrf_exempt
def edit_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Request is not POST'}, status=400)

    form = EditTaskForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    params = form.cleaned_data
    Task.objects.filter(id=params['task_id']).update(assignee_id=params['assignee_id'], status=params['status'])

    return JsonResponse({'result': 'ok'})


@csrf_exempt
def delete_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Request is not POST'}, status=400)

    form = OneTaskForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    params = form.cleaned_data
    Task.objects.filter(id=params['task_id']).delete()

    return JsonResponse({'result': 'ok'})


@csrf_exempt
def add_comment(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Request is not POST'}, status=400)

    form = AddCommentForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    params = form.cleaned_data
    TaskComment.objects.create(comment=params['comment'], task_id=params['task_id'])

    return JsonResponse({'result': 'ok'})


def get_all_tasks(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Request is not GET'}, status=400)

    form = TaskForm(request.GET)
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    params = form.cleaned_data
    name = params['name']
    status = params['status']
    assignee_id = params['assignee_id']
    reporter_id = params['reporter_id']
    project_id = params['project_id']
    description = params['description']

    tasks = Task.objects.all()
    if name:
        tasks = tasks.filter(name=name)
    if status:
        tasks = tasks.filter(status=status)
    if assignee_id:
        tasks = tasks.filter(assignee_id=assignee_id)
    if reporter_id:
        tasks = tasks.filter(reporter_id=reporter_id)
    if project_id:
        tasks = tasks.filter(reporter_id=project_id)
    if description:
        exclude_task_ids = TaskDescription.objects.filter(
            description__icontains=description
        ).values_list('id', flat=True)
        tasks = tasks.exclude(id__in=exclude_task_ids)

    tasks = tasks.select_related(
        'assignee', 'reporter', 'project'
    ).prefetch_related(
        'taskdescription_set', 'taskcomment_set'
    )

    result = []
    for task in tasks:
        result.append({
            'id': task.id,
            'name': task.name,
            'status': task.status,
            'assignee_id': task.assignee_id,
            'assignee_name': task.assignee.name if task.assignee else None,
            'reporter_id': task.reporter_id,
            'reporter_name': task.reporter.name,
            'project_id': task.project_id,
            'project_name': task.project.name,
            'description': [{d.id: d.description} for d in task.taskdescription_set.all()],
            'comment': [{c.id: c.comment} for c in task.taskcomment_set.all()],
        })

    return JsonResponse({'result': result})


def get_task(_, task_id):
    form = OneTaskForm({'task_id': task_id})
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    task = Task.objects.filter(
        id=task_id
    ).select_related(
        'assignee', 'reporter', 'project'
    ).prefetch_related(
        'taskdescription_set', 'taskcomment_set'
    ).first()

    result = {
        'id': task.id,
        'name': task.name,
        'status': task.status,
        'assignee_id': task.assignee_id,
        'assignee_name': task.assignee.name if task.assignee else None,
        'reporter_id': task.reporter_id,
        'reporter_name': task.reporter.name,
        'project_id': task.project_id,
        'project_name': task.project.name,
        'description': [{d.id: d.description} for d in task.taskdescription_set.all()],
        'comment': [{c.id: c.comment} for c in task.taskcomment_set.all()],
    }

    return JsonResponse({'result': result})





