from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMultiAlternatives
import os
from django.conf import settings
from testapp.models import Course, Resume

from django.views.generic import DetailView
from easy_pdf.views import PDFTemplateView,PDFTemplateResponseMixin
# Create your views here.

def index(request):
    return render(request,'index.html')

def course_view(request):
    course_list=Course.objects.all()
    context={
        'course_list':course_list
    }

    return render(request,"course.html",context)


def add_course(request): #task="Playing cricket"
    t=Course(addcourse=request.POST.get('addcourse'))
    t.save()
    return redirect("/course")


def delete_one_data(request,id):
    one_course=Course.objects.get(id=id)
    one_course.delete()
    return redirect("/course")

def fetch_resume_data(request,id):#id=1
    resume_list=Resume.objects.get(id=id)
    context={
        'resume_list':resume_list
    }
    return render(request,"resume.html",context)


def create_resume_form(request):
    if request.method == "POST":
        summary=request.POST.get('summary')
        name=request.POST.get('name')
        phoneno=request.POST.get('phoneno')
        email=request.POST.get('email')
        company=request.POST.get('company')
        duration=request.POST.get('duration')
        projects=request.POST.get('projects')
        skills=request.POST.get('skills')
        softwares=request.POST.get('softwares')
        certifications=request.POST.get('certifications')
        achievements=request.POST.get('achievements')
        strengths=request.POST.get('strengths')
        weakness=request.POST.get('weakness')
        schoolname=request.POST.get('schoolname')
        schoolduration=request.POST.get('schoolduration')
        schoolmarkspercentage=request.POST.get('schoolmarkspercentage')
        collegename=request.POST.get('collegename')
        collegeduration=request.POST.get('collegeduration')
        collegeuniversity=request.POST.get('collegeuniversity')
        collegemarkspercentage=request.POST.get('collegemarkspercentage')
        languages=request.POST.get('languages')

        r=Resume(summary=summary,name=name,phoneno=phoneno,emailid=email,skills=skills,
        softwares=softwares,company=company,experience=duration,projects=projects,
        certification=certifications,achievements=achievements,strengths=strengths,
        weakness=weakness,schoolname=schoolname,schoolduration=schoolduration,percentageofschoolmarks=schoolmarkspercentage,
        collegename=collegename,collegeduration=collegeduration,percentageofcollegemarks=collegemarkspercentage,
        collegeuniversity=collegeuniversity,languagesknown=languages)
        r.save()
        return redirect("/home")
        
    return render(request,"resumeform.html")  


def home_view(request):
    all_resume=Resume.objects.all()
    return render(request,"home.html",{'all_resume':all_resume})



class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = Resume
    template_name = 'user_detail.html'
    context_object_name = "obj"

def delete_resume(request,id):
    resume=Resume.objects.get(id=id)
    resume.delete()
    return redirect("/create")

@login_required
def java(request):
    return render(request,"java.html")

@login_required
def python(request):
    return render(request,"python.html")

@login_required
def aptitude(request):
    return render(request,"aptitude.html") 

@login_required
def Cpp(request):
    return render(request,"Cpp.html") 

@login_required
def Sql(request):
    return render(request,"Sql.html") 

@login_required
def Bootstrap(request):
    return render(request,"Bootstrap.html") 

@login_required
def Ruby(request):
    return render(request,"Ruby.html")
        
@login_required
def DotNet(request):
    return render(request,"DotNet.html")

@login_required
def Subscrib(request):
    return render(request,"subscrib.html")  


def Subscrib(request):
    if request.method=='POST':
        sub=request.POST.get('subject')
        msg=request.POST.get('body')
        message=send_mail(sub,msg , settings.EMAIL_HOST_USER,['vinodamveena@gmail.com',])
    return render(request,'Subscribe.html')

def contact(request):
    return render(request,'contact.html')

def logout(request):
    return render(request,"logout.html")