# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput, Textarea, HiddenInput, Select, DateInput, ChoiceField, EmailField, DateTimeInput, TimeInput

class EmailInputHTML5(TextInput):
    input_type = 'email'

class NumberInputHTML5(TextInput):
    input_type = 'number'

class TelephoneInputHTML5(TextInput):
    input_type = 'tel'

class DateInputHTML5(DateInput):
    input_type = 'date'

class DateTimeInputHTML5(DateTimeInput):
    input_type = 'datetime'

class TimeInputHTML5(TimeInput):
    input_type = 'time'
