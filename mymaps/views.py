from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    if request.method == 'GET':
        response = render(request, 'mymaps/index.html')
        response["Access-Control-Allow-Origin"] = "*"  # Allow all origins (adjust as needed)
        response["Access-Control-Allow-Headers"] = "Content-Type"
        response["Access-Control-Allow-Methods"] = "GET"
        return response
    else:
        return HttpResponseNotAllowed(['GET'])

def questions(request):
    return render(request, 'mymaps/questions.html')

from django.test import TestCase
# Create your tests here.
import csv
from datetime import datetime
from .models import Voters_list,Votelatlon,time_zone
def inject_voters_from_csv(request):
    #print(f'starting to inject')
    i=0
    with open(r'C:\Users\cr7\3D Objects\conv\New folder\full\lastcsv.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            voter = Votelatlon(
                ward=row['Ward'],
                pct=row['Pct'],
                voter_id=row['Voter ID'],
                last_name=row['Last Name '],
                first_name=row['First Name '],
                middle_name=row['Middle Name '],
                title=row['Title '],
                street_number=row['Street #'],
                street_name=row['Street Name'],
                apt_number=row['Apt #'],
                city=row['City'],
                state=row['State'],
                zip_code=row['Zip Code'],
                party_affiliation=row['Party Affiliation '],
                #date_of_birth=datetime.strptime(row['Date of Birth '], '%m/%d/%Y').date(),
                voter_status=row['Voter Status'],
                longitude=row['Longitude'],
                latitude=row['Latitude'],
                full_address=row['Full address']


            )
            voter.save()
            #print(i)
            i+=1
        ##print(f'success')

def get_voter_data(request):
    strig=request.GET.get('query','').split(',')
    query=strig[0]
    ward=strig[1]
    pcts=strig[2]
    ##print('Voters data query ',strig)
    voters=Votelatlon.objects.filter(ward=ward,pct=pcts,street_name=query.upper()).values_list()
    data = list(voters.values())
    ##print('get voters data',data)
    lst=list()
    i=0
    
    for q in data:
        if query.upper()==q['street_name'] :
            lst.append(q)
    response=JsonResponse(lst, safe=False)
    response["Access-Control-Allow-Origin"] = "http://16.170.195.14"  # Allow all origins (adjust as needed)
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "GET"
        
    return response
import re,random
def get_persons(request):
    random_num=random.randint(1,999)
    strig=request.GET.get('query','').split(',')
    #print(f'Get person {random_num} ',strig)
    
    query=strig[0]
    kq=strig[0].split(' ')
    #print(kq)
    
    ward=strig[1]
    pcts=strig[2]
    if len(kq)==4:
        #print('Normal House')
        st_number=kq[0]
        st_name=kq[1]+' '+kq[2]
        zip_number=kq[3]
        voters=Votelatlon.objects.filter(ward=ward,pct=pcts,street_number=st_number,street_name=st_name,zip_code=zip_number).values_list()
    if len(kq)==5:
        #print('Apartment ')

        apt_num=kq[0]
        st_number=kq[1]
        st_name=kq[2]+' '+kq[3]
        zip_number=kq[4]
        voters=Votelatlon.objects.filter(ward=ward,pct=pcts,apt_number=apt_num,street_number=st_number,street_name=st_name,zip_code=zip_number).values_list()
    data = list(voters.values())
    data2 = list(voters.first())

    ##print('Here is data',data)
    #print('LENGTH OF DATA ',len(data))
    names=''
    i=0
    digit= re.findall(r'\d+', query)
    strng=re.split(r'\d+', query)
    correct_strng=strng[-1].lstrip()
    query_without_spaces=''.join(query.split())
    address_verify=''
    i=0
    for q in data:
            i+=1
            
            names+=(q['first_name']+' '+q['last_name'])
            if i<len(data):
                names+=','
            

            text=str(q['apt_number'])+str(q['street_number'])+' '+q['street_name']+' '+q['zip_code']
            if text!=address_verify:
                address_verify+=text
            '''if q['apt_number']=='':
                var1=str(q['street_number'])+' '+q['street_name']+' '+q['zip_code']
            else:
                
                var1=str(q['apt_number'])+str(q['street_number'])+' '+q['street_name']+' '+q['zip_code']
            var_no_space=''.join(var1.split())
            if query_without_spaces==var_no_space:
                names.append(q['first_name']+' '+q['last_name'])
                address_verify.append(q['full_address'])
            i+=1'''
    names_x_address=names+','+address_verify
    response_data = {'names': names,
                     'row_data':data2
                     }
    
    response=JsonResponse(response_data, safe=False)
    response["Access-Control-Allow-Origin"] = "http://16.170.195.14"  # Allow all origins (adjust as needed)
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "GET"
    #print(f'{random_num} Names {names} address {address_verify}')
    return response 

