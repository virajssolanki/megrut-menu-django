from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username  = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			messages.success(request, f'Account created for {username}!')
			return redirect('mymess', username=username)
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

@login_required
def edit_profile(request, username):
	user = User.objects.get(username=username)
	if request.user == user:
		if request.method == 'POST':
			u_form = UserUpdateForm(request.POST, instance=request.user)
			p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()
				messages.success(request, f'Updated success')
				return redirect('mymess', username=user.username)
		else:
			u_form = UserUpdateForm(instance=request.user)
			p_form = ProfileUpdateForm(instance=request.user.profile)
	context = locals()
	return render(request, 'users/edit_profile.html', context)

@login_required
def mymess(request, username):
	user = User.objects.get(username=username)
	active_post = Post.objects.filter(author=request.user).filter(active=True)
	posts = Post.objects.filter(author=request.user).filter(active=False)
	if request.user == user:
		context = locals()
		return render(request, 'users/mymess.html', context)


def mess_profile(request, username):
	user = User.objects.get(username=username)
	context = locals()
	return render(request, 'users/mess_profile.html', context)

def close_mess(request, username):
	user = User.objects.get(username=username)
	user.profile.close = True
	user.save()
	return redirect('mymess', username=user.username)

def open_mess(request, username):
	user = User.objects.get(username=username)
	user.profile.close = False
	user.save()
	return redirect('mymess', username=user.username)