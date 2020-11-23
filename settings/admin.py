from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class AboutAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(models.About, AboutAdmin)
admin.site.register(models.FAQ)
admin.site.register(models.Info)
