from django.shortcuts import render, redirect 
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponse
from django .http import HttpResponse,JsonResponse
from .models import *
import datetime
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from .forms import CaseForm,SuspectForm,EvidenceForm,RibstationForm,OfficerForm,ReporterForm,MurderQuestionaireForm,ViolentQuestionaireForm,RobberyQuestionaireForm

# Create your views here.

def error401(request):

    context = {}
    return render(request, 'crime/401.html', context)
@unauthenticated_user
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get()
            return redirect('loginOrg.html')
    context = {'form':form}
    return render(request,'crime/register.html', context)

@unauthenticated_user
def index(request):
	
	context = {}
	return render(request, 'crime/index.html', context)	

@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if RIBHeadquarter.objects.filter(user=user):
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('home_Hq')
            elif RIBStation.objects.filter(user=user):
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('home_Station')
            elif StationUser.objects.filter(user=user):
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('home_Officer')
			       
    else:
        form = AuthenticationForm()
    return render(request, 'crime/loginOrg.html', { 'form': form })



def logoutUser(request):
    logout(request)
    return redirect('login_view')

@login_required(login_url='login_view')
@allowed_users(allowed_roles=['RIBHeadquarter'])
def homeHq(request):
    cases = Case.objects.all()
    officers = Officer.objects.all()
    stations = RIBStation.objects.all()
    suspects = Suspect.objects.all()
    total_suspects = suspects.count()
    total_cases = cases.count()
    finished = cases.filter(status='Finished').count()
    pending = cases.filter(status='Pending').count()
    context = {'cases':cases, 'suspects':suspects,'stations':stations,
    'total_casess':total_cases,'finished':finished,'officers':officers,
    'pending':pending }

    return render(request, 'crime/DashboardHq.html', context)


@login_required(login_url='login_view')
@allowed_users(allowed_roles=['RIBStation'])
def homeStation(request):
    cases = Case.objects.all()
    suspects = Suspect.objects.all()
    total_suspects = suspects.count()
    total_cases = cases.count()
    finished = cases.filter(status='Finished').count()
    pending = cases.filter(status='Pending').count()
    context = {'cases':cases, 'suspects':suspects,
    'total_casess':total_cases,'finished':finished,
    'pending':pending }

    return render(request, 'crime/DashboardStation.html', context)

@login_required(login_url='login_view')
@allowed_users(allowed_roles=['StationUser'])
def homeOfficer(request):
    cases = Case.objects.all()
    suspects = Suspect.objects.all()
    total_suspects = suspects.count()
    total_cases = cases.count()
    finished = cases.filter(status='Finished').count()
    pending = cases.filter(status='Pending').count()
    context = {'cases':cases, 'suspects':suspects,
    'total_casess':total_cases,'finished':finished,
    'pending':pending }

    return render(request, 'crime/DashboardOfficer.html', context)

def createRIBStation(request):
	form = RibstationForm()
	if request.method == 'POST':
		form = RibstationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home_Hq')

	context = {'form':form}
	return render(request, 'crime/ribstation_Form.html', context)


def RIBstationList(request):
    stations = RIBStation.objects.all()
    return render(request, 'crime/RIBstationList.html', {'stations':stations})


def createOfficer(request):
	form = OfficerForm()
	if request.method == 'POST':
		form = OfficerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home_Hq')

	context = {'form':form}
	return render(request, 'crime/officer_form.html', context)

def officerList(request):
    officers = Officer.objects.all()
    return render(request, 'crime/officerList.html', {'officers':officers})

def caseList(request):
    cases = Case.objects.all()
    return render(request, 'crime/caseList.html', {'cases':cases})

def evidenceList(request):
    evidences = Evidence.objects.all()
    return render(request, 'crime/evidenceList.html', {'evidences':evidences})

def witnes(request, pk_susp):
    suspect = Suspect.objects.get(id=pk_susp)
    reporters = suspect.reporters.all()
    reporter_count = reporters.count()
    context = {'suspect':suspect,'reporters':reporters,'reporter_count':reporter_count}
    return render(request, 'crime/witness.html',context)

def suspect(request, pk_susp):
    suspect = Suspect.objects.get(id=pk_susp)
    evidences = suspect.evidences.all()
    evidence_count = evidences.count()
    context = {'suspect':suspect,'evidences':evidences,'evidence_count':evidence_count}
    return render(request, 'crime/suspect.html',context)

