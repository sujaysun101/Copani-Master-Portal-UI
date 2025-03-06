from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import admin
from django.urls import path
from master_portal_app import views

def master_portal(request):
    model_0_url = reverse('model_0')
    model_1_url = reverse('model_1')
    model_2_url = reverse('model_2')
    return render(request, 'master_portal.html', {
        'model_0_url': model_0_url,
        'model_1_url': model_1_url,
        'model_2_url': model_2_url,
    })

def model_0_ui(request):
    return HttpResponseRedirect(reverse('model_0'))

def model_1_ui(request):
    return HttpResponseRedirect(reverse('model_1'))

def model_2_ui(request):
    return HttpResponseRedirect(reverse('model_2'))

# Create your views here.
