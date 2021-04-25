from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.form import BookForm
from testapp.models import Book
from django.core.mail import send_mail,EmailMultiAlternatives
import os
from django.conf import settings
# Create your views here.


def home(request):
    return render(request,"home.html")


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

@login_required
def index(request):
    shelf=Book.objects.all() #select all from book

    return render(request,'index.html',{'book_shelf':shelf})

def upload(request):
    #using model form to specify the view
    obj=BookForm()

    if request.method=='POST':
        # once the form is sumbitted,fetch form params using request
        obj=BookForm(request.POST,request.FILES)
        #to validate form fields
        if obj.is_valid():
            # save the accepted /form data
            obj.save()
            return redirect('index')

        else:
            return HttpResponse("something wrong,reload <a href='{{url:'index'}}'>reload</a>")
    
    else:
        #if form is loaded first time
        return render(request,'upload.html',{'upload_form':obj})

def update(request,book_id):
    # convert it to string
    book_id=int(book_id)

    try:
        # using id to fetch particular book details to update 
        book_select=Book.objects.get(id=book_id)

    except Book.DoesNotExist:
        return redirect('home')

    else:
        # to displaying form with filled data
        book_form=BookForm(request.POST or None,instance=book_select)

        #after updating the all fields, user will submit form
        if book_form.is_valid():
            old_image = ""
            if book_select.picture:
                old_image = book_select.picture.path
                #data/fields are updated 
                form = BookForm(request.POST,request.FILES,instance = book_select)
                if form.is_valid():
                    #if you found image at specified location , remove it
                    if os.path.exists(old_image):
                        os.remove(old_image)
                        #updated fields will be saved
                        form.save()
            return redirect('index')
        return render(request,'upload.html',{'upload_form':book_form})  
def delete(request,book_id):
    # convert it to string
    book_id=int(book_id)
    
    try:
        #id is autogenerated field 
        #using id to fetch particular book details to update
        book_select=Book.objects.get(id=book_id)

    except Book.DoesNotExist:
        return redirect('index')

    book_select.delete()
    return redirect('home')

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





