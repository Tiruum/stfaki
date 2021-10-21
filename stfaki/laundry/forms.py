from .models import signups
from django.forms import ModelForm

class signupsForm(ModelForm):
    class Meta:
        model = signups
        fields = ['user', 'datetime', 'wm1', 'wm2', 'wm3', 'wm4', 'wm5', 'wm6']
