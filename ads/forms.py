#-*- coding:utf-8 -*-
from .models import Ad
from django import forms

from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = "__all__"
        exclude = ('profile_status', 'likes', 'views', 'images', 'slug', 'rank', 'meta_title', 'meta_description', )