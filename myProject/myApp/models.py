from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    
    USER = [
        ('admin','Admin'),
        ('viewer','Viewer'),
    ]
    user_type=models.CharField(max_length=100,null=True,choices=USER)
    
    def __str__(self):
        
        return f"{self.username}-{self.first_name}-{self.last_name}"

class BasicInfoModel(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    contact_No = models.CharField(max_length=100, null=True)
    Designation = models.CharField(max_length=100, null=True)
    Profile_Pic = models.ImageField(upload_to="Media/Profile_Pic", null=True)
    Carrer_Summary = models.CharField(max_length=100, null=True)
    Age = models.PositiveIntegerField(null=True)
    Gender = models.CharField(max_length=100, null=True)
    
    
    date_of_birth = models.DateField(null=True, blank=True)
 
    def __str__(self) -> str:
        return self.user.username + " " + self.Designation
    

class EducationModel(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Institute_name=models.CharField(max_length=100,null=True)
    Degree=models.CharField(max_length=100,null=True)
    Field_OfStudy=models.CharField(max_length=100,null=True)
    Start_date=models.DateField(null=True,blank=True)
    End_date=models.DateField(null=True,blank=True)

    class Meta:
        unique_together = ['user','Institute_name','Degree']

    def __str__(self):

        return f"{self.user.username}-{self.Degree}-{self.Institute_name}"
    
class ExperienceModel(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Company_name=models.CharField(max_length=100,null=True)
    Job_title=models.CharField(max_length=100,null=True)
    Description=models.TextField(max_length=100,null=True)
    Start_date=models.DateField(null=True,blank=True)
    End_date=models.DateField(null=True,blank=True)

    

    def __str__(self):

        return f"{self.user.username}-{self.Description}-{self.Company_name}"
    
class SkillModel(models.Model):


    Skill_Level=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('advanced','Advanced'),
    ]
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=100,null=True)
    skill_level=models.CharField(max_length=100,null=True,choices=Skill_Level)


    class Meta:
        unique_together = ['user','skill_name']

    def __str__(self):
        return f"{self.user.username}-{self.skill_name}"
    
class languageModel(models.Model):



    Proficiency_Level=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('advanced','Advanced'),
    ]
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    language_name=models.CharField(max_length=100,null=True)
    language_level=models.CharField(max_length=100,null=True,choices=Proficiency_Level)

    class Meta:
        unique_together = ['user','language_name']

    def __str__(self):

        return f"{self.user.username}-{self.language_name}"

class IntarestModel(models.Model):

    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    interest_name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.interest_name}"
    
class FieldOfStudyModel(models.Model):

    
    study_name=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.study_name}"

class DegreeModel(models.Model):

    DEGREE=[
        ('bachelor','Bachelor'),
        ('masters','Masters'),
        ('doctoret','Doctoret'),
        ('diploma','Diploma'),
    ]
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True,blank=True)
    degree_lebel=models.CharField(max_length=100,null=True, choices=DEGREE)

    def __str__(self):
        return f"{self.description}"

class InstituteNameModel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=512, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    established_year = models.PositiveIntegerField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
    
class IntermediateLanguageModel(models.Model):
    
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Language_Name=models.CharField(max_length=100,null=True)

    
    def __str__(self) -> str:
        return self.Language_Name

class IntermediateSkillModel(models.Model):
    
    My_Skill_Name=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.My_Skill_Name
       
class AddJobModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Job created by which user
    job_title = models.CharField(max_length=255,null=True)
    company_name = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    requirements = models.TextField(null=True)
    salary = models.CharField(max_length=255,null=True)
    posted_on = models.DateField(default=timezone.now,null=True)
    updated_on = models.DateField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.user.username})"
    
class JobApplication(models.Model):
    job = models.ForeignKey(AddJobModel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} applied for {self.job.job_title}" 