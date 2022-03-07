from django.forms import ModelForm
from django import forms
from datetime import date
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Crime,CAQS,CAQW,Answer,QuestionSuspect,QuestionReporter,StationUser, Case,Suspect,Evidence,RIBStation,Officer,Reporter


class RibOfficerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        
    def __init__(self, *args, **kwargs):
        super(RibOfficerRegistrationForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None
    def save(self, commit=True):
        user = super(RibOfficerRegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            
        return user



class StationNameRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        
    def __init__(self, *args, **kwargs):
        super(StationNameRegistrationForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None
    def save(self, commit=True):
        user = super(StationNameRegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            
        return user


class DateInput(forms.DateInput):
    input_type = 'date'

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        # fields = '__all__'
        fields = ('case_name','crimeType','victim_name','reporter_name','reporter_phone','victim_address','case_desc','stationuser', 'suspects')
        labels = {
            'case_name':'Case Code',
            'crimeType':'Type Of Crime',
            'victim_name':'Victim Name',
            'reporter_name':'Reporter Name',
            'reporter_phone':'Reporter Phone',
            'victim_address':'Address of the Victim',
            'case_desc':'Case Description',
            'stationuser':'Case Officer',
            }
class RibstationForm(forms.ModelForm):
    class Meta:
        model = RIBStation
        fields = ('user','station_name','province')
        labels = {
            'user':'Station Commander',
            'station_name':'Station Name',
            'province':'Province',
            }

class SuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        # fields = '__all__'
        fields = ('suspectNID','f_name','l_name','gender','dob','phone','relation','father_name','mother_name','province','district','cell','village','ribstation','note')
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
            'ribstation':'RIBStation',
            'note':'Short Note',
            }

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ('evidenceCategory','evidence_note','officerimage','points')
        labels = {
            'evidenceCategory':'Evidence Category',
            'officerimage':'Evidence Photo',
            'points':'Points Gainned',
            'evidence_note':'Short note',
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

class StationUserForm(forms.ModelForm):
    class Meta:
        model = StationUser
        # fields = '__all__'
        fields = ('user','nationalId','f_name','l_name','gender','phone','email','rank','recruit_year','officerimage')
        labels = {
            'user':'User Name',
            'nationalId':'Officer ID',
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
        fields = ('reporterNID','f_name','l_name','gender','email','phone','relation','vote','note')
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
            # 'suspect':'Who are you Reporting',
            }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionSuspect
        fields = ('questionId','questionName',)
        labels = {
            'questionId': 'Id of the Question',
            'questionName':'Describe the Question To Be Asked Suspects',
            }
        widgets = {
            'questionId': forms.TextInput(attrs={'value':'VIO'}),
            'questionName': forms.Textarea(attrs={'placeholder':'Question To be asked'})
        }

class QuestionRepoForm(forms.ModelForm):
    class Meta:
        model = QuestionReporter
        fields = ('questionId','questionName')
        labels = {
            'questionId': 'Id of the Question',
            'questionName':'Describe the Question To Be Asked Witness',
            }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('AnswerName',)
        labels = {
            'AnswerName':'Predict an Answer To Be Answered',
            }

class CAQSForm(forms.ModelForm):
    class Meta:
        model = CAQS
        fields = ('suspect','question','answer')
        labels = {
            'suspect':'What is your name? ',
            'question':'Question',
            'answer':'Your Answer',

            
            }

class CAQWForm(forms.ModelForm):
    class Meta:
        model = CAQW
        fields = ('witness','question','answer')
        labels = {
            'witness':'What is your name? ',
            'question':'Question',
            'answer':'Your Answer',

            
            }
            

class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ('crimeName',)
        labels = {
            'crimeName':'Describe the Crime Name',
            }