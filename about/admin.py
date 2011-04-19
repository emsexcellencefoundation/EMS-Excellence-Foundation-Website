from django.contrib import admin
from .models import Acknowledgement, OrganizationPerson, OrganizationPosition, OrganizationPositionFilling

admin.site.register(Acknowledgement)
admin.site.register(OrganizationPerson)
admin.site.register(OrganizationPosition)
admin.site.register(OrganizationPositionFilling)