from .models import Questionnaire

def submit_questionnaire(request):
    if request.method == 'POST':
        
        apart = request.GET.get('query')
        user=apart.split(',')[-6]
        person=apart.split(',')[-5]
        ward=apart.split(',')[-4]
        pct=apart.split(',')[-3]
        lati=apart.split(',')[-2]
        longi=apart.split(',')[-1]
        query_list=re.findall(r'\d+', apart)
        if len(query_list)>2:
            apt=query_list[0]
            street_number=query_list[1]
        else:
            apt=''
            street_number=query_list[0]
        street_name = apart.split(',')[0]
        q1 = request.POST.get('question1')
        q2 = request.POST.get('question2')
        q3 = request.POST.get('question3')
        q4 = request.POST.get('question4')
        q5 = request.POST.get('question5')
        q6 = request.POST.get('question6')


        # Retrieve other question values in the same way

        questionnaire = Questionnaire(apt=apt, street_number=street_number, street_name=street_name,
                                      q1=q1, q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,user=user,voter_name=person,ward=ward,pct=pct)
        questionnaire.save()
        filtered_rows = Votelatlon.objects.filter(latitude=lati, longitude=longi)
        for row in filtered_rows:
            row.visited='yes'
            row.save()


        response = render(request, 'mymaps/success.html')
        response["Access-Control-Allow-Origin"] = "*"  # Allow all origins (adjust as needed)
        response["Access-Control-Allow-Headers"] = "Content-Type"
        response["Access-Control-Allow-Methods"] = "GET"
        return response  # Redirect to a success page or render a response

def get_pct_by_ward(request):
    #global ward
    ward = request.GET.get('ward', None)
    
    if ward is not None:
        pct_values = Votelatlon.objects.filter(ward=ward).values_list('pct', flat=True).distinct()
        ##print('Pct values',pct_values)
        pct_list = list(pct_values)
        response_data = {'pct_list': pct_list}
        response = JsonResponse(response_data)
        response["Access-Control-Allow-Origin"] = "*"  # Allow all origins (adjust as needed)
        response["Access-Control-Allow-Headers"] = "Content-Type"
        response["Access-Control-Allow-Methods"] = "GET"
        return response
    else:
        return JsonResponse({'error': 'Ward parameter is missing'})
def get_street_by_pct(request):
    query_ward_pct = request.GET.get('st').split(',')
    ward=query_ward_pct[0]
    pct=query_ward_pct[1]
    
    if pct is not None:
        #print('Ward in pct function',ward)
        pct_values = Votelatlon.objects.filter(ward=ward,pct=pct).values_list('street_name', flat=True).distinct()
        ##print('St values',pct_values)
        st_list = list(pct_values)
        response_data = {'st_list': st_list}
        
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Ward parameter is missing'})
#-----------------------------------dashboard=============================
import json
from django.db.models import Count
from datetime import datetime, timedelta
from django.db.models import Q

# Get the start and end time range


from django.core.serializers.json import DjangoJSONEncoder

class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def dashboard_view(request):
    # Retrieve data from the Questionnaire model
    end_time = datetime.now()
      # Current time
    start_time = end_time - timedelta(minutes=4000)  # Subtract 24 hours from the current time
    #print(start_time)
    #print(end_time)

    # Filter the Questionnaire objects based on the time range
    questionnaire = Questionnaire.objects.filter(Q(created_at__range=(start_time, end_time)))

    questionnaires = Questionnaire.objects.all()
    ward_counts = questionnaires.values_list('ward', flat=True).distinct()
    pct_counts = questionnaires.values_list('pct', flat=True).distinct()
    user_counts = questionnaires.values_list('user', flat=True).distinct()
    voter_counts = questionnaires.values_list('voter_name', flat=True).distinct()
    record_time=questionnaires.values_list('created_at', flat=True)
    #dump in json
    distinct_wards = Questionnaire.objects.values_list('ward', flat=True).distinct()
    distinct_pcts = Questionnaire.objects.values_list('pct', flat=True).distinct()

    ward_counts_json=json.dumps(list(ward_counts))
    pct_counts_json=json.dumps(list(pct_counts))
    user_counts_json=json.dumps(list(user_counts))
    voter_counts_json=json.dumps(list(voter_counts))
    record_time_json=json.dumps(list(record_time),cls=CustomJSONEncoder)
    questionnaires_json = json.dumps(list(questionnaires.values()), cls=CustomJSONEncoder)

    context = {
        'questionnaires_json': questionnaires_json,
         'ward_counts_json': ward_counts_json,
         'pct_counts_json':pct_counts_json,
         'user_counts_json':user_counts_json,
         'voter_counts_json':voter_counts_json,
         'record_json':record_time_json,
          'distinct_wards': distinct_wards,
          'distinct_pcts': distinct_pcts,
    }
    return render(request, 'mymaps/dashboard.html', context)

