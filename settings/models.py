from django.db import models

# Create your models here.
class About(models.Model):
    what_we_do=models.TextField(max_length=1000)
    our_mission=models.TextField(max_length=1000)
    Our_goal=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='about/')

    class Meta:
        verbose_name_plural ='about'

    def __str__(self):
        return str(self.id)

class FAQ(models.Model):
    question=models.CharField(max_length=200)
    answer=models.TextField(max_length=1000)

    def __str__(self):
        return str(self.question)


class Info(models.Model):
    name=models.CharField(max_length=25)
    logo=models.ImageField(upload_to='company/')
    description=models.TextField(max_length=500)
    fb_url=models.URLField(blank=True ,null=True)
    twitter_url=models.URLField(blank=True ,null=True)
    instgram_url=models.URLField(blank=True ,null=True)
    address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)
    email=models.EmailField()

    class Meta:
        verbose_name_plural ='info'

    def __str__(self): 
        return str(self.name)