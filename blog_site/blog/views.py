from django.shortcuts import render
from django.views.generic import TemplateView ,ListView

from .models import Blog

class BlogListView(ListView):
    template_name = 'home.html'
    model = Blog
    context_object_name = 'blogs'

