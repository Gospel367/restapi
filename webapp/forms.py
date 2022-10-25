from .models import MyDictionary
from django.forms.models import ModelForm

class DictForm(ModelForm):
    
    class Meta:
        model = MyDictionary
        fields = '__all__'
    