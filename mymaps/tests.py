from django.test import TestCase

# Create your tests here.
import csv
from datetime import datetime
from models import Voter


def inject_voters_from_csv():
    with open(r'C:\Users\cr7\Downloads\samplelist.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            voter = Voter(
                ward=row['Ward'],
                pct=row['Pct'],
                voter_id=row['Voter ID'],
                last_name=row['Last Name'],
                first_name=row['First Name'],
                middle_name=row['Middle Name'],
                title=row['Title'],
                street_number=row['Street #'],
                street_name=row['Street Name'],
                apt_number=row['Apt #'],
                zip_code=row['Zip Code'],
                party_affiliation=row['Party Affiliation'],
                date_of_birth=datetime.strptime(row['Date of Birth'], '%m/%d/%Y').date(),
                voter_status=row['Voter Status']
            )
            voter.save()
