from django.urls import path
from .views import AboutView,home,home_search,contact,dashboard
from . import api_view

app_name='settings'

urlpatterns=[
    path('',home,name='home'),
    path('search/',home_search,name='home_search'),
    path('about/',AboutView.as_view(),name='about'),
    path('contact/',contact,name='contact'),
    path('dashboard/',dashboard,name='dashboard'),


    path('about/api/',api_view.about_api,name='about_api'),
    path('about/api/faq/',api_view.faq_api,name='faq_api'),
    path('contact/api',api_view.contact_api,name='conact_api')

]