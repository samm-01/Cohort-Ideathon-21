from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from django.utils import timezone #k

# Create your models here.


class contact(models.Model):
    Full_Name = models.CharField(max_length=120)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    Email_Id = models.EmailField(max_length=12000)
    Batch = models.CharField(max_length=12)
    Username = models.CharField(
        max_length=120, null=True, blank=True, unique=True)
    Password = models.CharField(max_length=120)
    # user = models.OneToOneField(
    #     User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Full_Name

# contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)


class ProjectInput(models.Model):

    project_name = models.CharField(max_length=30)
    # project_category = models.ForeignKey(ProjectInput,on_delete = models.CASCADE)
    project_info = models.CharField(max_length=120000000000000000)
    project_category = models.CharField(max_length = 120, default = "Others")
    project_image = models.ImageField(
        upload_to="images", null=True, blank=True)
    project_date = models.DateField(auto_now_add=True)  # kriti
    project_time = models.TimeField(auto_now_add=True)  # kriti

    def __str__(self):
        return self.project_name


class InterviewInput(models.Model):

    interview_info = models.CharField(max_length=120000000000000000)
    interview_category = models.CharField(max_length = 120, default = "Others")
    interview_image = models.ImageField(upload_to="images", null=True, blank=True)
    interview_date = models.DateField(auto_now_add=True)  # kriti
    interview_time = models.TimeField(auto_now_add=True)  # kriti

    # def __str__(self):
    #     return self.Full_Name
