# shipments/views.py
from django.shortcuts import render, redirect
from .models import Shipment
from .forms import ShipmentForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout

@login_required
def account_info(request):
    return render(request, 'shipment/account_info.html', {'user': request.user})

@login_required
def home(request):
    return render(request, 'shipment/home.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return render(request, 'shipment/logout.html')
@login_required

def view_shipments(request):
    shipments = Shipment.objects.filter(user=request.user)
    return render(request, 'shipment/view_shipments.html', {'shipments': shipments})
@login_required
def add_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.user = request.user
            shipment.save()
            return redirect('view_shipments')
    else:
        form = ShipmentForm()
    return render(request, 'shipment/add_shipment.html', {'form': form})

def update_shipment(request, shipment_id):
    shipment = Shipment.objects.get(pk=shipment_id)
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('view_shipments')
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'shipment/update_shipment.html', {'form': form, 'shipment': shipment})

def delete_shipment(request, shipment_id):
    shipment = Shipment.objects.get(pk=shipment_id)
    shipment.delete()
    return redirect('view_shipments')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view_shipments')
    else:
        form = SignUpForm()
    return render(request, 'shipment/sign_up.html', {'form': form})

@user_passes_test(lambda u: not u.is_authenticated, login_url='home')
def home_for_unauthenticated(request):
    return render(request, 'shipment/home.html')

def location_page(request):
    return render(request, 'shipment/location_page.html')