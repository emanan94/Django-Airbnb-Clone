from django.contrib import admin
from .models import Property, Category, PropertyReview,PropertyImages,PropertyBook,Place
from django_summernote.admin import SummernoteModelAdmin
from tof.admin import TofAdmin, TranslationTabularInline

# Register your models here.

class PropertyAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    
    list_display=['title', 'check_availability','get_rating_ave']



class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ('property','in_progress')

admin.site.register(Property,PropertyAdmin)


class CategoryAdmin(TofAdmin):
    list_display = ('id', 'name')

admin.site.register(Category,CategoryAdmin)


admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook,PropertyBookAdmin)
admin.site.register(Place)
