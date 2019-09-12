from django.shortcuts import render, redirect, get_object_or_404
import json
from django.http import HttpResponse
from .models import Post
from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages import constants as message_constants
from .forms import AddMenuForm
from django.contrib.auth.decorators import login_required
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
									message_constants.INFO: 'info',
									message_constants.SUCCESS: 'success',
									message_constants.WARNING: 'warning',
									message_constants.ERROR: 'danger',}

@login_required
def delete_menu(request, pk):
	menu = Post.objects.get(id=pk)
	menu.delete()
	messages.warning(request, f'MENU DELETED')
	return redirect('mymess', username=request.user)


@login_required
def add_menu(request):
	if request.method == "POST":
		form = AddMenuForm(request.POST)
		if form.is_valid():
			posts = Post.objects.filter(author=request.user)
			for i in posts:
					i.active = False
					i.save()
			menu = form.save(commit=False)
			menu.session = 'khana'
			menu.author = request.user
			menu.save()
			messages.success(request, f'MENU ADDED')
			return redirect('mymess', username=request.user)
	else:
		form = AddMenuForm()
		context = locals()
		return render(request, 'users/mymess.html', {'form': form})


@login_required
def update_menu(request, pk):
	post = Post.objects.get(id=pk)
	if request.method == "POST":
		umform = AddMenuForm(request.POST, instance=post)
		if umform.is_valid():
			posts = Post.objects.filter(author=request.user)
			for i in posts:
					i.active = False
					i.save()
			menu = umform.save(commit=False)
			menu.active = True
			menu.date_posted = timezone.now()
			if timezone.now().hour > 14:
				menu.session = 'dinner'
			else:
				menu.session = 'lunch'
			menu.save()
			messages.success(request, f'MENU UPDATED')
			return redirect('mymess', username=request.user)
	else:
		umform = AddMenuForm(instance=post)
		context = locals()
		return render(request, 'users/mymess.html' , context)


@login_required
def activate(request, pk):
	post = Post.objects.get(id=pk)
	posts = Post.objects.filter(author=request.user)
	for i in posts:
		i.active = False
		i.session = 'old'
		i.save()
	post.active = True
	post.date_posted = timezone.now()
	if timezone.now().hour > 14:
		post.session = 'dinner'
	else:
		post.session = 'lunch'
	post.save()
	messages.success(request, f'MENU IS NOW LIVE')
	context = locals()
	return redirect('mymess', username=request.user)


def menulist(request):
	user=request.user
	if user.is_authenticated:
		if request.method == "POST":
			form = AddMenuForm(request.POST, request.FILES)
			if form.is_valid():
				posts = Post.objects.filter(author=request.user)
				for i in posts:
						i.active = False
						i.session = 'old'
						i.save()
				menu = form.save(commit=False)
				menu.author = request.user
				menu.city = request.user.profile.city
#				menu.image = form.cleaned_data["image"]
				if timezone.now().hour > 14:
					menu.session = 'dinner'
				else:
					menu.session = 'lunch'
				menu.save()
				saved = True
				messages.success(request, f'MENU ADDED')
				return redirect('mymess', username=request.user)
		else:
			form = AddMenuForm()

#	if not request.COOKIES.get('city'):
#		return render(request, 'blog/set_city.html')
#	else:
#		city = request.COOKIES.get('city')
	posts = Post.objects.filter(active=True).order_by('-date_posted')
	for i in posts:
		if i.date_posted < timezone.now()-timedelta(hours=12):
			i.session = 'old'
			i.save()
	if timezone.now().hour > 14:
		session = 'dinner'
	else:
		session = 'lunch'


	pinlist = []

	for i in posts:
		if request.COOKIES.get(i.author.username):
			pinlist.append(i)
		context = locals()
	return render(request, 'blog/home.html', context)


clean_menu = ['Sev tamatar, dudhi chana, roti, dal, rice, buttermilk, salad', 'Pani puri Baingan Bharta sev tameta  Dal Gujarati dal Punjabi rice roti buttermilk and green slat', 'DRY FRUIT KHEER, BATAKAWADA, MATAR PANEER, DAL RICE, PURI, RAMKADA', 'Pani puri, sev tameta, ringan oro, bajri, rotla, tava roti, dal rice, salad, chhas', 'BATAKA VATANA TAMETA, VATANA, roti, dal-rice, salad, chhas', 'Pani puri, Baingan Bharta, sev tameta , Dal Gujarati, dal Punjabi, rice, roti, buttermilk and green slat', 'BHINDA ALU FRY, MUG, ROTI, DAL, RICE, BUTTERMILK, SALAD', 'PAVBHAJI, MASALA RICE, Masala Onion, Garlic CHATNI', 'RINGAN BATETA,  DEAHIVAL, roti, dal-rice, salad, chhas', 'CHOLE CHANA, SUKI BHAJI, BHATURE, ROTI, DAL, RICE, BUTTERMILK, SALAD', 'Live Manchurian noodle, pav bhaji, dal fry, jeera rice, limbu, chhas, ramkda', 'LIVE DHOKALA, MATAR PANEER, roti, dal-rice, salad, chhas', 'Bhakhri, bataka vatana tamata, masur, tikhari, roti, dal, rice, buttermilk, salad']
def autocomplete(request):
	return HttpResponse(json.dumps(clean_menu), content_type="application/json")


def set_city(request, cityname):   
	response = redirect('blog-home')
	response.set_cookie('city', cityname, 3600 * 24 * 365 * 2)
	messages.success(request,"YOUR DEFAULT CITY SET TO {}".format(cityname))
	return response

def pin(request, username):   
	response = redirect('blog-home')
	response.set_cookie(username, 'pin', 3600 * 24 * 365 * 2)
	messages.success(request,"Added to watchlist")
	return response

def unpin(request, username):   
	response = redirect('blog-home')
	response.delete_cookie(username)
	messages.success(request,"Removed from watchlist")
	return response