# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
from subscriber.models import *
from subscriber.forms import *

@csrf_protect
@cache_page(60 * 60)
def index(request):
    form_person = personForm()

    return render_to_response('index.html', {
        'form_person': form_person
        },
    context_instance=RequestContext(request))

@csrf_protect
def add(request):
    if request.method == 'POST':
        form_person = personForm(request.POST)

        if form_person.is_valid():
            try:
                view_person = person.objects.get(email=form_person.instance.email)
                view_person.counter += 1
                view_person.save()
            except person.DoesNotExist:
                new_person = form_person.save(commit=False)
                new_person.remote_ip = request.META['REMOTE_ADDR']
                new_person.save()
            return render_to_response('add.html', {}, context_instance=RequestContext(request))
    else:
        form_person = personForm()

    return render_to_response('index.html', {
        'form_person': form_person
        },
    context_instance=RequestContext(request))

@cache_page(60 * 60)
def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))
