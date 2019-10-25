from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import *
from django.db.models import Count


#page d'accueil
def index(request):
    return render(request, 'galerie/index.html')


def inscription(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form= RegistrationForm()
        context={
        'form': form,
    }
    return render(request, 'registration/registration.html', context)

