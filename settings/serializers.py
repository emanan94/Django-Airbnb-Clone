from rest_framework import serializers
from .models import About, FAQ


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model=About
        fields = '__all__'




class FAQSerializers(serializers.ModelSerializer):
    class Meta:
        model=FAQ
        fields = '__all__'