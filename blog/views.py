from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages import constants as message_constants
from .forms import AddMenuForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
									 LoginRequiredMixin, 
									 UserPassesTestMixin,

									 )
from django.views.generic import (
									ListView, 
									DetailView, 
									CreateView, 
									UpdateView,
									DeleteView
									)
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
			menu.author = request.user
			menu.save()
			messages.success(request, f'MENU ADDED')
			return redirect('mymess', username=request.user)
	else:
		form = AddMenuForm()
		return render(request, 'users/mymess.html', {'form': form})


@login_required
def update_menu(request, pk):
	post = Post.objects.get(id=pk)
	if request.method == "POST":
		form = AddMenuForm(request.POST, instance=post)
		if form.is_valid():
			posts = Post.objects.filter(author=request.user)
			for i in posts:
					i.active = False
					i.save()
			menu = form.save(commit=False)
			menu.active = True
			menu.date_posted = timezone.now()
			menu.save()
			messages.success(request, f'MENU UPDATED')
			return redirect('mymess', username=request.user)
	else:
		form = AddMenuForm(instance=post)
		context = locals()
		return render(request, 'users/mymess.html' , context)


@login_required
def activate(request, pk):
	post = Post.objects.get(id=pk)
	posts = Post.objects.filter(author=request.user)
	for i in posts:
		i.active = False
		i.save()
	post.active = True
	post.date_posted = timezone.now()
	post.save()
	messages.success(request, f'MENU IS NOW LIVE')
	context = locals()
	return redirect('mymess', username=request.user)


def menulist(request):
	nomenu_users = []
	users = User.objects.all()
	for i in users:
		menu = Post.objects.filter(author=i).first()
		if menu is None:
			nomenu_users.append(i)

	posts = Post.objects.filter(active=True).order_by('-date_posted')
	context = locals()
	return render(request, 'blog/home.html', context)