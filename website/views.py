from django.shortcuts import render
from django.shortcuts import render, redirect

def website(request):
	return render(request, 'website/home.html')

def privacy_policy(request):
	return render(request, 'website/privacy_policy.html')