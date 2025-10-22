from django.contrib.auth.models import User
from django.db import models

# Create your models here.sq


class Student(models.Model):
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    email=models.CharField(max_length=200)
    phone_number= models.CharField(max_length=200)
    place=models.CharField(max_length=200,default="")
    city=models.CharField(max_length=200,default="")
    pincode=models.CharField(max_length=200,default="")
    state=models.CharField(max_length=200,default="")
    upload_photo=models.CharField(max_length=200)
    USER=models.OneToOneField(User,on_delete=models.CASCADE)

class Company(models.Model):
    name=models.CharField(max_length=200)
    icon=models.CharField(max_length=250)
    email=models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    pincode=models.CharField(max_length=200)
    year = models.CharField(max_length=200, default="")
    status=models.CharField(max_length=200, default='pending')
    license=models.CharField(max_length=200, default="")
    USER=models.OneToOneField(User,on_delete=models.CASCADE)


class Internship(models.Model):
    name=models.CharField(max_length=200)
    title= models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    i_status=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="")
    type=models.CharField(max_length=200,default="")
    COMPANY = models.ForeignKey(Company, on_delete=models.CASCADE)
#
class Application(models.Model):
    applied_date= models.DateField()
    status=models.CharField(max_length=200)
    INTERNSHIP=models.ForeignKey(Internship,on_delete=models.CASCADE)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)

class Task(models.Model):
    title= models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    assigned_date = models.DateField()
    due_date=models.DateField()
    INTERNSHIP = models.ForeignKey(Internship, on_delete=models.CASCADE)
    APPLICATION=models.ForeignKey(Application,on_delete=models.CASCADE,default='')

class Report(models.Model):
    title= models.CharField(max_length=200)
    content=models.CharField(max_length=200)
    report_date=models.DateField()
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    TASK = models.ForeignKey(Task, on_delete=models.CASCADE)

class Certificate(models.Model):
    title= models.CharField(max_length=200)
    issued_date = models.DateField()
    file_path=models.CharField(max_length=200)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    INTERNSHIP = models.ForeignKey(Internship, on_delete=models.CASCADE)

class Complaint(models.Model):
    complaint=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    date=models.DateField()
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)









