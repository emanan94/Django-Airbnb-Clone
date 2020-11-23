from django.shortcuts import render
from .models import About,FAQ,Info
from django.views.generic import ListView

# Create your views here.
class AboutView(ListView):
    model = FAQ


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last() 
        return context
    