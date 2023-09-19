from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

from blog.forms import createNewAccountForm
from blog.models import User


class LoginView(TemplateView):
    template_name = 'registeration/login.html'
    
    def post(self,request):
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user= authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,('You logged in Successfully!'))
                return redirect('home')
            else:
                messages.error(request,('Something went wrong try again!!'))
                return redirect('login')
        
class RegisterUserView(CreateView):
    template_name = 'registeration/register.html'
    model=User
    form_class = createNewAccountForm
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('login')



