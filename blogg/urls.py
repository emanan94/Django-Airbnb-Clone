from django.urls import path
from .views import PostList,PostDetail


app_name='blogg'

urlpatterns = [
    path('',PostList.as_view(),name='post_list'),
    path('<slug:slug>',PostDetail.as_view(),name='post_detail'),
   # path('<int:pk>',PostDetail.as_view(),name='post_detail'),
    # path('<slug:slug>',PostDetail.as_view(),name='post_detail'), #commented cause didn't add slug to sub url 

]
