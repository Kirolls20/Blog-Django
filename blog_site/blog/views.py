from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView ,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib import messages
from .models import Blog,User
from .forms import BlogForm

class BlogListView(ListView):
    template_name = 'home.html'
    model = Blog
    context_object_name = 'blogs'

class CreateBlogPost(LoginRequiredMixin,CreateView):
    template_name= 'create_blog.html'
    model= Blog
    form_class= BlogForm

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self,form):
        form= form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin,DetailView):
    template_name='profile.html'
    model= User
    context_object_name = 'user'

    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(user= self.request.user).all()
        return context
