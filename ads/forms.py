#-*- coding:utf-8 -*-
from .models import Ad
from django import forms

class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = "__all__"