from rest_framework import serializers
from dashboard.models import SubmittedForm

class SubmittedFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedForm
        fields = '__all__'
