from django.db import models
from django.contrib.auth.models import  AbstractUser

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
    
    # Date fields
    date_of_birth = models.DateField(null=True, blank=True)
 
    def __str__(self) -> str:
        return self.user.username + " " + self.Designation
