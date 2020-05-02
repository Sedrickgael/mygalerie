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


@login_required 
def dashboard(request):
    context={
        'hotels':ReservationHotel.objects.raw('SELECT * FROM ref_reservationhotel, ref_etablissements WHERE ref_reservationhotel.etablissement_id=ref_etablissements.id AND ref_etablissements.responsable_id= %s ORDER BY date_reservation', [request.user.id ], ),
        
        }
    return render(request, 'registration/dashboard.html', context)

@login_required 
def home(request):
    context={
        'contenus': Contenu.objects.all().order_by('?'),
    }
    return render(request,'galerie/home.html', context)


@login_required 
def profile(request):
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user )
        if  form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        context={
            'form': form,
        }
    return render(request, 'galerie/profile.html',  context)

