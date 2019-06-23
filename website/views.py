from django.shortcuts import render
from django.shortcuts import render, redirect
from order.forms import ReportBugForm
from order.models import Bugs
from django.contrib import messages

def website(request):
	return render(request, 'website/home.html')

def privacy_policy(request):
	return render(request, 'website/privacy_policy.html')

def report_bugs(request):
	if request.method == 'POST':
		form = ReportBugForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'THANKS! ')
			return redirect('order_home')
	else:
		form = ReportBugForm()
	return render(request, 'order/order_home.html', {'form':form})