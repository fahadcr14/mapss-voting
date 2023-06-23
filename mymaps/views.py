from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'mymaps/index.html')
def questions(request):
    return render(request, 'mymaps/questions.html')

from django.test import TestCase

# Create your tests here.
import csv
from datetime import datetime
from .models import Voter,Voters_list
ward=''

def inject_voters_from_csv():
    i=0
    with open(r'C:\Users\cr7\Downloads\voterlist.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            voter = Voters_list(
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
                state=['State'],
                zip_code=row['Zip Code'],
                party_affiliation=row['Party Affiliation '],
                date_of_birth=datetime.strptime(row['Date of Birth '], '%m/%d/%Y').date(),
                voter_status=row['Voter Status']
            )
            voter.save()
            print(i)
            i+=1
def get_voter_data(request):
    strig=request.GET.get('query','').split(',')
    query=strig[0]
    ward=strig[1]
    pcts=strig[2]
    print('Voters data query ',strig)
    #voters = Voters_list.objects.all()
    voters=Voters_list.objects.filter(ward=ward,pct=pcts,street_name=query.upper()).values_list()
    data = list(voters.values())
    print('get voters data',data)
    lst=list()
    i=0
    
    for q in data:
        if query.upper()==q['street_name'] :
            #print(q)
            lst.append(q)
    return JsonResponse(lst, safe=False)
    #print(data[0])
import re
def get_persons(request):
    #query=request.GET.get('query','')
    #print(query)
    #voters = Voters_list.objects.all()
    strig=request.GET.get('query','').split(',')
    print('Get person ',strig)
    query=strig[0]
    ward=strig[1]
    pcts=strig[2]
    voters=Voters_list.objects.filter(ward=ward,pct=pcts).values_list()
    data = list(voters.values())
    names=[]
    i=0
    digit= re.findall(r'\d+', query)
    strng=re.split(r'\d+', query)
    #print(digit[0])
    correct_strng=strng[-1].lstrip()
    query_without_spaces=''.join(query.split())
    for q in data:
        #if int(digit[0])==q['street_number'] and correct_strng.upper()==q['street_name'] :
            #print(query)
            '''var2=query
            
            print(f'Len of query {var2} ,Len of Local {var1}')
            if len(var2)==len(var1):
                print(f'Here is matched{var1}={var2}')'''
            if q['apt_number']=='':
                var1=str(q['street_number'])+' '+q['street_name']+' '+q['zip_code']
            else:
                var1=str(q['street_number'])+' '+q['street_name']+' '+q['zip_code']
            var_no_space=''.join(var1.split())
            #print(query_without_spaces,'\n',var_no_space)
            if query_without_spaces==var_no_space:
                print(f'-----------Q in data-----------')
                print(q)
                print(f'-------------------------------')
                #print(f'matched')
                #print(q)
                #names.append({str(q['street_number'])+' '+q['street_name']:q['first_name']+' '+q['last_name']})
                names.append(q['first_name']+' '+q['last_name'])
            i+=1
            
    print(correct_strng,names)
    return JsonResponse(names,  safe=False)   

from .models import Questionnaire

def submit_questionnaire(request):
    if request.method == 'POST':
        apart = request.GET.get('query')
        query_list=re.findall(r'\d+', apart)
        print('Here is query list',query_list)
        if len(query_list)>2:
            apt=query_list[0]
            street_number=query_list[1]
        else:
            apt=''
            street_number=query_list[0]
        #street_number = request.GET.get('query')
        street_name = request.GET.get('query')
        q1 = request.POST.get('question1')
        q2 = request.POST.get('question2')
        q3 = request.POST.get('question3')
        q4 = request.POST.get('question4')
        q5 = request.POST.get('question5')
        #print(f'QUESTION 1 IS {q1}')

        # Retrieve other question values in the same way

        questionnaire = Questionnaire(apt=apt, street_number=street_number, street_name=street_name,
                                      q1=q1, q2=q2,q3=q3,q4=q4,q5=q5)
        questionnaire.save()

        return render(request, 'mymaps/success.html')  # Redirect to a success page or render a response

    return render(request, 'mymaps/questions.html')
def get_pct_by_ward(request):
    global ward
    ward = request.GET.get('ward', None)
    
    if ward is not None:
        pct_values = Voters_list.objects.filter(ward=ward).values_list('pct', flat=True).distinct()
        print('Pct values',pct_values)
        pct_list = list(pct_values)
        return JsonResponse({'pct_list': pct_list})
    else:
        return JsonResponse({'error': 'Ward parameter is missing'})
def get_street_by_pct(request):
    pct = request.GET.get('st', None)
    
    if pct is not None:
        print('Ward in pct function',ward)
        pct_values = Voters_list.objects.filter(ward=ward,pct=pct).values_list('street_name', flat=True).distinct()
        print('St values',pct_values)
        pct_list = list(pct_values)
        return JsonResponse({'pct_list': pct_list})
    else:
        return JsonResponse({'error': 'Ward parameter is missing'})
def main():
    '''print("trying to inject")
    inject_voters_from_csv()
    print(f'sucess added')'''
    print('starting to delete')
    
main()