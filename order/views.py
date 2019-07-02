from django.shortcuts import render
from .forms import AddNumberForm, ReportBugForm
from .models import Number, Bugs
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def order_home(request):
	if request.method == 'POST':
		form = AddNumberForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'YOU ARE IN!')
			return redirect('order_home')
	else:
		form = AddNumberForm()
	return render(request, 'order/order_home.html', {'form':form})
	

def feedback(request):
	return render(request, 'order/chat.html')


@login_required
def numbers(request):
	numbers = Number.objects.all().order_by('-date_posted')
	bugs = Bugs.objects.all().order_by('-date_posted')
	context = locals()
	return render(request, 'order/numbers.html', context)