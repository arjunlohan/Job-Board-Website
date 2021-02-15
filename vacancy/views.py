from django.shortcuts import render
from .models import Vacancy as vacancy_model
from resume.models import Resume as resume_model
from vacancy.models import Vacancy as vacancy_model
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def vacancyview(request):
    return render(request, 'Vacancy list.html', context={'vacancies': vacancy_model.objects.all()})


def vacancycreate(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            description = request.POST.get('description', False)
            vacancy_model.objects.create(author=request.user, description=description)
            return render(request, 'main_page.html')
        else:
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=403)
