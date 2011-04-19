from django.db import models
from django.db.models import get_model

class Acknowledgement(models.Model):
    persons_name = models.CharField(max_length=50)
    affilation = models.CharField(max_length=500)
    contributions = models.TextField()

    def __unicode__(self):
        return self.persons_name

    def get_url(self):
        s = self.persons_name.lower() # lowercase the name
        s = s.replace(' ', '_') # replace spaces with underscore
        return s

class OrganizationPerson(models.Model):
    persons_name = models.CharField(max_length=50)
    
    short_bio = models.TextField()
    long_bio = models.TextField()

    def __unicode__(self):
        return self.persons_name

    def positions(self):
        OrganizationPositionFilling = get_model("about", "OrganizationPositionFilling")
        return ', '.join(['%s%s' % ('Interim ' if i.interim else '', str(i.position)) for i in OrganizationPositionFilling.objects.filter(person=self, end_date__isnull=True)])

class OrganizationPosition(models.Model):
    position_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.position_name    
        
    def is_position_open(self):
        pass

class OrganizationPositionFilling(models.Model):
    position = models.ForeignKey(OrganizationPosition)
    person = models.ForeignKey(OrganizationPerson)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    interim = models.BooleanField()

    def __unicode__(self):
        return '%s%s: %s' % ('Interim ' if self.interim else '', self.position.position_name, self.person.persons_name)
    
#class     
