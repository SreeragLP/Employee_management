from rest_framework import serializers
from dashboard.models import SubmittedForm  # Make sure it's importing only models

class SubmittedFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedForm
        fields = '__all__'
