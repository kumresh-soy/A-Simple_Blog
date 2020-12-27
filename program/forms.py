from django.contrib.auth.models import User
from django import forms
from .models import Post
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','placeholder':'******'}))

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    # author = forms.Select()
    class Meta:
        model = Post
        fields = ["title","content","category","author"]

