# coding: utf-8
from django import forms

from task_tracker.user.models import User
from task_tracker.project.models import Project
from .models import Task


class CreateTaskForm(forms.Form):
    name = forms.CharField(max_length=1024)
    status = forms.CharField(max_length=1024)
    description = forms.CharField(max_length=4096)
    assignee_id = forms.IntegerField(required=False)
    reporter_id = forms.IntegerField()
    project_id = forms.IntegerField()

    def clean_assignee_id(self):
        assignee_id = self.cleaned_data['assignee_id']

        if assignee_id is not None and not Project.objects.filter(id=assignee_id).exists():
            raise forms.ValidationError("Field assignee_id is incorrect")

        return assignee_id

    def clean_reporter_id(self):
        reporter_id = self.cleaned_data['reporter_id']

        if not User.objects.filter(id=reporter_id).exists():
            raise forms.ValidationError("Field reporter_id is incorrect")

        return reporter_id

    def clean_project_id(self):
        project_id = self.cleaned_data['project_id']

        if not Project.objects.filter(id=project_id).exists():
            raise forms.ValidationError("Field project_id is incorrect")

        return project_id


class EditTaskForm(forms.Form):
    status = forms.CharField(max_length=1024)
    assignee_id = forms.IntegerField(required=False)
    task_id = forms.IntegerField()

    def clean_assignee_id(self):
        assignee_id = self.cleaned_data['assignee_id']

        if assignee_id is not None and not User.objects.filter(id=assignee_id).exists():
            raise forms.ValidationError("Field assignee_id is incorrect")

        return assignee_id

    def clean_task_id(self):
        task_id = self.cleaned_data['task_id']

        if not Task.objects.filter(id=task_id).exists():
            raise forms.ValidationError("Field task_id is incorrect")

        return task_id


class OneTaskForm(forms.Form):
    task_id = forms.IntegerField()

    def clean_task_id(self):
        task_id = self.cleaned_data['task_id']

        if not Task.objects.filter(id=task_id).exists():
            raise forms.ValidationError("Field task_id is incorrect")

        return task_id


class AddCommentForm(forms.Form):
    comment = forms.CharField(max_length=4096)
    task_id = forms.IntegerField()

    def clean_task_id(self):
        task_id = self.cleaned_data['task_id']

        if not Task.objects.filter(id=task_id).exists():
            raise forms.ValidationError("Field task_id is incorrect")

        return task_id


class TaskForm(forms.Form):
    name = forms.CharField(max_length=1024, required=False)
    status = forms.CharField(max_length=1024, required=False)
    description = forms.CharField(max_length=4096, required=False)
    assignee_id = forms.IntegerField(required=False)
    reporter_id = forms.IntegerField(required=False)
    project_id = forms.IntegerField(required=False)

    def clean_assignee_id(self):
        assignee_id = self.cleaned_data['assignee_id']

        if assignee_id is not None and not User.objects.filter(id=assignee_id).exists():
            raise forms.ValidationError("Field assignee_id is incorrect")

        return assignee_id

    def clean_reporter_id(self):
        reporter_id = self.cleaned_data['reporter_id']

        if reporter_id is not None and not User.objects.filter(id=reporter_id).exists():
            raise forms.ValidationError("Field reporter_id is incorrect")

        return reporter_id

    def clean_project_id(self):
        project_id = self.cleaned_data['project_id']

        if project_id is not None and not Project.objects.filter(id=project_id).exists():
            raise forms.ValidationError("Field assignee_id is incorrect")

        return project_id
