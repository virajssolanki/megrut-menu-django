from django.shortcuts import render
from .forms import AddNumberForm
from .models import Number
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
@login_required
def numbers(request):
	numbers = Number.objects.all()
	return render(request, 'order/numbers.html', {'numbers':numbers})