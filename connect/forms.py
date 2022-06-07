from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Profile

class SignUpForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')

class UpdateUserInfoForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']