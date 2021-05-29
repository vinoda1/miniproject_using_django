"""AUTHPROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from AUTHPROJECT import settings
from AUTHPROJECT.settings import *
#import views.py from book app
from testapp import views
urlpatterns = [
    path('',views.index,name="index"),
    path('admin/', admin.site.urls),
    path('fetch/<int:id>', views.fetch_resume_data),
    path('create/', views.create_resume_form),
    path('home/', views.home_view),
    path('detail/<int:pk>', views.PDFUserDetailView.as_view()),
    path('Subscribe/',views.Subscrib),
    path('java/', views.java),
    path('python/', views.python),
    path('aptitude/', views.aptitude),
    path('Cpp/', views.Cpp),
    path('Sql/', views.Sql),
    path('Bootstrap/', views.Bootstrap),
    path('Ruby/', views.Ruby),
    path('Dotnet/', views.DotNet),
    path('Subscrib/', views.Subscrib),
    path('course/', views.course_view),
    path('add/', views.add_course),
    path('delete/<int:id>/', views.delete_one_data),
    path('delete_resume/<int:id>/',views.delete_resume),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', views.contact),
    path('logout/', views.logout),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
