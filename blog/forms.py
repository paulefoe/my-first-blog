from django import forms
from registration.forms import RegistrationForm
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class CommentFormLogged(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class Register(RegistrationForm):
    email = forms.EmailField(required=True)

    class Meta:
        fields = {'username', 'password1', 'password2', 'email'}
