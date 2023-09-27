from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogHome.as_view(),name='home'),
    path('create/blog-post/',views.CreateBlogPost.as_view(),name='create_blog'),
    path('user/<int:pk>/profile/',views.ProfileView.as_view(),name='profile'),
    path('edit/<int:pk>/blogpost/',views.EditBlogView.as_view(),name='edit_blog'),
    path('delete/<int:pk>/blogpost/',views.DeleteBlogView.as_view(),name='delete_blog'),
]