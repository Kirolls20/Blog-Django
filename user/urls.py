from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns =[
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('create-New-Account/',views.RegisterUserView.as_view(),name='register_user')
]   