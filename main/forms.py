from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import  Post

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'