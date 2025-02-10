from django.shortcuts import render, redirect
from .models import DynamicForm
from django.apps import apps
from dashboard.models import DynamicForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse  # Import reverse for proper redirection
from .models import SubmittedForm




def dashboard_view(request):
    submitted_forms = SubmittedForm.objects.all()

    # Extract unique field names dynamically
    field_names = set()
    for form in submitted_forms:
        field_names.update(form.data.keys())

    return render(request, 'dashboard.html', {
        'submitted_forms': submitted_forms,
        'field_names': sorted(field_names)  # Send sorted field names
    })


def dynamic_forms(request):
    return render(request, 'dynamic_forms.html')


def save_dynamic_form(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Receive JSON from frontend
            form_name = data.get("form_name")  # Name of the form
            form_fields = data.get("fields")  # List of label & type

            # Save to DB
            new_form = DynamicForm(name=form_name, fields=form_fields)
            new_form.save()

            return JsonResponse({"message": "Form saved successfully!"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


def employee_creation(request):
    DynamicForm = apps.get_model('dashboard', 'DynamicForm')  # Delayed import
    forms = DynamicForm.objects.all()  # Get all saved forms
    return render(request, 'employee_creation.html', {'forms': forms})


def get_form_fields(request, form_id):
    form = get_object_or_404(DynamicForm, id=form_id)

    try:
        fields = json.loads(form.fields) if isinstance(form.fields, str) else form.fields
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid form data"}, status=400)

    return JsonResponse({"fields": fields})



@csrf_exempt  # If CSRF causes issues, but try to use CSRF token instead
def save_form(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Read JSON data properly

            print("Received Data:", data)

            # Save to database
            submitted_form = SubmittedForm.objects.create(
                form_id=1,  # Temporary static ID
                data=data
            )
            submitted_form.save()

            return JsonResponse({"message": "Form saved successfully!"}, status=200)

        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({"message": "Error processing form data."}, status=400)

    return JsonResponse({"message": "Invalid request."}, status=405)



def delete_form(request, id):
    form = get_object_or_404(SubmittedForm, id=id)
    form.delete()

    return redirect(reverse('dashboard:dashboard'))






