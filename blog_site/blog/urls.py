from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogListView.as_view(),name='home'),
    path('create/blog-post/',views.CreateBlogPost.as_view(),name='create_blog')
]