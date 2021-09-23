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
    ("Theft", "Theft"),
    ("Violent", "Violent"),
    ("Fraud", "Fraud"),
    ("Cyber crime", "Cyber crime"),
    
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

class Case(models.Model):
    case_name = models.CharField(max_length=30)
    crimeType = models.CharField(max_length=15, choices=CRIMETYPE, default="Select Crime")
    case_desc = models.CharField(max_length=150)
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS, default="Pending")
    def __str__(self):
        return self.case_name


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
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    note = models.CharField(max_length=150, blank=False)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.f_name  


class Evidence(models.Model):
    evidenceCategory = models.CharField(max_length=15, choices=EVIDENCECATEGORY, default="Select Category")
    evidence_note = models.CharField(max_length=255)
    points =  models.CharField(max_length=10, blank=False)
    suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE)
    officerimage = models.ImageField(upload_to='images/', max_length=154, blank=True, null=True)
    
    def __str__(self):
        return self.evidenceCategory


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

class Reporter(models.Model):
    reporterNID = models.CharField(max_length=16, blank=False)
    f_name = models.CharField(max_length=30, blank=False)
    l_name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    email = models.CharField(max_length=30, blank=False)
    phone =  models.CharField(max_length=10, blank=False)
    relation = models.CharField(max_length=30, blank=False)   
    vote = models.CharField(max_length=3, choices=VOTE)
    suspect = models.ForeignKey(Suspect, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    
  
    def __str__(self):
        return self.f_name  


