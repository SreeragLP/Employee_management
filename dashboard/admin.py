from django.contrib import admin
from .models import DynamicForm, SubmittedForm

# Register your models here.

admin.site.register(DynamicForm)
admin.site.register(SubmittedForm)
