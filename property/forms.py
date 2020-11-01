from django import forms
from .models import PropertyBook


class PropertyBookForm(forms.ModelForm):
    date_from=forms.DateTimeField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    date_to=forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
  

    #another way to Django: Getting Form Select Options from a Database Table  
    '''OPTIONS = (
        (1,1),
        (2,2),
        (3,3), 
        (4,4), 
        )
    guest = forms.ChoiceField(required=True, choices=OPTIONS)'''

    class Meta:
        model=PropertyBook
        fields=['name','email','date_from','date_to','guest','children']