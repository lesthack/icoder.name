# -*- coding: utf-8 -*-

from django import forms
from subscriber.widgets import *
from subscriber.models import *

class personForm(ModelForm):
    class Meta:
        model = person
        fields = {'email'}
        widgets = {
            'email': EmailInputHTML5(attrs={'placeholder':'Email'}),
        }
