from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubmittedFormViewSet

router = DefaultRouter()
router.register(r'submitted-forms', SubmittedFormViewSet, basename='submittedform')

urlpatterns = [
    path('', include(router.urls)),
]
