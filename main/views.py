
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings
import os


class myUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(myUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about_me(request):
    return render(request, 'main/about_me.html')

def my_server(request):
    return render(request, 'main/my_server.html')

def download_cv(request):
    path = os.path.join(settings.BASE_DIR, 'main', 'media', 'cv_elmeri.pdf')
    return FileResponse(open(path, 'rb'), content_type='application/pdf')


def register(request):
    if request.method == 'POST':
        form = myUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main/home')
    else:
        form = myUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
