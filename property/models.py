from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Property(models.Model):
    owner=models.ForeignKey(User,related_name='property_owner',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    place=models.CharField(max_length=50)
    image=models.ImageField(upload_to='property/')
    category=models.ForeignKey('Category',related_name='property_category',on_delete=models.CASCADE)
    
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)


class PropertyImages(models.Model):
    property=models.ForeignKey('Property',related_name='property_image',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='property_images/')
    
    def __str__(self):
        return str(self.property.title)


class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class PropertyReview(models.Model):
    property=models.ForeignKey('Property',related_name='property_review',on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='review_author', on_delete=models.CASCADE)
    ratting= models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    feedback= models.CharField(default='', max_length=200)


    def __str__(self):
        return str(self.property.title)