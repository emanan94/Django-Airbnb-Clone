from django.shortcuts import render
from .admin import Post,Category
from django.views.generic import ListView,DetailView
from taggit.models import Tag
from django.db.models import Count


# Create your views here.

class PostList(ListView):
    model=Post
    paginate_by=8

class PostDetail(DetailView):
    model=Post

  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all().annotate(post_count=Count('post_category'))
        context['recent_posts']=Post.objects.all()[:3]
        return context
