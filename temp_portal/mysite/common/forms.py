from .models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username","last_name","first_name",'password' ,"job",)