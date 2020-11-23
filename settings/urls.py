from django.urls import path
from .views import AboutView

app_name='settings'

urlpatterns=[
    path('',AboutView.as_view(),name='about')
]