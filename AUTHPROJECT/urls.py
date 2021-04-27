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
    path('',views.page),
    path('home/', views.home,name="home"),
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('index/',views.upload,name='upload-book'),
    path('upload/',views.upload,name='upload-book'),
    path('update/<int:book_id>',views.update,name='update_book'),
    path('delete/<int:book_id>',views.delete,name='delete_book'),
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
    path('upload/', views.upload),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', views.contact),
    path('logout/', views.logout),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
