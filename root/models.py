# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.template import loader, Context

class perfil(models.Model):
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.user.username
