from django.db import models

class Resume(models.Model):
    profilepic=models.CharField(max_length=300)
    summary=models.TextField()
    name=models.CharField(max_length=100)
    phoneno=models.IntegerField()
    emailid=models.CharField(max_length=100)
    skills=models.TextField()
    softwares=models.TextField()
    company=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    projects=models.TextField()
    certification=models.CharField(max_length=100)
    achievements=models.TextField()
    strengths=models.CharField(max_length=100)
    weakness=models.CharField(max_length=100)
    schoolname=models.CharField(max_length=100)
    schoolduration=models.IntegerField()
    percentageofschoolmarks=models.IntegerField()
    collegename=models.CharField(max_length=100)
    collegeduration=models.IntegerField()
    percentageofcollegemarks=models.IntegerField()
    collegeuniversity=models.CharField(max_length=100)
    languagesknown=models.TextField()


class Course(models.Model):
    addcourse=models.CharField(max_length=100)