from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Property(models.Model):
    owner=models.ForeignKey(User,related_name='property_owner',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=50 ,blank=True , null=True)
    price=models.IntegerField()
    place=models.ForeignKey('Place',related_name='property_place',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='property/')
    category=models.ForeignKey('Category',related_name='property_category',on_delete=models.CASCADE)
    
    slug=models.SlugField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural='Properties'

    def save(self, *args, **kwargs):
       if self.title:
           self.slug=slugify(self.title)
       super(Property, self).save(*args, **kwargs) # Call the real save() method
 
 
    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
                      #namespace:path_name
        return reverse('property:property_detail',kwargs={'slug':self.slug})



    #Check_Availability
    def check_availability(self):
        all_resrvations=self.property_book.all()
        time=timezone.now()

        for reservation in all_resrvations:
            if time> reservation.date_to:
                return 'Available'
            elif time> reservation.date_from and time < reservation.date_to:
                return 'Occupied'
        else:
            return 'Not Available'

    
    #Rating Average
    def get_rating_ave(self):
        all_reviews=self.property_review.all()
        all_ratings=0
        
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings+= review.rating

            return round(all_ratings / len(all_reviews))
        else:
            return '-'
    


#===========
class PropertyImages(models.Model):
    property=models.ForeignKey('Property',related_name='property_image',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='property_images/')

    class Meta:
        verbose_name_plural='PropertyImages'
        verbose_name='PropertyImage'

    def __str__(self):
        return str(self.property.title)


#===========
class Category(models.Model):
    name= models.CharField(max_length=50)
    icon= models.CharField(max_length=25 , blank=True, null=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return str(self.name)

#===========
class PropertyReview(models.Model):
    property=models.ForeignKey('Property',related_name='property_review',on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='review_author', on_delete=models.CASCADE)
    rating= models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    feedback= models.TextField(default='', max_length=200)


    def __str__(self):
        return str(self.property.title)

#===========
class PropertyBook(models.Model):
    visitors_type=(
        (1,1),
        (2,2),
        (3,3),
        (4,4),
    )
    property=models.ForeignKey(Property,related_name='property_book',on_delete=models.CASCADE)
    user_name=models.ForeignKey(User,related_name='user_book',on_delete=models.CASCADE)
    date_from=models.DateTimeField(default=timezone.now)
    date_to=models.DateTimeField(default=timezone.now)
    guest=models.IntegerField(default=1,choices=visitors_type)
    children=models.IntegerField(default=0,choices=visitors_type)


    def __str__(self):
        return str(self.property.title)


    #Progress
    def in_progress(self):
        now = timezone.now()
        return now > self.date_from and now < self.date_to

    in_progress.boolean = True

#================
class Place(models.Model):
    place_name= models.CharField(max_length=50)
    image=models.ImageField(upload_to='places/')


    def __str__(self):
        return self.place_name
    