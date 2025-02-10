from django.db import models
import json

class DynamicForm(models.Model):
    name = models.CharField(max_length=255)
    fields = models.JSONField()  # Store form fields dynamically as JSON

    def __str__(self):
        return f"Form {self.id}"


class SubmittedForm(models.Model):
    form_id = models.IntegerField()  # Store which form this data belongs to
    data = models.JSONField()  # Store all form field values as JSON
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Form {self.form_id} - {self.created_at}"



