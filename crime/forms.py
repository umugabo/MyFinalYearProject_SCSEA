from django.forms import ModelForm
from django import forms
from datetime import date
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Case,Suspect,Evidence,RIBStation,Officer,Reporter

class DateInput(forms.DateInput):
    input_type = 'date'

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        # fields = '__all__'
        fields = ('case_name','crimeType','case_desc','officer','status')
        labels = {
            'case_name':'Case Name',
            'crimeType':'Type Of Crime',
            'case_desc':'Case Description',
            'officer':'Case Officer',
            'status':'Case Status',
            }
class RibstationForm(forms.ModelForm):
    class Meta:
        model = RIBStation
        fields = ('user','station_name','province')
        labels = {
            'user':'Station user',
            'station_name':'Station Name',
            'province':'Province',
            }

class SuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        # fields = '__all__'
        fields = ('suspectNID','f_name','l_name','gender','dob','phone','relation','father_name','mother_name','province','district','cell','village','note','case')
        labels = {
            'suspectNID':'Suspect Id',
            'f_name':'First Name',
            'l_name':'Last Name',
            'gender':'Gender',
            'dob':'Date Of Birth',
            'phone':'Phone Number',            
            'relation':'Relation to Crime',
            'father_name':'Father Name',
            'mother_name':'Mother Name',
            'province':'Province',
            'district':'District',
            'cell':'Cell',
            'village':'Village',
            'note':'Short Note',
            'case':'Case Type',
            }

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        # fields = '__all__'
        fields = ('evidenceCategory','evidence_note','suspect','officerimage','points')
        labels = {
            'evidenceCategory':'Evidence Category',
            'evidence_note':'Short note',
            'suspect':'Case Suspect',
            'officerimage':'Evidence Photo',
            'points':'Points Gainned',
            }

class OfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        # fields = '__all__'
        fields = ('user','OfficerNationalId','f_name','l_name','gender','phone','email','rank','recruit_year','officerimage')
        labels = {
            'user':'User Name',
            'OfficerNationalId':'Officer ID',
            'f_name':'Fist Name',
            'l_name':'Last Name',
            'gender':'Gender',
            'phone':'Phone',
            'email':'Email',
            'rank':'Rank',
            'recruit_year':'Join RIB Year',
            'officerimage':'Officer Photo',
            }

class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        # fields = '__all__'
        fields = ('reporterNID','f_name','l_name','gender','email','phone','relation','vote','note','suspect')
        labels = {
            'reporterNID':'Reporter Id',
            'f_name':'First Name',
            'l_name':'Last Name',
            'gender':'Gender',
            'email':'Email',
            'phone':'Phone Number',            
            'relation':'Your Relation with suspect',
            'vote':'Are you linking suspect to the case(Guilty)',
            'note':'Short Note',
            'suspect':'Who are you Reporting',
            }


class MurderQuestionaireForm(forms.ModelForm):
    class Meta:
        model = Suspect
        # fields = '__all__'
        fields = ('suspectNID','f_name','l_name','gender','dob','phone','relation','father_name','mother_name','province','district','cell','village','note','case')
        labels = {
            'suspectNID':'What is  your id?',
            'f_name':'Why are you suspected to this case?',
            'l_name':'Where were you when the crime was taking place?',
            'gender':'Are you related to the suspect',
            'dob':'Did you know the victim before?',
            'phone':'For how long have you been known eachother?',            
            'relation':'Relation to Crime',
            'father_name':'What do you know about the victm?',
            'mother_name':'Have you talked to the victim before his/her death?',
            'province':'Have you ever had conflicts with the victim?',
            'district':'When have you lastly seen the Victim',
            'cell':'What were you two doing?',
            'village':'Where were you?',
            'note':'Short Note on how the victim has been killed',
            'case':'How many marks can you get out of 10 the be the suspected Person?',
            }