# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.template import loader, Context
from django.core.mail import EmailMessage

class person(models.Model):
    email = models.EmailField()
    remote_ip = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    counter = models.IntegerField(default=1)

    def __unicode__(self):
        return self.email
