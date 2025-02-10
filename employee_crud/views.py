from rest_framework import viewsets, permissions
from dashboard.models import SubmittedForm
from .serializers import SubmittedFormSerializer

class SubmittedFormViewSet(viewsets.ModelViewSet):
    queryset = SubmittedForm.objects.all()
    serializer_class = SubmittedFormSerializer
    permission_classes = [permissions.IsAuthenticated]
