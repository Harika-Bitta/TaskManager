from django.contrib import admin

from taskapp.models import Task, Department

# Register your models here.
admin.site.register(Task)
admin.site.register(Department)