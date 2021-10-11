from django.db import models
from django.contrib.auth.models import User


# Create your models here.

GENDER = [
    ("M", "MALE"),
    ("F", "FEMALE"),
]

EVIDENCECATEGORY = [
    ("Physical", "Physical"),
    ("Logical", "Logical"),
]


RANK = [
    ("Captain", "Captain"),
    ("Major", "Major"),
    ("General", "General"),
    ("Major General", "Major General"),
]


CRIMETYPE = [
    ("Robbery", "Robbery"),
    ("Violent", "Violent"),
    ("Murder", "Murder"),
    ]
STATUS = [
    ("Pending", "Pending"),
    ("Studied", "Studied"),
    ("Finished", "Finished"), 
]
VOTE = [
    ("Yes", "YES"),
    ("No", "NO"),
]

WHERE = [
    ("I was there at crime scene", "I was there at crime scene"),
    ("I were at work", "I were at work"),
    ("I was Near the crime scene", "I was Near the crime scene"),
    ("I was Too Far in different district", "I was Too Far in different district"),
]

REASON = [
    ("I was there", "I was there"),
    ("I don't know", "I don't know"),
    ("I know the Victim", "I know the Victim"),
    ("I've met with the Victim", "I've met with the Victim"),
]

class Province(models.Model):
    prov_name = models.CharField(max_length=30)

    def __str__(self):
        return self.prov_name


class District(models.Model):
    dist_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.dist_name

class Sector(models.Model):
    sect_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.sect_name

class Cell(models.Model):
    cel_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.cel_name

class Village(models.Model):
    vil_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.vil_name



class RIBStation(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=30, blank=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    def __str__(self):
        return self.station_name


class Officer(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    OfficerNationalId = models.CharField(max_length=16, blank=False)
    f_name = models.CharField(max_length=30, blank=False)
    l_name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=10, blank=False)
    email = models.CharField(max_length=50, blank=False)
    officerimage = models.ImageField(upload_to='images/', max_length=154, blank=True, null=True)
    rank = models.CharField(max_length=30, choices=RANK)
    recruit_year = models.IntegerField()
    def __str__(self):
        return self.f_name 

class Evidence(models.Model):
    evidenceCategory = models.CharField(max_length=15, choices=EVIDENCECATEGORY, default="Select Category")
    evidence_note = models.CharField(max_length=255)
    points =  models.CharField(max_length=10, blank=False)
    officerimage = models.ImageField(upload_to='images/', max_length=154, blank=True, null=True)
    
    def __str__(self):
        return self.evidenceCategory
class Reporter(models.Model):
    reporterNID = models.CharField(max_length=16, blank=False)
    f_name = models.CharField(max_length=30, blank=False)
    l_name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    email = models.CharField(max_length=30, blank=False)
    phone =  models.CharField(max_length=10, blank=False)
    relation = models.CharField(max_length=30, blank=False)   
    vote = models.CharField(max_length=3, choices=VOTE)
    # suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE)
    note = models.TextField(max_length=100, blank=True)
    
  
    def __str__(self):
        return self.f_name  

class Suspect(models.Model):
    suspectNID = models.CharField(max_length=16, blank=False)
    f_name = models.CharField(max_length=30, blank=False)
    l_name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    dob = models.DateField()
    phone =  models.CharField(max_length=10, blank=False)
    date_arrested = models.DateTimeField(auto_now_add=True,null=True) 
    relation = models.CharField(max_length=30, blank=False)   
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    cell = models.CharField(max_length=100, blank=True)
    village = models.CharField(max_length=100, blank=True)
    note = models.CharField(max_length=150, blank=False)
    evidences = models.ManyToManyField(Evidence, blank=True, null=True)
    reporters = models.ManyToManyField(Reporter, blank=True, null=True)

  
    def __str__(self):
        return self.f_name  

class Case(models.Model):
    case_name = models.CharField(max_length=7)
    victim_name = models.CharField(max_length=90, blank=True, null=True)
    reporter_name = models.CharField(max_length=90, blank=True, null=True)
    reporter_phone = models.CharField(max_length=10, blank=True, null=True)
    victim_address = models.CharField(max_length=90, blank=True, null=True)
    crimeType = models.CharField(max_length=15, choices=CRIMETYPE, default="Select Crime")
    case_desc = models.TextField()
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    suspects = models.ManyToManyField(Suspect, blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS)
    def __str__(self):
        return self.crimeType



class Admin(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    adminNationalId = models.CharField(max_length=16, blank=False)
    f_name = models.CharField(max_length=30, blank=False)
    l_name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=10, blank=False)
    email = models.CharField(max_length=50, blank=False)
    adminimage = models.ImageField(upload_to='images/', max_length=154, blank=True, null=True)
    def __str__(self):
        return self.f_name 

class RIBHeadquarter(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=30, blank=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
  
    
    def __str__(self):
        return self.station_name  


class StationUser(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    officerNationalId = models.CharField(max_length=16, blank=False)
    f_name = models.CharField(max_length=30, blank=False)
    l_name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=10, blank=False)
    email = models.CharField(max_length=50, blank=False)
    rank = models.CharField(max_length=30, choices=RANK)
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=5, blank=False)
    station = models.ForeignKey(RIBStation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.f_name 



class MurderQuestions(models.Model):
    suspectNID = models.CharField(max_length=16, blank=False)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=3, choices=VOTE) 
    q2 = models.CharField(max_length=50, choices=WHERE)
    q6 = models.CharField(max_length=3, choices=VOTE)
    q3 = models.CharField(max_length=3, choices=VOTE)
    q4 = models.CharField(max_length=3, choices=VOTE)
    q5 = models.CharField(max_length=10, blank=False)
    date_arrested = models.DateTimeField(auto_now_add=True,null=True) 
    vote = models.CharField(max_length=3, choices=VOTE)  
    q7 = models.CharField(max_length=3, choices=VOTE)
    q8 = models.DateField()
    q9 = models.CharField(max_length=100, blank=True) 
    q10 = models.CharField(max_length=100, blank=True) 
    q11 = models.CharField(max_length=3, choices=VOTE) 
    q12 = models.CharField(max_length=10, blank=False)
    q13 = models.CharField(max_length=100, choices=REASON) 
    q14 = models.CharField(max_length=100, blank=True)
    q15 = models.CharField(max_length=300, blank=True)
    q16 = models.CharField(max_length=1, blank=True)
    note = models.CharField(max_length=150, blank=False)
    suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE, null=True, blank=True)

    
  
    def __str__(self):
        return self.suspectNID 

