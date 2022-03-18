from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighborhood, Profile, Business, Post


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email' ,'username','password1', 'password2', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
    
