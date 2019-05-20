from django.shortcuts import render, redirect
from .models import Post
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

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'users/mymess.html'

	fields = ['menu', 'price']

		
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['menu','price']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False 


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
			return redirect('mymess', username=request.user)
	else:
		form = AddMenuForm()
		return render(request, 'users/mymess.html', {'form': form})