class ViolentQuestions(models.Model):
    suspectNID = models.CharField(max_length=16, blank=False)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=3, choices=VOTE) 
    q2 = models.CharField(max_length=50, choices=WHERE)
    q6 = models.CharField(max_length=3, choices=VOTE)
    q3 = models.CharField(max_length=3, choices=VOTE)
    q4 = models.CharField(max_length=3, choices=VOTE)
    q5 = models.CharField(max_length=10, blank=False)
    date_arrested = models.DateTimeField(auto_now_add=True,null=True) 
    vote = models.CharField(max_length=3, choices=VOTE)  
    q7 = models.CharField(max_length=3, choices=VOTE)
    q8 = models.DateField()
    q9 = models.CharField(max_length=100, blank=True) 
    q10 = models.CharField(max_length=100, blank=True) 
    q11 = models.CharField(max_length=3, choices=VOTE) 
    q12 = models.CharField(max_length=10, blank=False)
    q13 = models.CharField(max_length=100, choices=REASON) 
    q14 = models.CharField(max_length=100, blank=True)
    q15 = models.CharField(max_length=300, blank=True)
    q16 = models.CharField(max_length=1, blank=True)
    note = models.CharField(max_length=150, blank=False)
    suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE, null=True, blank=True)

  
    def __str__(self):
        return self.suspectNID

class RobberyQuestions(models.Model):
    suspectNID = models.CharField(max_length=16, blank=False)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=3, choices=VOTE) 
    q2 = models.CharField(max_length=50, choices=WHERE)
    q6 = models.CharField(max_length=3, choices=VOTE)
    q3 = models.CharField(max_length=3, choices=VOTE)
    q4 = models.CharField(max_length=3, choices=VOTE)
    q5 = models.CharField(max_length=10, blank=False)
    date_arrested = models.DateTimeField(auto_now_add=True,null=True) 
    vote = models.CharField(max_length=3, choices=VOTE)  
    q7 = models.CharField(max_length=3, choices=VOTE)
    q8 = models.DateField()
    q9 = models.CharField(max_length=100, blank=True) 
    q10 = models.CharField(max_length=100, blank=True) 
    q11 = models.CharField(max_length=3, choices=VOTE) 
    q12 = models.CharField(max_length=10, blank=False)
    q13 = models.CharField(max_length=100, choices=REASON) 
    q14 = models.CharField(max_length=100, blank=True)
    q15 = models.CharField(max_length=300, blank=True)
    q16 = models.CharField(max_length=1, blank=True)
    note = models.CharField(max_length=150, blank=False)
    suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE, null=True, blank=True)

    
  
    def __str__(self):
        return self.suspectNID