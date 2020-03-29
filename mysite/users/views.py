from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import datetime

@login_required
def home(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {'today' : today})

#this will return the sign up page view
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log user in
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html',{'form':form})
