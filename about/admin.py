from django.contrib import admin
from .models import MissionStatement, Acknowledgement, OrganizationPerson, OrganizationPosition, OrganizationPositionFilling

admin.site.register(MissionStatement) 
admin.site.register(Acknowledgement)
admin.site.register(OrganizationPerson)
admin.site.register(OrganizationPosition)
admin.site.register(OrganizationPositionFilling)
