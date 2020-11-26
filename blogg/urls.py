from django.urls import path
from .views import PostList,PostDetail
from . import api_view

app_name='blogg'

urlpatterns = [
    path('',PostList.as_view(),name='post_list'),
    path('<slug:slug>',PostDetail.as_view(),name='post_detail'),
    # path('<int:pk>',PostDetail.as_view(),name='post_detail'),
    # path('<slug:slug>',PostDetail.as_view(),name='post_detail'), #commented cause didn't add slug to sub url 

    path('api/list' , api_view.post_list_api , name='post_list_api'),
    path('api/list/<int:id>' , api_view.post_detail , name='post_detail_api'),
    path('api/list/<str:query>' , api_view.post_search , name='post_search_api'),

]
