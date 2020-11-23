from django.urls import path
from . import views #=== from .views import PropertyList, PropertyDetail 


app_name='property'


urlpatterns=[
    path('', views.PropertyList.as_view(), name='property_list' ), # views. cause line 2
    path('new/', views.NewProperty.as_view(), name='new_property' ), 
    path('<slug:slug>', views.PropertyDetail.as_view(), name='property_detail'),
]