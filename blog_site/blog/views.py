from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView ,ListView
from django.views.generic.edit import CreateView
from django.contrib import messages
from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
    template_name = 'home.html'
    model = Blog
    context_object_name = 'blogs'

class CreateBlogPost(CreateView):
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