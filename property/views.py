from django.shortcuts import render ,redirect
from .admin import Property, Category, PropertyImages, PropertyReview
from django.views.generic import ListView, DetailView,CreateView
from django.views.generic.edit import FormMixin
from .forms import PropertyBookForm
from django.urls import reverse
from django.contrib import messages
from .filters import PropertyFilter
from django_filters.views import FilterView


# Create your views here.


class PropertyList(FilterView):
    model=Property
    paginate_by=2
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'

    



class PropertyDetail(DetailView, FormMixin):
    model=Property
    form_class=PropertyBookForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["property_images"] =PropertyImages.objects.filter(property=self.get_object().id) 
        print( context["property_images"]) #to add empty list then add images to it
        
        context["review_count"]=PropertyReview.objects.filter(property=self.get_object()).count()
        return context

    #to save form

    def post(self, request, *args, **kwargs):
       form=self.get_form()
       if form.is_valid():
           myform=form.save(commit=False)
           myform.property=self.get_object()
           myform.save()
           messages.success(request, 'Your reservation confirmed.')

           #send email message

           return redirect(reverse('property:property_detail',kwargs={'slug':self.get_object().slug}))
           
    
class NewProperty(CreateView):
    model=Property
    fields=['title','description','price','place','image','category']
   
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, 'Successfully Added Your Property')

            ### send gmail message

            return redirect(reverse('property:property_list'))
        