def suspectList(request):
    suspect = Suspect.objects.all()
    return render(request, 'crime/suspectList.html', {'suspect':suspect})

def createCase(request):
	form = CaseForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = CaseForm(request.POST)
		if form.is_valid():
			case = form.save(commit=False)
			case.status = 'Pending'
			case.save()
			return redirect('home_Station')

	context = {'form':form}
	return render(request, 'crime/case_form.html', context)

def updateCase(request, pk):

	case = Case.objects.get(id=pk)
	form = CaseForm(instance=case)

	if request.method == 'POST':
		form = CaseForm(request.POST, instance=case)
		if form.is_valid():
			form.save()
			return redirect('home_Station')

	context = {'form':form}
	return render(request, 'crime/case_form.html', context)

def deleteCase(request, pk):
	case = Case.objects.get(id=pk)
	if request.method == "POST":
		case.delete()
		return redirect('home_Station')

	context = {'item':case}
	return render(request, 'crime/deleteCase.html', context)


def createSuspect(request, case_pk):

	case = Case.objects.get(id=case_pk) 


	form = SuspectForm()
	if request.method == 'POST':
		form = SuspectForm(request.POST)
		if form.is_valid():
			suspect = form.save()
			case.suspects.add(suspect)
			return redirect('suspectList')

	context = {'form':form, 'case':case}
	return render(request, 'crime/suspect_form.html', context)

def viewCaseSuspects(request, case_pk):

	case = Case.objects.get(id=case_pk)
	suspects = case.suspects.all()

	context = {'suspects':suspects, 'case':case}
	return render(request, 'crime/caseSuspects.html', context)

def updateSuspect(request, case_pk):

	suspect = Suspect.objects.get(id=case_pk)
	form = SuspectForm(instance=suspect)

	if request.method == 'POST':
		form = SuspectForm(request.POST, instance=suspect)
		if form.is_valid():
			form.save()
			return redirect('suspectList')

	context = {'form':form}
	return render(request, 'crime/suspect_form.html', context)

def deleteSuspect(request, case_pk):
	suspect = Suspect.objects.get(id=case_pk)
	if request.method == "POST":
		suspect.delete()
		return redirect('suspectList')

	context = {'item':suspect}
	return render(request, 'crime/deleteSuspect.html', context)

def createEvidence(request, suspect_pk):
	suspect = Suspect.objects.get(id=suspect_pk)
	form = EvidenceForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = EvidenceForm(request.POST)
		if form.is_valid():
			evidence = form.save()
			suspect.evidences.add(evidence)
			return redirect('evidence')

	context = {'form':form, 'suspect':suspect}
	return render(request, 'crime/evidence_form.html', context)



def updateEvidence(request, pk):

	evidence = Evidence.objects.get(id=pk)
	form = EvidenceForm(instance=evidence)

	if request.method == 'POST':
		form = EvidenceForm(request.POST, instance=evidence)
		if form.is_valid():
			form.save()
			return redirect('evidence')

	context = {'form':form}
	return render(request, 'crime/evidence_Form.html', context)

def createReporter(request, suspect_pk):
	suspect = Suspect.objects.get(id=suspect_pk)
	form = ReporterForm()
	if request.method == 'POST':
		form = ReporterForm(request.POST)
		if form.is_valid():
			reporter = form.save()
			suspect.reporters.add(reporter)
			return redirect('home_Officer')

	context = {'form':form, 'suspect':suspect}
	return render(request, 'crime/reporter_form.html', context)

def reporterList(request):
    reporter = Reporter.objects.all()
    return render(request, 'crime/reportertList.html', {'reporter':reporter})

def createMurderForm(request):
	form = MurderQuestionaireForm()
	if request.method == 'POST':
		form = MurderQuestionaireForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'crime/MurderQuestionaireForm.html', context)

def createViolentForm(request):
	form = ViolentQuestionaireForm()
	if request.method == 'POST':
		form = ViolentQuestionaireForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'crime/ViolentQuestionaireForm.html', context)

def createRobberyForm(request):
	form = RobberyQuestionaireForm()
	if request.method == 'POST':
		form = RobberyQuestionaireForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'crime/RobberyQuestionaireForm.html', context)