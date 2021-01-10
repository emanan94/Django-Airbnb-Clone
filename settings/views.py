from django.shortcuts import render
from .models import About,FAQ,Info
from django.views.generic import ListView
from property import models as property_models
from blogg import models as blog_models
from django.contrib.auth.models import User
from django.db.models import Q, Count




# Create your views here.

def home(request):
    property_category=property_models.Category.objects.all()
    recent_blog=blog_models.Post.objects.all()[:4]
    popular_apartments=property_models.Property.objects.filter(category__name='Apartment')[:4]
    pupular_villa=property_models.Property.objects.filter(category__name='Villa')[:4]
    pupular_suite=property_models.Property.objects.filter(category__name='suite')[:5]

    user_count=User.objects.all().count()
    apartments_count=property_models.Property.objects.filter(category__name='Apartment').count()
    villa_count=property_models.Property.objects.filter(category__name='Villa').count()
    suite_count=property_models.Property.objects.filter(category__name='suite').count()

    places=property_models.Place.objects.all().annotate(property_count=Count('property_place'))

    about=About.objects.last()
    
    return render(request,'settings/index.html',{
    'property_category': property_category,
    'recent_blog':recent_blog,
    'popular_apartments':popular_apartments,
    'about':about,
    'pupular_villa':pupular_villa,
    'pupular_suite':pupular_suite,
    'apartments_count':apartments_count,
    'villa_count':villa_count,
    'suite_count': suite_count,
    'places':places
    })


def home_search(request):
    name=request.GET.get('q','')
    location = request.GET['location']

    search_result=property_models.Property.objects.filter(
        Q(title__icontains=name)&
        Q(place__icontains=location)
    )

    return render(request,'settings/home_search.html',{'search_result':search_result})


class AboutView(ListView):
    model = FAQ


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last() 
        return context
    

def contact(request):
    info=Info.objects.all()

    return render(request,'settings/contact.html',{'info':info})