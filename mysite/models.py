from django.db import models
from email.policy import default

# Create your models here.
class Socity_Members(models.Model):
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=25, default=000)
    age=models.IntegerField()
    house_no=models.CharField(max_length=25)
    pic=models.FileField(upload_to='media', default='k.jpg')
    
    def __str__(self) -> str:
        return self.name

class Events(models.Model):
    event_name=models.CharField(max_length=25)
    # date=models.DateField(auto_now_add=False)
    event_date=models.CharField(max_length=25)
    event_information=models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.event_name

class Visitors(models.Model):
    visitor_name=models.CharField(max_length=25)
    # date=models.DateField(auto_now_add=False)
    visit_date_and_time=models.CharField(max_length=25)
    exit_time=models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.visitor_name

class Watchman(models.Model):
    watchman_name=models.CharField(max_length=25)
    # date=models.DateField(auto_now_add=False)
    watchman_date_and_time=models.CharField(max_length=25)
    # exit_time=models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.watchman_name

class Notice(models.Model):
    notice_name=models.CharField(max_length=25)
    # date=models.DateField(auto_now_add=False)
    notice_date=models.CharField(max_length=25)
    notice_information=models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.notice_name

class Complaint(models.Model):
    notice_name=models.CharField(max_length=25)
    notice_date=models.CharField(max_length=25)
    notice_information=models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.notice_name

# class Product_manager(models.Model)