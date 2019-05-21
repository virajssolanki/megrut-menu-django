from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib import messages
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


@login_required
def delete_menu(request, pk):
	menu = Post.objects.get(id=pk)
	menu.delete()
	messages.danger(request, f'Menu Deleted')
	return render(request, 'users/mymess.html' , context)


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
			messages.success(request, f'Menu is live')
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
			menu.save()
			messages.success(request, f'Updated success')
			return redirect('mymess', username=request.user)
	else:
		form = AddMenuForm(instance=post)
		context = locals()
		return render(request, 'users/mymess.html' , context)


def menulist(request):
	posts = Post.objects.filter(active=True)
	context = locals()
	return render(request, 'blog/home.html', context)


@login_required
def activate(request, pk):
	post = Post.objects.get(id=pk)
	posts = Post.objects.filter(author=request.user)
	for i in posts:
		i.active = False
		i.save()
	post.active = True
	post.save()
	messages.success(request, f'Menu is now live')
	context = locals()
	return redirect('mymess', username=request.user)