from django.utils import timezone
#showing realtime reports
def dashboardview(request):
    if request.method == "GET":
        # Retrieve the start and end times from the request parameters
        timehour = request.GET.get('hour')
        #print(timehour)
        end_time = datetime.now()  # Current time
        start_time = end_time - timedelta(hours=int(timehour))

        # Retrieve the Questionnaire objects based on the time range
        questionnaire = Questionnaire.objects.filter(Q(created_at__range=(start_time, end_time)))

        # Convert the Questionnaire objects to JSON
        questionnaires_json = list(questionnaire.values())

        # Return the JSON response
        return JsonResponse(questionnaires_json, safe=False)
#filtering by ward and pct
def filterbywardpct(request):
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            ward = data.get('wardd')
            pct = data.get('pctt')
            #print(f'Ward: {ward}')
            #print(f'PCT: {pct}')
            questionair=Questionnaire.objects.filter(ward=ward,pct=pct).values_list()
            # Perform further processing with the ward and pct values
            questionnaires_json = list(questionair.values())
            
            # Return a JSON response if needed
            
            return JsonResponse(questionnaires_json,safe=False)
def get_pcts(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ward = data.get('ward')
        #print(f'GET PCTS WARD {ward}')

        # Perform filtering based on the selected ward to retrieve the corresponding PCT values
        filtered_pcts = Questionnaire.objects.filter(ward=ward).values_list('pct', flat=True).distinct()

        # Convert the queryset to a list
        pcts_list = list(filtered_pcts)

        return JsonResponse(pcts_list, safe=False)

    return JsonResponse({'message': 'Invalid request method'}, status=400)

#----------------------------TEXTUAL Data----------------------#
@login_required

def textualcontrol(request):
    
        
    return render(request, 'mymaps/textualdata.html')
#apis for textuatal data
def textualcontroldata(request):
    votelatlon = Votelatlon.objects.all()
    votelatlon_json = list(votelatlon.values())

    distinct_wards = Votelatlon.objects.values_list('ward', flat=True).distinct()
    distinct_pcts = Votelatlon.objects.values_list('pct', flat=True).distinct()
    distinct_st = Votelatlon.objects.values_list('street_name', flat=True).distinct()

    context = {
        'votelatlon_json': votelatlon_json,
        'distinct_wards': list(distinct_wards),
        'distinct_pcts': list(distinct_pcts),
    }
    

    return JsonResponse(context)
#-------------------------------------Edit Database ------------------------------------------

@login_required
def datacontrol(request):
    if request.user.is_superuser:
        questionnaires = Questionnaire.objects.all()

        questionnaires_json = json.dumps(list(questionnaires.values()))
        distinct_wards = Questionnaire.objects.values_list('ward', flat=True).distinct()
        distinct_pcts = Questionnaire.objects.values_list('pct', flat=True).distinct()
        context = {
            'questionnaires_json': questionnaires_json,
            'distinct_wards': distinct_wards,
            'distinct_pcts': distinct_pcts,
            }
        return render(request, 'mymaps/datacontrol.html',context)
    else:
        messages.error(request, 'ONly Admins Can Edit Data')
        return render(request, 'mymaps/dashboard.html')

import time
def submitdata(request):
    print('submit data called')

    if request.method=="POST":
        print('submit get data called')
        signal=request.GET.get('query')
        
        ward=request.POST.get('ward')
        pct=request.POST.get('pct')
        vn=request.POST.get('vn')
        apt=request.POST.get('apt')
        stn=request.POST.get('stn')
        
        sta=request.POST.get('sta')
        print('Street Number',stn)
        
        person=request.POST.get('person')
        q1 = request.POST.get('question1')
        q2 = request.POST.get('question2')
        q3 = request.POST.get('question3')
        q4 = request.POST.get('question4')
        q5 = request.POST.get('question5')
        q6 = request.POST.get('question6')
        print('Questions',q1,q2,q3,q4,q5,q6)
        #print(f'Running submit datat {ward,pct,sta,stn,zip}')
        questionnaire = Questionnaire(apt=apt, street_number=stn, street_name=sta,
                                      q1=q1, q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,user=person,voter_name=vn,ward=ward,pct=pct)
        questionnaire.save()
        questionaire=Questionnaire.objects.all()
        questionnaires_json = list(questionaire.values())

        if signal=='textual':
        
            filtered_rows = Votelatlon.objects.filter(apt_number=apt, street_name=sta,street_number=stn)
            for row in filtered_rows:
                row.visited='yes'
                row.save()
            response_data = {'message': 'Data submitted successfully'}
            return JsonResponse(response_data, status=200)        
        else:
            return JsonResponse(questionnaires_json, safe=False)

    return render(request, 'mymaps/datacontrol.html')
def edit_row_data(request):
    if request.method=="POST":
        row_id=request.POST.get('id')
        ward=request.POST.get('ward')
        pct=request.POST.get('pct')
        #apt=request.POST.get('apt')
        #street_no=request.POST.get('street_no')
        #street_name=request.POST.get('street_name')
        full_address=request.POST.get('full_address')
        user=request.POST.get('user')
        voter_name=request.POST.get('voter_name')
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        q4=request.POST.get('q4')
        q5=request.POST.get('q5')
        q6=request.POST.get('q6')
        row = Questionnaire.objects.filter(id=row_id).first()
        if row:
            #print(f'Ward is {ward} Pct{pct} Full address {full_address} User {user} Voter Name{voter_name} q1{q1} q2 {q2} q3{q3} q4{q4} q5{q6}')
        # Update the fields of the row with the new values
            row.ward = ward
            row.pct = pct
            #row.apt=apt
            #row.street_number=street_no
            #ow.street_name=street_name
            row.street_name=full_address
            row.user=user
            row.voter_name=voter_name
            row.q1=q1
            row.q2=q2
            row.q3=q3
            row.q4=q4
            row.q5=q5
            row.q6=q6
            row.save()

        questionaire=Questionnaire.objects.all()
        questionnaires_json = list(questionaire.values())
        return JsonResponse(questionnaires_json, safe=False)


#-------------------------------------------------------Backup data base-------------------------------------------
def restoredata(request):
    if request.method == "GET":
        # Retrieve the start and end times from the request parameters
        timehour = request.GET.get('hour')
        #print(timehour)
        end_time = time_zone()  # Current time
        start_time = end_time - timedelta(hours=int(timehour))
        #print(f'end time {start_time}')
        # Retrieve the Questionnaire objects based on the time range
        questionnaire = Questionnaire.objects.filter(Q(created_at__range=(start_time, end_time)))
        questionnaire.delete()
        #print(f'Timezone is {time_zone()}')
        questionnaire = Questionnaire.objects.all()

        # Convert the Questionnaire objects to JSON
        questionnaires_json = list(questionnaire.values())

        # Return the JSON response
        return JsonResponse(questionnaires_json, safe=False)
    #---------------------------------Reseting the data
def resetdata(request):
    if request.method=='GET':
        questionnaire=Questionnaire.objects.all()
        questionnaire.delete()
        questionnaire = Questionnaire.objects.all()

        # Convert the Questionnaire objects to JSON
        questionnaires_json = list(questionnaire.values())

        # Return the JSON response
        return JsonResponse(questionnaires_json, safe=False)
    
#-------------------------------------Authentication----------------------------------------
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User


def auth(request):
    return render(request,'mymaps/auth.html')
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email,email=email, password=password)
        print('Login successful')
        if user is not None:
            # User credentials are valid, log in the user
            login(request, user)
            print('Login successful')

            return HttpResponse(status=303, content='', headers={'Location': '/datacontrol.html'})
        else:
            # User credentials are invalid, show an error message or handle the authentication failure
            return HttpResponse(status=404, content='', headers={'Location': '/auth.html'})

    return render(request, 'mymaps/auth.html')
from django.urls import reverse

def register_view(request):
    if request.method == 'POST':
        print('register is working')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Add your code to create a new user account with the provided email and password
            # For example, you can use Django's built-in User model to create the user:
            user = User.objects.create_user(username=email, email=email, password=password)

            # After creating the user, log them in
            login(request, user)
            print('register successful')

            return HttpResponse(status=303, content='', headers={'Location': '/datacontrol.html'})
        else:
            # Passwords do not match, handle the error
            return render(request, 'auth.html', {'error': 'Passwords do not match.'})
        

    return HttpResponse(status=404, content='', headers={'Location': '/auth.html'})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return render(request, 'mymaps/auth.html')
    #return render(request, 'register.html', {'form': form})
def login_vieww(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the next page
        next_page = request.GET.get('next')
        if next_page:
            return redirect(next_page)
        else:
            return redirect('mymaps/auth.html')  # Change 'dashboard' to the desired default page URL name

    # If the user is not logged in, handle the login logic here...
    # Your login logic here...

    return render(request, 'mymaps/auth.html')
'''    
def main():
    
    #print("trying to inject")
    inject_voters_from_csv()
    #print(f'sucess added')
    ##print('starting to delete')
    
main()'''


