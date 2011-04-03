from django.shortcuts import render_to_response
import django
from models import MissionStatement, Acknowledgement, OrganizationPerson

def index(request):
    return render_to_response("homepage.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'home',
        "mission_statement": MissionStatement.objects.all()[0].statement
    })

def about(request):
    return render_to_response("about.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'about',
        "mission_statement": MissionStatement.objects.all()[0].statement
    })

def acknowledgements(request):
    return render_to_response("acknowledgements.html", {
        "ip_address": request.META['REMOTE_ADDR'],
        "django_version": django.VERSION,
        "meta": request.META.keys(),
        "page": 'acknowledgements',
        "people_acknowledged": Acknowledgement.objects.all()
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
        "people": OrganizationPerson.objects.all()
    })
