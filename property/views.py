from django.shortcuts import render
from .admin import Property, Category, PropertyImages, PropertyReview
from django.views.generic import ListView, DetailView
# Create your views here.


class PropertyList(ListView):
    model=Property



class PropertyDetail(DetailView):
    model=Property


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["property_images"] =PropertyImages.objects.filter(property=self.get_object().id) 
        print( context["property_images"]) #to add empty list then add images to it
        return context
    
