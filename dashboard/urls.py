from django.urls import path
from . import views
from .views import (dashboard_view, dynamic_forms,save_dynamic_form,employee_creation,
                    get_form_fields,save_form,delete_form)

app_name = "dashboard"

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dynamic_forms/', dynamic_forms, name='dynamic_forms'),
    path('save_dynamic_form/', save_dynamic_form, name='save_dynamic_form'),

    path('employee_creation/', employee_creation, name='employee_creation'),

    path('get-form-fields/<int:form_id>/', get_form_fields, name='get_form_fields'),

    path('save-form/', save_form, name='save_form'),

    path('delete-form/<int:id>/', delete_form, name='delete_form'),




]
