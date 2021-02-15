"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from resume import views as views_resume
from vacancy import views as views_vacancy
from resume.views import MainView as MainView
from resume.views import MySignUpView, MyLoginView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_resume.main),
    path('vacancies', views_vacancy.vacancyview),
    path('resumes',  views_resume.resumeview),
    path('signup', MySignUpView.as_view()),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('login', MyLoginView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('home', MainView.as_view()),
    path('resume/new',views_resume.resumecreate),
    path('vacancy/new',views_vacancy.vacancycreate)
]