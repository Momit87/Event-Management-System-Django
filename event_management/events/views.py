from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    ordering = ['date_time']

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event-list')

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
    success_url = reverse_lazy('event-list')

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('event-list')
