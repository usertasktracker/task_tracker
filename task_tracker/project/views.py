# coding: utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import Project
from .forms import ProjectForm


@csrf_exempt
def create_project(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Request is not POST'}, status=400)

    form = ProjectForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    params = form.cleaned_data
    Project.objects.create(name=params['name'])
    return JsonResponse({'result': 'ok'})


def get_all_projects(_):
    projects = Project.objects.all().values('id', 'name')
    return JsonResponse({'result': list(projects)})


