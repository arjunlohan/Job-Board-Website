from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Resume as resume_model
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse

def main(request):
    return render(request, 'main_page.html')


def resumeview(request):
    return render(request, 'Resume list.html', context={'resumes': resume_model.objects.all()})


class MySignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'Sign up page.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'Login page.html'


home_page_link = ['vacancy/new', 'resume/new']


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Personal profile.html', context={'links': home_page_link})


def resumecreate(request):
    if request.user.is_authenticated:
        description = request.POST.get('description', False)
        resume_model.objects.create(author=request.user, description=description)
        return render(request, 'main_page.html')
    else:
        return HttpResponse(status=403)
