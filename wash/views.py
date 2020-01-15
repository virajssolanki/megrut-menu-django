from django.shortcuts import render
from django.shortcuts import render, redirect
from order.forms import ReportBugForm

def wash(request):
	return render(request, 'wash/home.html')