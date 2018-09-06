# coding: utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import User
from .forms import UserForm


@csrf_exempt
def create_user(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Request is not POST'}, status=400)

    form = UserForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'error': form.errors}, status=400)

    params = form.cleaned_data
    User.objects.create(name=params['name'])
    return JsonResponse({'result': 'ok'})


def get_all_users(_):
    users = User.objects.all().values('id', 'name')
    return JsonResponse({'result': list(users)})

