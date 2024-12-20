from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)

urlpatterns = [
    # Route for the list of events
    path('', EventListView.as_view(), name='event-list'),

    # Route for event details
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),

    # Route for creating a new event
    path('create/', EventCreateView.as_view(), name='event-create'),

    # Route for updating an event
    path('<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),

    # Route for deleting an event
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]
