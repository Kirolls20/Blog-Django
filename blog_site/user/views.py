from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout


class LoginView(TemplateView):
    template_name = 'registeration/login.html'
    
    def post(self,request):
        if not  request.user.is_authenticated:
            if request.method == 'POST':
                username = request.POST['username']
                password= request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfully')
                    return redirect('home')
                else:
                    messages.error(request,('Something went wrong try again!!'))
                    return redirect('login')
        return redirect('home')
        
                

