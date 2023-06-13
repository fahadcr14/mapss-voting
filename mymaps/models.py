'''import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mapss.settings")
import django
django.setup()'''
from django.db import models

class Voter(models.Model):
    ward = models.IntegerField()
    pct = models.CharField(max_length=1)
    voter_id = models.CharField(max_length=12)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=10, blank=True)
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True)
    zip_code = models.CharField(max_length=10)
    party_affiliation = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    voter_status = models.CharField(max_length=1)
class Questionnaire(models.Model):
    apt = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    q1 = models.CharField(max_length=100, null=True, blank=True)
    q2 = models.CharField(max_length=100, null=True, blank=True)
    q3 = models.CharField(max_length=100, null=True, blank=True)
    q4 = models.CharField(max_length=100, null=True, blank=True)
    q5 = models.CharField(max_length=100, null=True, blank=True)


    
