from django.contrib.auth.models import User
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db.models import Max
from .models import *
import random
import datetime
import re

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail или ID',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))