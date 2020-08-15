from django import forms 
from .models import itemDetails
  
class itemDetailsForm(forms.ModelForm): 
  
    class Meta: 
        model = itemDetails 
        exclude = ('User',),
        fields = ['name','description','bid','category','Image'] 