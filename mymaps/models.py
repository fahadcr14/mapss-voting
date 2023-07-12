'''import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mapss.settings")
import django
django.setup()'''
from django.db import models
from django.utils import timezone
import pytz
from datetime import datetime
'''class Voter(models.Model):
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
    voter_status = models.CharField(max_length=1)'''
def time_zone():
    utc_time = datetime.now(pytz.utc)

    # Convert the UTC time to a specific time zone
    target_timezone = pytz.timezone('America/Chicago')
    local_time = utc_time.astimezone(target_timezone)

    return local_time
class Questionnaire(models.Model):
    ward=models.CharField(max_length=255, null=True, blank=True)
    pct=models.CharField(max_length=255, null=True, blank=True)
    apt = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    q1 = models.CharField(max_length=100, null=True, blank=True)
    q2 = models.CharField(max_length=100, null=True, blank=True)
    q3 = models.CharField(max_length=100, null=True, blank=True)
    q4 = models.CharField(max_length=100, null=True, blank=True)
    q5 = models.CharField(max_length=100, null=True, blank=True)
    q6 = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    voter_name=models.CharField(max_length=255, null=True, blank=True)
    created_at = models.CharField(max_length=100,default=time_zone())
    '''def save(self, *args, **kwargs):
        self.created_at = timezone.localtime()
        super().save(*args, **kwargs)
'''


class Voters_list(models.Model):
    ward = models.IntegerField()
    pct = models.CharField(max_length=1)
    voter_id = models.CharField(max_length=12)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=10, blank=True)
    street_number = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    party_affiliation = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    voter_status = models.CharField(max_length=1)
    longitude=models.CharField(max_length=100)
    latitude=models.CharField(max_length=100)
    full_address = models.CharField(max_length=255,blank=True)
    
    


class Votelatlon(models.Model):
    ward = models.IntegerField()
    pct = models.CharField(max_length=1)
    voter_id = models.CharField(max_length=12)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=10, blank=True)
    street_number = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    apt_number = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    party_affiliation = models.CharField(max_length=100, blank=True)
    date_of_birth =  models.CharField(max_length=255,blank=True)
    voter_status = models.CharField(max_length=1)
    longitude=models.CharField(max_length=100)
    latitude=models.CharField(max_length=100)
    full_address = models.CharField(max_length=255,blank=True)
    visited = models.CharField(max_length=255, blank=True, default='no')
