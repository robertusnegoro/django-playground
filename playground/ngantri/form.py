from django import forms
from .models import Person


# Create your forms here.
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "image")
