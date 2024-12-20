from rest_framework.generics import RetrieveAPIView
from events.models import Event
from .serializers import EventSerializer

class EventDetailAPI(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
