from django.forms import ModelForm
from .models import Uses

class UsesForm(ModelForm):
  class Meta:
    model = Uses
    fields = ['date', 'used']