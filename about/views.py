# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
import django
from models import Acknowledgement, OrganizationPerson, OrganizationPosition
from forms import AddPositionForm
from  django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import authenticate, login, logout 

def index(request):
    add_position_form = ''
    if request.user.is_authenticated():
        if request.method == 'POST': # If the form has been submitted... 
            add_position_form = AddPositionForm(request.POST) # A form bound to the POST data 
            if add_position_form.is_valid(): # All validation rules pass 
                OrganizationPosition(position_name=add_position_form.cleaned_data['position']).save()
            # Process the data in form.cleaned_data 
            # ... 
            ##return HttpResponseRedirect('/thanks/') # Redirect after POST  
        add_position_form = AddPositionForm() # An unbound form 

    context = RequestContext(request, {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'home',
        "open_positions": OrganizationPosition.objects.all(),
        "add_position_form": add_position_form,
        "is_user_logged_in": request.user.is_authenticated(),
        "login_failed_username": request.GET.get('login_failed_username', ''),
        "user": request.user,
    })

    return render_to_response("homepage.html", context)

def about(request):
    mission_statement = MissionStatement.objects.all()[0].statement if MissionStatement.objects.all() else ''
    return render_to_response("about.html", RequestContext(request, {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'about',
        "mission_statement": mission_statement,
        "is_user_logged_in": request.user.is_authenticated(),
    }))

def acknowledgements(request):
    return render_to_response("acknowledgements.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'acknowledgements',
        "people_acknowledged": Acknowledgement.objects.all(),
    })

def person_acknowledged(request, name):
    return render_to_response("person_acknowledged.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'person acknowledged',
        "section": 'acknowledgements',
        "person_acknowledged": Acknowledgement.objects.get(persons_name__iexact=name.replace('_', ' ')),
    })

def our_people(request):
    return render_to_response("our_people.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'our people',
        "people": OrganizationPerson.objects.all(),
    })
    

def our_plan(request):
    return render_to_response("our_plan.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'our plan',
    })
    
def our_philosophy(request):
    return render_to_response("our_philosophy.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'our philosophy',
    })
    
def our_performance(request):
    return render_to_response("our_performance.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'our performance',
    })
    
def our_policies(request):
    return render_to_response("our_policies.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'our policies',
    })
    
def delete_position(request, position_id):
    if request.user.is_authenticated():
        OrganizationPosition.objects.get(id=position_id).delete()
    return HttpResponseRedirect('/')
    
def logout_user(request):
    logout(request) 
    return HttpResponseRedirect(request.META['HTTP_REFERER']) # Redirect back to the page the user logged out from
    
def login_user(request):
    username = request.POST['username'] 
    password = request.POST['password'] 
    user = authenticate(username=username, password=password) 
    if user is not None: 
        if user.is_active: 
            login(request, user) 
            return HttpResponseRedirect(request.META['HTTP_REFERER']) # Redirect to a success page. 
        else: 
            return HttpResponseRedirect(request.META['HTTP_REFERER'] + '?login_failed=disabled') # Return a ’disabled account’ error message 
    else: 
        referer = request.META['HTTP_REFERER']
        if '?' in referer:
            referer = referer[:referer.find('?')]
        return HttpResponseRedirect(referer + '?login_failed_username=%s' % (username)) # Return an ’invalid login’ error message. 

