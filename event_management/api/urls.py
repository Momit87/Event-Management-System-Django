from django.urls import path
from .views import EventDetailAPI

urlpatterns = [
    path('events/<int:pk>/', EventDetailAPI.as_view(), name='event-detail-api'),
]

